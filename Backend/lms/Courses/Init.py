from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('api/users/', include('users.urls')),  # User-related endpoints
    path('api/courses/', include('courses.urls')),  # Course-related endpoints
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Optional: API Documentation (like Swagger)
# from rest_framework.documentation import include_docs_urls
# urlpatterns += [
#     path('docs/', include_docs_urls(title='LMS API Documentation')),
# ]
