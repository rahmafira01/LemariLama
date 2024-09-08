from django.urls import path
from .views import show_main
from django.urls import path, include

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

urlpatterns = [
    path('', include('main.urls')),
]