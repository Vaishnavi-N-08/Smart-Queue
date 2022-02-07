from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgot/', views.forgot, name='forgot'),
    path('reset/<str:hash>', views.reset, name='reset'),
    path('locations/', views.locations, name='locations'),
    path('branch/<str:hash>', views.branch, name='branch'),
    path('voter/<str:hash>', views.voter, name='voter'),
    path('que/<str:hash>', views.que, name='que'),
    path('host/', views.host, name='host'),
]