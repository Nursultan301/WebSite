from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('women.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Известные женщина мира"
