from django.urls import path
from soldier import views
from soldier.views import view_list, save_soldier_details
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('user_page/', views.user_page, name='user_page'),
    path('soldier_list/', views.soldier_list, name='soldier_list'),
    path('soldier_detail/', views.soldier_detail, name='soldier_detail'),
    path('view-list/', view_list, name='view_list'),
    path('login/', views.login_view, name='login'),
    path('soldier_detail/', views.soldier_detail, name='soldier_detail'),
    path('save_soldier_details/', views.save_soldier_details, name='save_soldier_details'),

]
