from django.db import models

from users.models import CustomUser

class NaturalPerson(CustomUser):
	"""
        Natural Person model
    """
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
    
    
class Addres(Base):
	"""
	  Address model
	"""
	# user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	cep = models.CharField(max_length=12)
	city = models.CharField(max_length=50)
	street = models.CharField(max_length=50)
	neighborhood = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
  
	class Meta:
		verbose_name = 'address'
		verbose_name_plural = 'addresses'
      
	def __str__(self):
		return f'{self.street} {self.street}'
  
  
class Email(Base):
    """
      Email model
    """
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    prefix_number = models.CharField(max_length=3)
    area_code = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'phone'
        verbose_name_plural = 'phones'
        
    def __str__(self):
        return f'{self.prefix_number} {self.area_code} {self.phone_number}'
        