from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('puzzles/', views.puzzles_index, name='puzzles_index'),
  path('puzzles/create', views.PuzzlesCreate.as_view(), name='puzzles_create'),
]
