from django.forms import ModelForm
from .models import ExcelFiles


class ExcelForm(ModelForm):
    class Meta:
        model = ExcelFiles
        fields = ('file',)
