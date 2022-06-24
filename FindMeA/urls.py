from django.urls import path
from . import views

app_name = 'FindMeA'

urlpatterns = [
    path('homepage', views.homepage, name = 'homepage'),
    path('signup', views.signup, name='signup'),
    path('', views.load_login_page, name= 'load_login_page'),
    path('login', views.verify_and_login, name='verify'),
    path('createyourprofile', views.createyourprofile, name = "createyourprofile"),
    path('findsomeone', views.findsomeone, name = "findsomeone"),
    path("userprofile", views.userprofile, name="userprofile"),
    path("makeprofile", views.makeprofile, name = "makeprofile"),
    path("possiblementors", views.possiblementors, name = "possiblementors"),
    path("browseusers", views.browseusers, name = "browseusers"),
    path('findfriend', views.findfriend, name = "findfriend"),
    path('mentorme', views.mentorme, name = "mentorme"),
    path("splashpage", views.splashpage, name = "splashpage")
]