from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Puzzle(models.Model):
  hidden_word = models.CharField(max_length=6)
  date = models.DateField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.hidden_word

  def get_absolute_url(self):
    return reverse('puzzles_index')

class Guess(models.Model):
  word = models.CharField(max_length=6)
  puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)

  def __str__(self):
    return self.word