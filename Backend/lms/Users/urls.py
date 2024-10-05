from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('api/users/', include('users.urls')),  # User-related routes
    path('api/courses/', include('courses.urls')),  # Course-related routes
]
