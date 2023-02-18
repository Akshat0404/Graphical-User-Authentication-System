# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model
# User = get_user_model()
# from django.forms.widgets import PasswordInput, TextInput
# from django.core.exceptions import ValidationError


# class CustomUserCreationForm(forms.Form):
#     email = forms.EmailField(widget=TextInput(attrs={'class':'validate','id': 'icon_prefix', 'type': 'text'}))
#     name = forms.CharField(widget=TextInput(attrs={'class':'validate','id': 'icon_prefix', 'type': 'text'}), min_length=2, max_length=150)
    

#     def clean_email(self):
#         email = self.cleaned_data['email'].lower()
#         r = User.objects.filter(email=email)
#         if r.count():
#             raise  ValidationError("Email already exists")
#         return email


#     def clean_name(self):
#         name = self.cleaned_data['name']
        
#         return name

#     def save(self, commit=True):
#         user = User.objects.create_user(
#             self.cleaned_data['username'],
#             name= self.cleaned_data['name'],
#         )
#         return user