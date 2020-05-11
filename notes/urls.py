from django.urls import path

from .api.views import ListNotes, DetailNote

urlpatterns = [
    path('', ListNotes.as_view()),
    path('<int:pk>/', DetailNote.as_view()),
]