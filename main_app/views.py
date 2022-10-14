from django.shortcuts import render
from .models import Puzzle

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def puzzles_index(request):
  puzzles = Puzzle.objects.all()
  return render(request, 'puzzles/index.html', { 'puzzles': puzzles })