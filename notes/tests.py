from rest_framework.test import APITestCase
from rest_framework import status

from notes.api.serilaizers import NoteSerializer
from notes.models import Note

class NotesAPITestCase(APITestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Learning Django", description="Django is awesome", is_published=True)
        self.endpoint = f'http://localhost:8000/api/v1/notes/{self.note.pk}/'

    def test_get_method(self):
        endpoint = 'http://localhost:8000/api/v1/notes/'
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_detail_method_success(self):
        response = self.client.get(self.endpoint)
        note = Note.objects.get(pk=self.note.pk)
        serializer = NoteSerializer(note)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_method_success(self):
        endpoint = 'http://localhost:8000/api/v1/notes/'
        payload = {
            'title': "Title of note",
            'description': "Description for that note"
        }
        response = self.client.post(endpoint, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_method_fail(self):
        endpoint = 'http://localhost:8000/api/v1/notes/'
        payload = {
            'description': "Description for that note"
        }
        response = self.client.post(endpoint, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
  
    def test_put_method_success(self):
        payload = {
            'title': 'Learning Django',
            'description': "Updated description for that note"
        }
        response = self.client.put(self.endpoint, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_method_success(self):
        response = self.client.delete(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

