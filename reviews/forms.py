from django import forms
from reviews.models import GAME_CHOICE
from ckeditor.fields import RichTextField

class NewReviewForm(forms.Form):
    
    titulo = forms.CharField(label="Titulo", max_length=50, required=True)
    descripcion = forms.CharField(label="Descripcion", max_length=200, required=True, widget=forms.Textarea(attrs={'rows':3, "cols": 60}))
    review = RichTextField()
    juego = forms.ChoiceField(choices=GAME_CHOICE, required=True)
    creador = forms.CharField(label="Creador", max_length=50)

class EditReviewForm(forms.Form):
    
    titulo = forms.CharField(label="Titulo", max_length=50, required=True)
    descripcion = forms.CharField(label="Descripcion", max_length=200, required=True, widget=forms.Textarea(attrs={'rows':3, "cols": 60}))
    review = RichTextField()
    juego = forms.ChoiceField(choices=GAME_CHOICE, required=True)
    creador = forms.CharField(label="Creador", max_length=50) 