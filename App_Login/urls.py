from django.urls import path
from App_Login import views

app_name = "App_Login"

urlpatterns = [
    path("signup/", views.sign_up ,name="signup"),
    path("login/", views.login_page ,name="login"),
    path("logout/", views.logout_page ,name="logout"),
    path("profile/", views.profile_page ,name="profile"),
    path("profileChange/", views.profile_change ,name="profileChange"),
    path("password/", views.password_change ,name="passwordChange"),
]