from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, empty_value="enter your name")
    roll = forms.IntegerField()
