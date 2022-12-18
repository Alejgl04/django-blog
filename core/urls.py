
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import HomeView, About, Contact

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', HomeView.as_view(), name='home'),  
  path('about/', About.as_view(), name='about'),  
  path('contact/', Contact.as_view(), name='contact'),  
 
  path('newsletter/', include('newsletters.urls', namespace="newsletter")),
  path('dashboard/', include('dashboard.urls', namespace="dashboard")),
  
  
]

if settings.DEBUG:
   urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
   urlpatterns += static( settings.STATIC_URL, document_root = settings.STATIC_ROOT)