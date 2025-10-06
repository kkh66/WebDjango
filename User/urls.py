from django.urls import path, include
from . import views

app_name = 'User'
urlpatterns = [
    # Basic function
    path('', include([
        path('', views.login, name='login'),
        path('register/', views.register, name='register'),
        path('logout/', views.logout_user, name='logout'),
        path('profile/', views.profile, name='profile'),
        path('delete/',views.delete_profile, name='delete'),
    ]))
]
