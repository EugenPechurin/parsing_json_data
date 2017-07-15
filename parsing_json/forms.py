from django import forms

from parsing_json.models import DataRowModel


class UploadFileForm(forms.Form):
    file = forms.FileField()


class DataRowForm(forms.ModelForm):
    class Meta:
        model = DataRowModel
        fields = [
            "region",
            "city",
            "value"
        ]
