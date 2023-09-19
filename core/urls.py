from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import(
    NaturalPersonViewSet,
    LegalPersonViewSet,
    AddressViewSet,
    EmailViewSet,
    PhoneViewSet,
    AccountViewSet,
    InvestmentViewSet,
    LoanViewSet,
    InstallmentViewSet,
    CardViewSet,
    TransactionViewSet,
)

router = SimpleRouter()
router.register('natural-person', NaturalPersonViewSet)
router.register('legal-person', LegalPersonViewSet)
router.register('addresses', AddressViewSet)
router.register('emails', EmailViewSet)
router.register('phones', PhoneViewSet)
router.register('accounts', AccountViewSet)
router.register('investments', InvestmentViewSet)
router.register('loans', LoanViewSet)
router.register('installments', InstallmentViewSet)
router.register('cards', CardViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = [
	
]
