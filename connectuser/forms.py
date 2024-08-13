from django.forms import ModelForm
from .models import Pdf


class PdfForm(ModelForm):
    class Meta:
        model = Pdf
        fields = ['name', 'pdf']
