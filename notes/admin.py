from django.contrib import admin

from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', )

admin.site.register(Note, NoteAdmin)