from django.urls import path
from . import views

app_name = "searchapp"
urlpatterns = [
    path("", views.home, name="home"),
    path("searchlaptops", views.searchlaptops, name="searchlaptops"),
    path("searchphones", views.searchphones, name="searchphones"),
    path("history",views.history,name="history"),
    path("signup",views.signup,name="signup"),
    path("login",views.login_view,name="login"),
    path("logout",views.logout_view,name="logout"),
    path("mycart",views.mycart,name="mycart"),
    path("aboutus", views.aboutus, name="aboutus")
]