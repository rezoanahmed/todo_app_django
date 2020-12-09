from django.urls import path
from mytodos import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('del/', views.delete, name = 'delete'),
]
