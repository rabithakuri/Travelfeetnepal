from django.urls import path
from first import views

app_name = 'first'

urlpatterns = [
            path('contact/',views.contact,name='contact'),
            path('itenary/',views.itenary,name='itenary'),
            path('gallery/',views.gallery,name='gallery'),
            path('faq/',views.faq,name='faq'),
            path('about/',views.about,name='about'),
            path('annapurna/',views.annapurna,name='annapurna'),
            path('langtang/',views.langtang,name='langtang'),
            path('annapurnacircuit/',views.annapurnacircuit,name='annapurnacircuit'),
            path('poonhill/',views.poonhill,name='poonhill'),
            path('mardihimal/',views.mardihimal,name='mardihimal'),
            path('everestthreepasses/',views.everestthreepasses,name='everestthreepasses'),
]
