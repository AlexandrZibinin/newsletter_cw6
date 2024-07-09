from django.forms import ModelForm

from letter.models import Letter


class LetterForm(ModelForm):
    class Meta:
        model = Letter
        exclude = ("owner",)