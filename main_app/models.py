from django.db import models
from django.urls import reverse

# Create your models here.

class Puzzle(models.Model):
  hidden_word = models.CharField(max_length=6)
  date = models.DateField()

  def get_absolute_url(self):
    return reverse('puzzles_index')

class Guess(models.Model):
  word = models.CharField(max_length=6)
  puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)