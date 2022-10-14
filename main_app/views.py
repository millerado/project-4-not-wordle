from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Guess, Puzzle
from .forms import GuessForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def puzzles_index(request):
  puzzles = Puzzle.objects.all()
  return render(request, 'puzzles/index.html', { 'puzzles': puzzles })

def puzzles_detail(request, puzzle_id):
  puzzle = Puzzle.objects.get(id=puzzle_id)
  guess_form = GuessForm()
  return render(request, 'puzzles/detail.html', { 'puzzle': puzzle, 'guess_form': guess_form })

def add_guess(request, puzzle_id):
  form = GuessForm(request.POST)
  if form.is_valid():
    new_guess = form.save(commit=False)
    new_guess.puzzle_id = puzzle_id
    new_guess.save()
  return redirect('puzzles_detail', puzzle_id=puzzle_id)

class PuzzlesCreate(CreateView):
  model = Puzzle
  fields = ('hidden_word', 'date')