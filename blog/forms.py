from django import  forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=128)
    message = forms.CharField(widget=forms.Textarea, label="Message")
    username = forms.EmailField(label= "email")
    renvoi = forms.BooleanField(help_text="Cochez ici", required=False)
    
    
class  NouveauContactForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    photo = forms.ImageField()