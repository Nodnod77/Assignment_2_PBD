from django.forms import ModelForm
from main.models import FormEntry
from django.utils.html import strip_tags

class FormEntryForm(ModelForm):
    class Meta:
        model = FormEntry
        fields = ["data1", "data2", "data3"]

    def clean_form(self):
        form = self.cleaned_data["form"]
        return strip_tags(form)

    def clean_feelings(self):
        feelings = self.cleaned_data["feelings"]
        return strip_tags(feelings)