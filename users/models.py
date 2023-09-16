from django.db import models

from django.contrib.auth.models import(
    AbstractUser, 
    BaseUserManager
)

# CUSTOM USER CONFIG
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
