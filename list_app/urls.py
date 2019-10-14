from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="home"),
  path('add_list', views.add_list),
  path('delete_list/<int:list_id>/', views.delete_list),
  path('lists/<int:list_id>/', views.list_page),
]