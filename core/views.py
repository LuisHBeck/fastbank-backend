from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

import random
from datetime import datetime, timedelta
from decimal import Decimal

from .models import *

from .serializers import *

from .permissions import *

from .utils.filters import *

#NATURAL PERSON VIEW 
class NaturalPersonViewSet(viewsets.ModelViewSet):
    serializer_class = NaturalPersonSerializer
    permission_classes = [
		NormalUserGetPostPatch
	]
    
    def get_queryset(self):
        user = self.request.user
        return filtering_by_user(NaturalPerson, user)
    
    
#LEGAL PERSON VIEW
class LegalPersonViewSet(viewsets.ModelViewSet):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer
    permission_classes = [
        NormalUserGetPostPatch
    ]
    
    def get_queryset(self):
        user = self.request.user
        return filtering_by_user(LegalPerson, user)
    
    
#ADDRESS VIEW
class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [
        NormalUserGetPostPatch
    ]
    
    def get_queryset(self):
        user = self.request.user
        return filtering_by_user(Address, user)
    
    
#EMAIL VIEW
class EmailViewSet(viewsets.ModelViewSet):
    serializer_class = EmailSerializer
    permission_classes = [
        NormalUserGetPostPatch
    ]
    
    def get_queryset(self):
        user = self.request.user
        return filtering_by_user(Email, user)
    

#PHONE VIEW
class PhoneViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneSerializer
    permission_classes = [
        NormalUserGetPostPatch
    ]
    
    def get_queryset(self):
        user = self.request.user
        return filtering_by_user(Phone, user)
    
    
#ACCOUNT VIEW
class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = [
        NormalUserGetPostPatch
    ]
    
    def get_queryset(self):
        user = self.request.user
        return filtering_by_user(Account, user)
    
    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return AccountPatchSerializer
        elif self.request.method == 'POST':
            return CreateAccountSerializer
        return AccountSerializer
    
    def create(self, request):
        last_account = Account.objects.order_by('-number').first()
        if last_account:
            next_account = last_account.number + 1
        else:
            next_account = 1111
            
        user = self.request.user
        agency = 1
        number = f'{next_account:03}'
        type = request.data.get('type')
        balance = 0
        credit_limit = 500
        
        account = Account.objects.create(
            agency=agency,
            number=int(number),
            type=type,
            balance=balance,
            credit_limit=credit_limit
        )
        account.user.add(user)
        return Response({'created': f'Agency: {agency}, Number: {number}, Credit Limit: R${credit_limit}'}, status=status.HTTP_201_CREATED)
    

#INVESTMENT VIEW
class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    permission_classes = [
        NormalUserGet
    ]


#ACCOUNT INVESTMENT VIEW
class AccountInvestmentViewSet(viewsets.ModelViewSet):
    # queryset = AccountInvestments.objects.all()
    serializer_class = AccountInvestmentSerializer
    permission_classes = [
        NormalUserGetPost
    ]

    def get_queryset(self):
        user = self.request.user
        account = self.request.query_params.get('account')
        return filtering_by_account(AccountInvestments, account, user)
    

    def create(self, request):
        acc_number = request.data.get('id_account')
        investment_id = request.data.get('id_investment')

        account = get_object_or_404(Account, pk=acc_number)
        investment = get_object_or_404(Investment, pk=investment_id)

        if account.balance >= investment.contribution:
            acc_investment = AccountInvestments.objects.create(
                id_account = account,
                id_investment = investment
            )

            account.balance -= investment.contribution
            account.save()

            statement = Statement.objects.create(
                id_account = account,
                transaction_type = '-*',
                amount = investment.contribution,
                balance = account.balance
            )

            return Response({'investment': f'Successfully invested R${investment.contribution}'}, status=status.HTTP_201_CREATED)
        
        return Response({'investment': f'Insufficient founds'}, status=status.HTTP_200_OK)
    

#LOAN VIEW
class LoanViewSet(viewsets.ModelViewSet):
    permission_classes = [
        NormalUserGetPost
    ]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateLoanSerializer
        return LoanSerializer

    def get_queryset(self):
        user = self.request.user
        account = self.request.query_params.get('account')
        return filtering_by_account(Loan, account, user)
    
    def create(self, request):
        request_date = datetime.now()
        interest_rate = 15.0
        is_approved = True
        approval_date = datetime.now()
        amount_request = float(request.data.get('amount_request'))
        installment_amount = int(request.data.get('installment_amount'))
        observation = request.data.get('observation')
        id_account = request.data.get('id_account')
        account = get_object_or_404(Account, pk=id_account)
        rate_amount = amount_request * (interest_rate/100) 
        final_amount = amount_request + rate_amount
        installment_amount_value = final_amount / installment_amount

        if account.credit_limit >= (amount_request/3):
            loan = Loan.objects.create(
                id_account = account,
                request_date = request_date,
                amount_request = amount_request,
                interest_rate = interest_rate,
                is_approved = is_approved,
                approval_date = approval_date,
                installment_amount = installment_amount,
                observation = observation
            )

            for installment in range(installment_amount):
                installment_ = Installment.objects.create(
                    id_account = get_object_or_404(Account, pk=account.pk),
                    number = installment + 1,
                    expiration_date = request_date + timedelta(days=(30 * installment)),
                    payment_amount = installment_amount_value
                )

            account.balance += Decimal(amount_request)
            account.save()

            statement = Statement.objects.create(
                id_account = account,
                transaction_type = '+',
                amount = amount_request,
                balance = account.balance
            )  
            return Response({'request': f'Amount: {amount_request} Installments: {installment_amount}, Interest rate: {interest_rate}%, Final amount: {final_amount}, {installment_amount} x R${installment_amount_value}'}, status=status.HTTP_201_CREATED)
        
        loan = Loan.objects.create(
            id_account = account,
            request_date = request_date,
            amount_request = amount_request,
            interest_rate = interest_rate,
            installment_amount = installment_amount,
            is_approved = False,
            observation = 'Not approved! Amount requested exceeds your credit limit by more than 3 times'
        )
        return Response({'request': 'Not approved! Amount requested exceeds your credit limit by more than 3 times'}, status=status.HTTP_201_CREATED)


