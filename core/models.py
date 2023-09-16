from django.db import models

from django.contrib.auth.models import(
    AbstractUser, 
    BaseUserManager
)


class CustomUserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, register_number, password, **extra_fields):
		if not register_number:
			raise ValueError('Your register number is required')
		user = self.model(register_number=register_number, username=register_number, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_user(self, register_number, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(register_number, password, **extra_fields)
    
	def create_superuser(self, register_number, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_staff', True)
		
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser needs the is_superuser=True')
		
		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser needs the is_staff=True') 
		return self._create_user(register_number, password, **extra_fields)
	

class CustomUser(AbstractUser):
	"""
		Custumized User model
	"""
	register_number = models.IntegerField(unique=True, primary_key=True)
	picture = models.CharField(max_length=255)
	is_staff = models.BooleanField(default=True)

	USERNAME_FIELD = 'register_number'
	REQUIRED_FIELDS = ['picture']
	

	def __str__(self) -> str:
		return str(self.register_number)
	
	objects = CustomUserManager()
	

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
	# USER FK FIELD
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
    # USER FK FIELD
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
    # USER FK FIELD
    phone_number = models.CharField(max_length=10)
    prefix_number = models.CharField(max_length=3)
    area_code = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'phone'
        verbose_name_plural = 'phones'
        
    def __str__(self):
        return f'{self.prefix_number} {self.area_code} {self.phone_number}'
        