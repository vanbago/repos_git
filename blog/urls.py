from django.urls import path
from .import views

# le chemin qui va trouvé les url de l'application défini dans url du projet
 
urlpatterns = [
     path('home', views.home, name='home'),
     path('read/<id>/<slug>', views.read, name='read'),
     path('new_contact', views.nouveau_contact, name='new_contact'),
     path('contacts', views.contact, name='contacts'),
     path('voir_contact', views.voir_contact, name='voir_contact'),
     path('signup/', views.signup, name="signup")
    ]

