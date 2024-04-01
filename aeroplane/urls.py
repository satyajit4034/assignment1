from django.urls import path
from aeroplane.views import *
app_name='something'

urlpatterns = [
    path('airindia/',airindia,name='airindia.html')
]