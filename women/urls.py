from django.urls import path

from women import views

urlpatterns = [
    path('', views.index, name='home'),
    path('detail/<slug:slug>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('category/<slug:cat_slug>/', views.category, name='category')

]
