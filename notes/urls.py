from django.urls import path

from .api.views import ListNotes, DetailNote

urlpatterns = [
    path('notes/', ListNotes.as_view()),
    path('notes/<int:pk>/', DetailNote.as_view()),
]