from django.urls import path
from . import views


urlpatterns = [
    path('',views.index_view,name='index'),
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('user_input/',views.user_input_view,name='user_input'),
    path('user_details/',views.user_details_view,name='user_details'),
    
]



