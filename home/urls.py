from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('about/', about, name='about'),
    path('academics/', academics, name='academics'),
    path('gallery/', gallery, name='gallery'),
    path('news/', news, name='news'),
    path('partnerships/', partnerships, name='partnerships'),
    path('contact/', contact, name='contact'),
    path('apply/', apply, name='apply'),
]