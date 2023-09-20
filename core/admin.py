from django.contrib import admin

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

@admin.register(NaturalPerson)
class NaturalPersonAdmin(admin.ModelAdmin):
	list_display = [
   		'user',
		'name',
		'birth_date',
		'cpf',
		'rg',
		'social_name',
	]


@admin.register(LegalPerson)
class LegalPersonAdmin(admin.ModelAdmin):
	list_display = [
   		'user',
		'fantasy_name',
		'establishment_date',
		'cnpj',
		'municipal_registration',
		'state_registration',
		'legal_nature',
	]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'user',
		'street',
  		'number',
		'neighborhood',
		'city',
		'state',
		'cep',
	]
	ordering = ['id']


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
	list_display = [
		'id',
        'user',
        'email',
    ]
	ordering = ['id']


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
	list_display = [
		'id',
        'user',
        'area_code',
		'prefix_number',
		'phone_number',
    ]
	ordering = ['id']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
	list_display = [
		'id',
        # 'user',
		'agency',
		'number',
        'type',
        'balance',
        'credit_limit',
        'is_active',
	]
	ordering = ['id']


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
	list_display = [
		'id',
        'id_account',
        'type',
        'contribution',
        'admin_fee',
		'period',
		'risc_rate',
		'profitability',
		'is_active',
	]
	ordering = ['id']


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'id_account',
		'request_date',
		'amount_request',
		'interest_rate',
		'is_approved',
		'approval_date',
		'installment_amount',
		'observation',
	]
	ordering = ['id']


@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
	list_display = [
		'id',
        'id_loan',
		'number',
		'expiration_date',
		'payment_date',
		'payment_amount',
	]
	ordering = ['id']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
	list_display = [
		'id',
        'id_account',
        'number',
        'expiration_date',
		'flag',
		'verification_code',
        'is_active',
	]
	ordering = ['id']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
	list_display = [
		'id',
        'id_card',
        'type',
        'timestamp',
        'operation',
		'amount',
	]
	ordering = ['id']
