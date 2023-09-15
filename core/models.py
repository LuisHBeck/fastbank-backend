from django.db import models

from django.contrib.auth.models import(
    AbstractUser, 
    BaseUserManager
)


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
    