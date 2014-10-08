from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class FileUploadForm(forms.Form):
    name = forms.CharField(max_length=36)
    up_file = forms.FileField()
