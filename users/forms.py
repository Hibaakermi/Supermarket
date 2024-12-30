from django import forms

class Userinfo(forms.Form):
    name = forms.CharField(max_length=30,label_suffix='',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your name'}))
    email = forms.CharField(max_length=50,label_suffix='',widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Enter your email'}))
    password = forms.CharField(max_length=30,label_suffix='',widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Enter your password'}))
    cpassword = forms.CharField(label='Confirm Password',max_length=30,label_suffix='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Confirm your password'}))
    address = forms.CharField(label_suffix='',widget=forms.Textarea(attrs={'class':'form-control  mb-3 address' ,'rows':'10', 'placeholder': 'Enter your address'}))
   