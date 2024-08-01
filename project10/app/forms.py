from django import forms

def validation_for_a(data):
    if data.startswith('a'):
        raise forms.ValidationError('should not start with a')
    

def validation_for_len(data):
    if len(data) <= 5:
        raise forms.ValidationError('Length is lessthan 5')


class SchoolForm(forms.Form):
    sname = forms.CharField(max_length=50, required=False, validators=[validation_for_a, validation_for_len])
    princy = forms.CharField(max_length=25, required=False)
    contact=forms.CharField(max_length=20, required=False)
    loc = forms.CharField(max_length=200, required=False, widget=forms.Textarea(attrs={'cols': 30, 'rows': 10}))
    