from django.contrib import admin
from django.urls import path, include
from .views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('problems/', include('problems.urls')),
    path('todolist/', include('todolist.urls')),
    path('', index),
]
