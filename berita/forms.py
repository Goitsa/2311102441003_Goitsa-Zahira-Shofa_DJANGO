from django import forms
from berita.models import Artikel

class Artikelform(forms.ModelForm):

    class Meta:
        model = Artikel
        fields = ( 'judul', 'isi', 'kategori',  'author', 'thumbnail')
        widgets = {
            "judul" : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                }),
            "isi" : forms.Textarea(
                attrs = {
                    'class': 'form-control',
                }),
            "kategori" : forms.Select(
                attrs = {
                    'class': 'form-control',
                }),
            "author": forms.Select(
                attrs={
                    'class': 'form-control',
                }),
        }