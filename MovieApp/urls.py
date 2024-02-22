from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexx,name='indexx'),
    path('engList/',views.engList,name='engList'),
    path('marList/',views.marList,name='marList'),
    path('hinList/',views.hinList,name='hinList'),
    path('souList/',views.souList,name='souList'),
    path('about/',views.about,name='about'),
    path('details/<int:pid>',views.Mdetails,name='details'),
    path('booknow/<int:pid>',views.booknow,name='booknow'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('payment_form/',views.payment_form,name='payment_form'),
    path('payment_gateway/', views.payment_gateway, name='payment_gateway'),
]