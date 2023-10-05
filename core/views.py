from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

import random
from datetime import datetime, timedelta

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
    Transaction,
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
    InstallmentSerializer,
    CardSerializer,
    CardRequestSerializer,
    TransactionSerializer,
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
            flag="Mastercad",
            verification_code=cv,
            is_active=True,
        )
        
        return Response({'Successfully created': f'Number: {number}, Expiration: {expiration_date}, Verification Code: {cv}'}, status=status.HTTP_201_CREATED)
    
    
#TRANSACTION VIEW
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [
        NormalUserGetPostPatch
    ]