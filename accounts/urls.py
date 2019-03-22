from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<int:pk>/', views.AccountView.as_view(template_name='accounts/account.html'), name='user_account'),
    path(r'comments/', views.CommentsView.as_view(), name='user_comments'),
]