from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('update/<str:pk>/',views.update,name="update"),
    path('delet/<str:pk>/',views.delete,name="delete"),
]