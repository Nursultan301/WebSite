from django.urls import path

from women import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('about/', views.about, name='about'),
]
