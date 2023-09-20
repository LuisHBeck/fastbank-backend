from rest_framework import viewsets

from .models import (
	NaturalPerson,
	LegalPerson,
	Address,
 	Email,
	Phone,
    Account,
    Investment,
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
    InvestmentSerializer,
    LoanSerializer,
    InstallmentSerializer,
    CardSerializer,
    TransactionSerializer,
)

from .permissions import (
    IsSuperUser,
    NormalUserGet,
    NormalUserPost,
    NormalUserGetPost,
    NormalUserPostPut,
    NormalUserGetPostPut
)

from .utils.filters import filtering_by_user

#NATURAL PERSON VIEW 
class NaturalPersonViewSet(viewsets.ModelViewSet):
    serializer_class = NaturalPersonSerializer
    permission_classes = [
		NormalUserGetPostPut
	]
    
    def get_queryset(self):
        user = self.request.user
        return filtering_by_user(NaturalPerson, user)
    
#LEGAL PERSON VIEW
class LegalPersonViewSet(viewsets.ModelViewSet):
    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer
    permission_classes = [
        NormalUserGetPostPut
    ]
    
    def get_queryset(self):
        user = self.request.user
        return filtering_by_user(LegalPerson, user)
    
#ADDRESS VIEW
class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [
        NormalUserGetPostPut
    ]
    
    def get_queryset(self):
        user = self.request.user
        return filtering_by_user(Address, user)
    
#EMAIL VIEW
class EmailViewSet(viewsets.ModelViewSet):
    serializer_class = EmailSerializer
    permission_classes = [
        NormalUserGetPostPut
    ]
    
    def get_queryset(self):
        user = self.request.user
        return filtering_by_user(Email, user)
    

#PHONE VIEW
class PhoneViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneSerializer
    permission_classes = [
        NormalUserGetPostPut
    ]
    
    def get_queryset(self):
        user = self.request.user
        return filtering_by_user(Phone, user)
    
    
#ACCOUNT VIEW
class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [
        NormalUserGetPost
    ]
    
    def get_queryset(self):
        user = self.request.user
        return filtering_by_user(Account, user)
    

#INVESTMENT VIEW
class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    permission_classes = [
        NormalUserGetPostPut
    ]
    
    
#LOAN VIEW
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [
        NormalUserGetPostPut
    ]
    

#INSTALLMENT VIEW
class InstallmentViewSet(viewsets.ModelViewSet):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer
    permission_classes = [
        NormalUserGetPostPut
    ]
    

#CARD VIEW
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [
        NormalUserGetPostPut
    ]
    
    
#TRANSACTION VIEW
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [
        NormalUserGetPostPut
    ]