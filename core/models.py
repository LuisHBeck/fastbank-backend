from django.db import models
from django.contrib.auth import get_user_model

from users.models import CustomUser

class NaturalPerson(models.Model):
	"""
        Natural Person model
    """
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="natural_person")
	name = models.CharField(max_length=50)
	birth_date = models.DateField()
	cpf = models.CharField(max_length=11)
	rg = models.CharField(max_length=8)
	social_name = models.CharField(max_length=50)

	class Meta:
		verbose_name = 'natural person'
		verbose_name_plural = 'natural persons'

	def __str__(self) -> str:
		return f'{self.cpf}'
	

class LegalPerson(CustomUser):
	"""
        Legal Person model
    """
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="legal_person")
	fantasy_name = models.CharField(max_length=100)
	establishment_date = models.DateField
	cnpj = models.CharField(max_length=14)
	municipal_registration = models.CharField(max_length=11)
	state_registration = models.CharField(max_length=9)
	legal_nature = models.CharField(max_length=100)

	class Meta:
		verbose_name = 'legal person'
		verbose_name_plural = 'legal persons'

	def __str__(self) -> str:
		return f'{self.cnpj}'
	
# BANK MODELS
class Base(models.Model):
	"""
	Base abstract class for all models
	"""
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
    
    
class Address(Base):
	"""
	  Address model
	"""
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	street = models.CharField(max_length=50)
	number = models.CharField(max_length=5)
	neighborhood = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	cep = models.CharField(max_length=12)
	
  
	class Meta:
		verbose_name = 'address'
		verbose_name_plural = 'addresses'
      
	def __str__(self):
		return f'{self.street} {self.street}'
  
  
class Email(Base):
    """
      Email model
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_email')
    email = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'email'
        verbose_name_plural = 'emails'
    
    def __str__(self):
        return f'{self.email}'
    

class Phone(Base): 
    """
    Phone model
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    area_code = models.CharField(max_length=3)
    prefix_number = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'phone'
        verbose_name_plural = 'phones'
        
    def __str__(self):
        return f'{self.prefix_number} {self.area_code} {self.phone_number}'
		

class Account(Base):
	"""
      Account model
    """
	ACCOUNT_TYPE_CHOICES = [
		['Current', 'Current'],
		['Savings', 'Savings'],
	]
	user = models.ManyToManyField(get_user_model())
	agency = models.CharField(max_length=15)
	number = models.CharField(max_length=15)
	type = models.CharField(max_length=8, choices=ACCOUNT_TYPE_CHOICES)
	balance = models.DecimalField(decimal_places=2, max_digits=7)
	credit_limit = models.DecimalField(decimal_places=2, max_digits=7)
	is_active = models.BooleanField(default=True)


	class Meta:
		verbose_name = 'account'
		verbose_name_plural = 'accounts'

	def __str__(self):
		return f'{self.agency} {self.number}'
	

class Investment(Base):
	"""
      Investment model
    """
	id_account = models.ForeignKey(Account, on_delete=models.CASCADE)
	type = models.CharField(max_length=50)
	contribution = models.DecimalField(decimal_places=2, max_digits=7)
	admin_fee = models.DecimalField(decimal_places=2, max_digits=7)
	period = models.DateField()
	risc_rate = models.DecimalField(decimal_places=2, max_digits=7)
	profitability = models.DecimalField(decimal_places=2, max_digits=7)
	is_active = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'investment'
		verbose_name_plural = 'investments'

	def __str__(self):
		return f'{self.type}'
	

class Loan(Base):
	"""
      Loan model
    """
	id_account = models.ForeignKey(Account, on_delete=models.CASCADE)
	request_date = models.DateField()
	amount_request = models.DecimalField(decimal_places=2, max_digits=7)
	interest_rate = models.DecimalField(decimal_places=2, max_digits=7)
	is_approved = models.BooleanField(default=True)
	approval_date = models.DateField(blank=True, null=True)
	installment_amount = models.IntegerField()
	observation = models.TextField()

	class Meta:
		verbose_name = 'loan'
		verbose_name_plural = 'loans'

	def __str__(self):
		return f'{self.amount_request}'
	

class Installment(Base):
	"""
      Installment model
    """
	id_loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
	number = models.CharField(max_length=50)
	expiration_date = models.DateField()
	payment_date = models.DateField(blank=True, null=True)
	payment_amount = models.DecimalField(decimal_places=2, max_digits=7)

	class Meta:
		verbose_name = 'installment'
		verbose_name_plural = 'installments'

	def __str__(self):
		return f'{self.number}'
	

class Card(Base):
	"""
      Card model
    """
	id_account = models.ForeignKey(Account, on_delete=models.CASCADE)
	number = models.CharField(max_length=50)
	expiration_date = models.DateField()
	flag = models.CharField(max_length=25)
	verification_code = models.CharField(max_length=25)
	is_active = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'card'
		verbose_name_plural = 'cards'

	def __str__(self):
		return f'{self.number}'
	

class Transaction(Base):
	"""
      Transaction model
    """
	id_card = models.ForeignKey(Card, on_delete=models.CASCADE)
	type = models.CharField(max_length=25)
	timestamp = models.DateField()
	operation = models.CharField(max_length=25)
	amount = models.DecimalField(decimal_places=2, max_digits=7)

	class Meta:
		verbose_name = 'transaction'
		verbose_name_plural = 'transactions'

	def __str__(self):
		return f'{self.type}' 