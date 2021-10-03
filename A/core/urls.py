from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('login/',views.Login.as_view(),name='login'),
    path('logout/',views.Logout.as_view(),name='logout'),
    path('user-panel/',views.UserPanel.as_view(),name='user-panel'),
    path('pictures/',views.Pictures.as_view(),name='pictures'),
    path('doctors/',views.Doctors.as_view(),name='doctors'),
    path('contact-us/',views.ContactUs.as_view(),name='contact-us'),
    path('about-us/',views.AboutUs.as_view(),name='about-us'),
    path('',views.Home.as_view(),name='home')
]