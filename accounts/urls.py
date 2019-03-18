from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path(r'comments/', views.add_comment, name='comment'),
]