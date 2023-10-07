from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import(
    NaturalPersonViewSet,
    LegalPersonViewSet,
    AddressViewSet,
    EmailViewSet,
    PhoneViewSet,
    AccountViewSet,
    CreateAccountViewSet,
    InvestmentViewSet,
    AccountInvestmentViewSet,
    LoanViewSet,
    CreateLoanViewSet,
    InstallmentViewSet,
    CardViewSet,
    CreateCardViewSet,
    TransactionViewSet,
)

router = SimpleRouter()
router.register('natural-people', NaturalPersonViewSet, basename='natural-people')
router.register('legal-people', LegalPersonViewSet, basename='legal-people')
router.register('addresses', AddressViewSet, basename='addresses')
router.register('emails', EmailViewSet, basename='emails')
router.register('phones', PhoneViewSet, basename='phones')
router.register('accounts', AccountViewSet, basename='accounts')
router.register('accounts-new', CreateAccountViewSet, basename='create-account')
router.register('investments', InvestmentViewSet, basename='investments')
router.register('investments/account/new', AccountInvestmentViewSet, basename='account-investments')
router.register('loans', LoanViewSet)
router.register('loans-new', CreateLoanViewSet, basename='create-loan')
router.register('installments', InstallmentViewSet)
router.register('cards', CardViewSet)
router.register('cards-new', CreateCardViewSet, basename='new-card')
router.register('transactions', TransactionViewSet)

urlpatterns = [
	path('investments/account/<int:account>/', AccountInvestmentViewSet.as_view({'get': 'list'}), name='account-investments')
]
