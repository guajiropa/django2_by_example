"""
AUTHOR      :   Robert James Patterson
DATE        :   11/26/18
SYNOPSIS    :   Work thru files for 'Dajngo 2 by Example' by Packt Publishing
"""
from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

    def __str__(self):
        return 'This is an \'EmailPostForm\' object.'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        