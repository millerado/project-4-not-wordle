from django.forms import ModelForm
from .models import Guess

class GuessForm(ModelForm):
  class Meta:
    model = Guess
    fields = ('word')