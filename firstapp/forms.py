from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя", help_text="Введите свое имя")
    comment = forms.CharField(label="Комментарий", help_text="Введите свой возраст")
    email = forms.EmailField(required=False)