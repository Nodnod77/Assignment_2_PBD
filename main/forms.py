from django.forms import ModelForm
from main.models import FormEntry

class FormEntryForm(ModelForm):
    class Meta:
        model = FormEntry
        fields = ["data1", "data2", "data3"]