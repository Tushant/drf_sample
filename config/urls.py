from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # for versioning
    path('api/v1/', include('notes.urls')),
]
