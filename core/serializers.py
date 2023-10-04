from rest_framework import serializers

from django.contrib.auth import get_user_model

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
	Transaction
)

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = [
            'register_number',
            'password',
        ]
        

class NaturalPersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NaturalPerson
        fields = [
            'user',
			'name',
			'birth_date',
			'cpf',
			'rg',
			'social_name'
		]
        
        
class LegalPersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LegalPerson
        fields = [
            'user',
			'fantasy_name',
			'establishment_date',
			'cnpj',
   			'municipal_registration',
			'state_registration',
            'legal_nature'
		]
        
    
class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = [
			'user',
   			'street',
			'number',
			'neighborhood',
			'city',
   			'state',
			'cep',	
		]
        

class EmailSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = Email
        fields = [
			'user',
            'email'	
		]
        
        
class PhoneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Phone
        fields = [
			'user',
   			'area_code',
			'prefix_number',
            'phone_number'
		]
        

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = [
            'user',
            'agency',
            'number',
            'type',
            'balance',
            'credit_limit',
            'is_active'
        ]
        
        
class AccountRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = [
            'type'
        ]
        
        
class AccountPatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = [
            'user'
        ]
        

class InvestmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Investment
        fields = [
			'type',
            'contribution',
            'admin_fee',
            'period',
            'risc_rate',
            'profitability',
            'is_active'
		]


class AccountInvestmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountInvestments
        fields = [
            'id_account',
            'id_investment'
        ]
        

class LoanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Loan
        fields = [
			'id_account',
			'request_date',
            'amount_request',
            'interest_rate',
            'installment_amount',
            'observation'	
		]
        
    
class InstallmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Installment
        fields = [
			'id_loan',
			'number',
			'expiration_date',
			'payment_date',
			'payment_amount'
		]
        
        
class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Card
        fields = [
			'id_account',
            'number',
            'expiration_date',
            'flag',
            'verification_code',
            'is_active',
		]
        

class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = [
            'id_card',
            'type',
            'timestamp',
            'operation',
            'amount'
		]