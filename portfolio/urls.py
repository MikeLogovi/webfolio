from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .controllers import home_controller
from django.http import HttpResponse

from . import views
urlpatterns = [
    path('',home_controller.home,name="home"),
    path('admin/', admin.site.urls),
    path('websites/',include('websites.urls')),
    path('developpers/',include('developpers.urls')),
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

