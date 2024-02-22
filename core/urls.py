from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("",views.home,name='frontpage'),
    path("signup/",views.signup,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('login/',views.login_user,name='login'),
    # path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    # path('login/',auth_views.LoginView.as_view(template_name='core/login.html'),name='login')
]