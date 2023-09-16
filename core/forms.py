from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm): 
    
    class Meta:
        model = CustomUser
        fields = [
            'picture'
        ]
        labels = {'username': 'Register Number'}
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.register_number = self.cleaned_data['username']
        
        if commit:
            user.save()
        return user
    
    
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = [
            'picture'
        ]