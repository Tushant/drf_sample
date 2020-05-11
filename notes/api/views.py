from rest_framework import generics

from notes.models import Note
from .serilaizers import NoteSerializer

class ListNotes(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class DetailNote(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
