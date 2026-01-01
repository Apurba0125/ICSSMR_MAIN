from django import forms

class BulkMailForm(forms.Form):
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':5}))
    number_of_users = forms.IntegerField(min_value=1, max_value=20, initial=1, widget=forms.NumberInput(attrs={'class':'form-control'}))
