from django.urls import path
from accounts.views import register,login_view,logout_view

urlpatterns = [
    path('signup/',register,name="signup"),
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout")
]