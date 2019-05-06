from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<int:pk>/', views.AccountView.as_view(), name='user_account'),
    path(r'comments/', views.CommentsView.as_view(), name='user_comments'),
    # path(r'login/', views.CommentsView.as_view(), name='login'),
    # path(r'logout/', views.CommentsView.as_view(), name='logout')
]