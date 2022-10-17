from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Guess, Puzzle
from .forms import GuessForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def puzzles_index(request):
  puzzles = Puzzle.objects.filter(user=request.user)
  return render(request, 'puzzles/index.html', { 'puzzles': puzzles })

@login_required
def puzzles_detail(request, puzzle_id):
  puzzle = Puzzle.objects.get(id=puzzle_id)
  guess_form = GuessForm()
  return render(request, 'puzzles/detail.html', { 'puzzle': puzzle, 'guess_form': guess_form })

@login_required
def add_guess(request, puzzle_id):
  form = GuessForm(request.POST)
  if form.is_valid():
    new_guess = form.save(commit=False)
    new_guess.puzzle_id = puzzle_id
    new_guess.save()
  return redirect('puzzles_detail', puzzle_id=puzzle_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # Create User form object w/data from browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # add user to database
      user = form.save()
      # log a user in w/code
      login(request, user)
      return redirect('puzzles_index')
    else:
      error_message = 'Invalid Username or Password - Please Try Again'
  # A bad POST or a GET request
  form = UserCreationForm()
  context = { 'form': form, 'error_message': error_message }
  return render(request, 'registration/signup.html', context)


class PuzzlesCreate(LoginRequiredMixin, CreateView):
  model = Puzzle
  fields = ('hidden_word', 'date')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)