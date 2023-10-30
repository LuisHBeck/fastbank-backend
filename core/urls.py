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
    AccountInvestmentViewSet,
    LoanViewSet,
    InstallmentViewSet,
    CardViewSet,
    CardTransactionViewSet,
    PixViewSet,
    StatementViewSet
)

router = SimpleRouter()
router.register('natural-people', NaturalPersonViewSet, basename='natural-people')
router.register('legal-people', LegalPersonViewSet, basename='legal-people')
router.register('addresses', AddressViewSet, basename='addresses')
router.register('emails', EmailViewSet, basename='emails')
router.register('phones', PhoneViewSet, basename='phones')
router.register('accounts', AccountViewSet, basename='accounts')
router.register('investments', InvestmentViewSet, basename='investments')
router.register('account-investments', AccountInvestmentViewSet, basename='account-investments') # REVIEW
router.register('loans', LoanViewSet, basename='loans')
router.register('installments', InstallmentViewSet, basename='installments')
router.register('cards', CardViewSet, basename='loans')
router.register('card-transactions', CardTransactionViewSet, basename='cards-transactions')
router.register('pix', PixViewSet, basename='pix')
router.register('statements', StatementViewSet, basename='statements')

urlpatterns = [
	path('investments/account/<int:account>/', AccountInvestmentViewSet.as_view({'get': 'list'}), name='account-investments')
]
