from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Heart'

urlpatterns = [
    url(r'^check/$', views.Check, name="check"),
    url(r'^predict/$', views.predictHeart, name="predictHeart"),
]