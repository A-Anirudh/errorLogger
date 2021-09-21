from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('profile/<str:username>', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('captcha/', include('captcha.urls')),


]