#INSTALLMENT VIEW
class InstallmentViewSet(viewsets.ModelViewSet):
    # queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer
    permission_classes = [
        NormalUserGetPostPatch
    ]

    def get_queryset(self):
        user = self.request.user
        account = self.request.query_params.get('account')
        queryset = filtering_by_account(Installment, account, user)
        if not isinstance(queryset, list):
            current_month = datetime.now().month
            queryset = queryset.filter(expiration_date__month=current_month)
        return queryset
    
    def list(self, request):
        queryset = self.get_queryset()
        final_value = self.request.query_params.get('final')
        if final_value:
            value = 0
            for installment in queryset:
                value += installment.payment_amount
            return Response({'installment_amount': value}, status=status.HTTP_200_OK) 
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def partial_update(self, request, *args, **kwargs):
        installment = self.get_object()
        loan = installment.id_loan
        account = loan.id_account
        if account.balance >= installment.payment_amount:
            account.balance -= installment.payment_amount
            account.save()
            installment.paid = True 
            installment.save()
            statement = Statement.objects.create(
                id_account = account,
                transaction_type = '-',
                amount = installment.payment_amount,
                balance = account.balance
            )  
            return Response({'Successfully paid': 'success'}, status=status.HTTP_202_ACCEPTED)

    
#CARD VIEW
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    permission_classes = [
        NormalUserGetPostPatch
    ]

    def get_queryset(self):
        user = self.request.user
        account = self.request.query_params.get('account')
        return filtering_by_account(Card, account, user)
    

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateCardSerializer
        return CardSerializer

    def create(self, request):
        size = 12
        number = random.randint(10 ** (size - 1), (10 ** size) - 1)
        cv = random.randint(10 ** (3 - 1), (10 ** 3) - 1)
        current_date = datetime.now()
        expiration_date = current_date + timedelta(days=(30 * 45))
        id_account = request.data.get('id_account')
        account = get_object_or_404(Account, pk=id_account)

        card = Card.objects.create(
            id_account=account,
            number=number,
            expiration_date=expiration_date,
            flag="Mastercard",
            verification_code=cv,
            is_active=True,
        )
        return Response({'created': f'Number: {number}, Expiration: {expiration_date}, Verification Code: {cv}'}, status=status.HTTP_201_CREATED)
    
    
#TRANSACTION VIEW
class CardTransactionViewSet(viewsets.GenericViewSet):
    serializer_class = CardTransactionSerializer
    permission_classes = [
        NormalUserGetPostPatch
    ]

    def create(self, request):
        timestamp = datetime.now()
        id_card = request.data.get('id_card')
        card = get_object_or_404(Card, pk=id_card)
        operation = "Debit"
        amount = request.data.get('amount')

        id_account = request.data.get('id_account')
        account = get_object_or_404(Account, pk=id_account)

        if (account.balance >= amount):
            card_transaction = CardTransaction.objects.create(
                id_card = card,
                timestamp = timestamp,
                operation = operation,
                amount = amount
            )
            account.balance -= Decimal(amount)
            account.save()

            statement = Statement.objects.create(
                id_account = account,
                transaction_type = '-',
                amount = amount,
                balance = account.balance
            )  
            return Response({'Success': 'Successfully created'}, status=status.HTTP_201_CREATED)
        return Response({'Fail': 'Insufficient bunds'}, status=status.HTTP_201_CREATED)
    
#PIX VIEWSET
class PixViewSet(viewsets.GenericViewSet):
    serializer_class = StatementSerializer
    permission_classes = [
        NormalUserGetPost
    ]

    def create(self, request):
        id_payer_acount = request.data.get('id_account')
        id_receiver_account = request.data.get('id_receiver_account')
        amount = request.data.get('amount')

        payer_account = get_object_or_404(Account, pk=id_payer_acount)
        receiver_account = get_object_or_404(Account, pk=id_receiver_account)

        if payer_account.balance >= Decimal(amount):
            payer_account.balance -= Decimal(amount)
            payer_account.save()
            receiver_account.balance += Decimal(amount)
            receiver_account.save()

            payer_statement = Statement.objects.create(
                id_account = payer_account,
                transaction_type = '-',
                amount = amount,
                balance = payer_account.balance
            ) 

            receiver_statement = Statement.objects.create(
                id_account = receiver_account,
                transaction_type = '+',
                amount = amount,
                balance = receiver_account.balance
            ) 
            return Response({'Success': 'Successfully transferred'}, status=status.HTTP_201_CREATED)
        return Response({'Failed': 'Insufficient founds'}, status=status.HTTP_201_CREATED)
    

class StatementViewSet(viewsets.ModelViewSet):
    serializer_class = StatementSerializer
    permission_classes = [
        NormalUserGet
    ]

    def get_queryset(self):
        user = self.request.user
        account = self.request.query_params.get('account')
        return filtering_by_account(Statement, account, user)