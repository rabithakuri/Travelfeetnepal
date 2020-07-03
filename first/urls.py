from django.urls import path
from first import views

app_name = 'first'

urlpatterns = [
    path('itenary/',views.itenary,name='itenary'),
    path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
]
