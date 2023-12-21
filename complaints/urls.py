from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('complain',views.complain,name='complain'),
    path('record/', views.record_audio, name='record_audio'),

]