from django import forms
from .models import Join

#
# class EmailForm(forms.Form):
#     name = forms.CharField(required=False)
#     email = forms.EmailField()


class JoinForm(forms.ModelForm):
    # name = forms.CharField(required=False)
    email = forms.EmailField()

    class Meta:
        model = Join
        fields = ['email']
