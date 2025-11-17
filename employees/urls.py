from django.urls import path
from .views import *

urlpatterns = [
    path("<int:pk>/",employee_detail,name="employee_detail")
]
 