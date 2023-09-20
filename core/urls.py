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
router.register('natural-person', NaturalPersonViewSet, basename='natural-person')
router.register('legal-person', LegalPersonViewSet, basename='legal-person')
router.register('addresses', AddressViewSet, basename='addresses')
router.register('emails', EmailViewSet, basename='emails')
router.register('phones', PhoneViewSet, basename='phones')
router.register('accounts', AccountViewSet)
router.register('investments', InvestmentViewSet)
router.register('loans', LoanViewSet)
router.register('installments', InstallmentViewSet)
router.register('cards', CardViewSet)
router.register('transactions', TransactionViewSet)

urlpatterns = [
	
]
