from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from cv_requests import views
from cv_requests.views import CVDownloadAPIView, CVRequestAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('download/<uuid:cv_request_id>/', CVDownloadAPIView.as_view(), name='cv_download'),
    path('api/cv/', CVRequestAPIView.as_view(), name='cv_request'),
    path('', views.home, name='home'),

    # Add this line to serve your React application's index.html
    re_path('.*', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
