from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('puzzles/', views.puzzles_index, name='puzzles_index'),
  path('puzzles/<int:puzzle_id>/', views.puzzles_detail, name='puzzles_detail'),
  path('puzzles/create', views.PuzzlesCreate.as_view(), name='puzzles_create'),
  path('puzzles/create_auto', views.create_auto, name='create_auto'),
  path('puzzles/<int:puzzle_id>/update'),
  path('puzzles/<int:puzzle_id>/delete'),
  path('puzzles/<int:puzzle_id>/add_guess/', views.add_guess, name='add_guess'),
  path('accounts/signup/', views.signup, name='signup'),
]
