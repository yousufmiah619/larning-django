from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

from . import views  # local import, no circular issue

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path('employee/',include("employees.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)