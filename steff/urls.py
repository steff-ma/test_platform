from django.conf.urls import url
from django.urls import path
from steff import views

urlpatterns = [
    path('', views.test_data, name='test_data'),
]
