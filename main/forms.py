from django.forms import ModelForm, Textarea, TextInput, EmailInput
from .models import Letters

class LettersForm(ModelForm):
    class Meta:
        model = Letters
        fields = (
            'name',
            'email',
            'message',
        )
        widgets = {
            "name": TextInput(attrs={
                'class': "textInput",
                'placeholder': "Введите имя",
            }),
            "email": EmailInput(attrs={
                'class': "textInput",
                'placeholder': "Введите email",
            }),
            "message": Textarea(attrs={
                'class': "textInput",
                'placeholder': "Введите ваше сообщение",
            })
        }