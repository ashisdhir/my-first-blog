from django.urls import path

from . import views

app_name = 'emp_details'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:reporter_id>/', views.detail, name='detail'),
]