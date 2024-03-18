from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Product
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number', 'address',)

class LoginForm(AuthenticationForm):
    pass


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['picture', 'name', 'description', 'price', 'brand']