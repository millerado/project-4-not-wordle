from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Puzzle

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def puzzles_index(request):
  puzzles = Puzzle.objects.all()
  return render(request, 'puzzles/index.html', { 'puzzles': puzzles })

class PuzzlesCreate(CreateView):
  model = Puzzle
  fields = ('hidden_word', 'date')