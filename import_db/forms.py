from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name', 'document', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'document': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
