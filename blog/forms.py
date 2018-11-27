"""
AUTHOR      :   Robert James Patterson
DATE        :   11/26/18
SYNOPSIS    :   Work thru files for 'Dajngo 2 by Example' by Packt Publishing
"""
from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_lenght=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(require=False, widget=forms.Textarea)
