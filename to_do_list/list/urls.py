from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('add_to_do', views.add_to_do, name='add_to_do'),
    path('del_to_do/<int:to_do_item_id>', views.del_to_do, name='del_to_do'),
]
