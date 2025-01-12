from django import forms
from .models import grocrey,vegitables
from django import forms

class vegitablesForm(forms.ModelForm):
    class Meta:
        model = vegitables
        fields = '__all__'
        labels = {
            'vname' : 'Vegitable Name ',
            'vprice' : 'Price',
            'vinfo' : "Vegitable Info",
            'vimg': 'Vegitable Image'
        }
        widget = {
            'vname' : forms.TextInput(attrs={'class': 'form-control'}),
            'vprice' : forms.NumberInput(attrs={'class': 'form-control'}),
            'vimg' : forms.FileInput(attrs={'class': 'form-control'}),
            'vinfo' : forms.Textarea(attrs={'class': 'form-control'}),
        }


class groceryForm(forms.ModelForm):
    class Meta:
        model = grocrey
        fields = '__all__'
        labels = {
            'gname' : 'Vegitable Name ',
            'gprice' : 'Price',
            'ginfo' : "Vegitable Info",
            'gimg': 'Vegitable Image'
        }
        widget = {
            'gname' : forms.TextInput(attrs={'class': 'form-control'}),
            'gprice' : forms.NumberInput(attrs={'class': 'form-control'}),
            'gimg' : forms.FileInput(attrs={'class': 'form-control'}),
            'ginfo' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class SearchForm(forms.ModelForm):
    query = forms.CharField(max_length=100, label='Search', required=False)

# marketAdmin/forms.py


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nom')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')

