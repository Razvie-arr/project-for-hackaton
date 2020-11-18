from django.urls import path
from . import views
urlpatterns = [
    path('', views.site_view, name='site_view'),
]