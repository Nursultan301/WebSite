from django.urls import path

from women import views

urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('category/<int:pk>/', views.category, name='category')

]
