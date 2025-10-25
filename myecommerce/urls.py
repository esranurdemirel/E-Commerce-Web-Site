from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static #for media and static files

urlpatterns = [
    path('admin/', admin.site.urls), #for access to admin panel
    path('',include('eshop.urls')),
]

if settings.DEBUG:
  #for showing the css/js files and images properly on development process
  urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
  #to run static files(like css and javascript) on developing mode
  urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)