from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

import random
from datetime import datetime, timedelta
from decimal import Decimal

from .models import (
	NaturalPerson,
	LegalPerson,
	Address,
 	Email,
	Phone,
    Account,
    Investment,
    AccountInvestments,
    Loan,
    Installment,
    Card,
    CardTransaction,
    Statement
)

from .serializers import (
	NaturalPersonSerializer,
	LegalPersonSerializer,
	AddressSerializer,
 	EmailSerializer,
	PhoneSerializer,
    AccountSerializer,
    AccountPatchSerializer,
    AccountRequestSerializer,
    InvestmentSerializer,
    AccountInvestmentSerializer,
    LoanSerializer,
    CreateLoanSerializer,
    InstallmentSerializer,
    CardSerializer,
    CardRequestSerializer,
    CardTransactionSerializer,
)

from .permissions import (
    IsSuperUser,
    NormalUserGet,
    NormalUserPost,
    NormalUserGetPost,
    NormalUserPostPatch,
    NormalUserGetPostPatch
)

from .utils.filters import filtering_by_user
from core import serializers

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
        return AccountSerializer


class CreateAccountViewSet(viewsets.GenericViewSet):
    permission_classes = [
        NormalUserPost
    ]
    serializer_class = AccountRequestSerializer

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
        
        return Response({'Successfully created': f'Agency: {agency}, Number: {number}, Credit Limit: R${credit_limit}'}, status=status.HTTP_201_CREATED)
    

#INVESTMENT VIEW
class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    permission_classes = [
        NormalUserGet
    ]


#ACCOUNT INVESTMENT VIEW
class AccountInvestmentViewSet(viewsets.ModelViewSet):
    serializer_class = AccountInvestmentSerializer
    permission_classes = [
        NormalUserPost
    ]

    def get_queryset(self):
        account = self.kwargs['account']
        return AccountInvestments.objects.filter(id_account=account)
    
    
#LOAN VIEW
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [
        NormalUserGetPostPatch
    ]


class CreateLoanViewSet(viewsets.GenericViewSet):
    permission_classes = [
        NormalUserGetPost
    ]
    serializer_class = CreateLoanSerializer

    def create(self, request):
        request_date = datetime.now()
        interest_rate = 15
        is_approved = True
        approval_date = datetime.now()
        amount_request = request.data.get('amount_request')
        installment_amount = request.data.get('installment_amount')
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
                    id_loan = get_object_or_404(Loan, pk=1),
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

            return Response({'Request': f'Amount: {amount_request} Installments: {installment_amount}, Interest rate: {interest_rate}'}, status=status.HTTP_201_CREATED)
        else:
            loan = Loan.objects.create(
                id_account = account,
                request_date = request_date,
                amount_request = amount_request,
                interest_rate = interest_rate,
                installment_amount = installment_amount,
                is_approved = False,
                observation = 'Not approved! Amount requested exceeds your credit limit by more than 3 times'
            )
            return Response({'Request': 'Not approved! Amount requested exceeds your credit limit by more than 3 times'}, status=status.HTTP_201_CREATED)



#INSTALLMENT VIEW
class InstallmentViewSet(viewsets.ModelViewSet):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer
    permission_classes = [
        NormalUserGetPostPatch
    ]
    

#CARD VIEW
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [
        NormalUserGetPostPatch
    ]


class CreateCardViewSet(viewsets.GenericViewSet):
    permission_classes = [
        NormalUserPost
    ]
    serializer_class = CardRequestSerializer

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
        
        return Response({'Successfully created': f'Number: {number}, Expiration: {expiration_date}, Verification Code: {cv}'}, status=status.HTTP_201_CREATED)
    
    
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
