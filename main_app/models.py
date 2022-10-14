from django.db import models

# Create your models here.

class Puzzle(models.Model):
  hidden_word = models.CharField(max_length=6)
  date = models.DateField()

class Guess(models.Model):
  word = models.CharField(max_length=6)
  puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)