from django.urls import path
from first import views

app_name = 'first'

urlpatterns = [
            path('contact/',views.contact,name='contact'),
            path('itenary/',views.itenary,name='itenary'),
            path('gallery/',views.gallery,name='gallery'),
]
