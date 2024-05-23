from django import forms

from funko_api.models import Funko


class FunkoForm(forms.ModelForm):

    class Meta:
        model = Funko
        fields = [
            'name',
            'number',
            'collection',
            'is_backlight',
        ]