from django.urls import path
from soldier import views
from soldier.views import view_list, p_bty_view, q_bty_view, r_bty_view, s_bty_view
from . import views
from .views import bty_champ_view, save_bty_champ_view, soldier_btychamp_view, update_scores


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('user_page/', views.user_page, name='user_page'),
    path('soldier_list/', views.soldier_list, name='soldier_list'),
    path('soldier_detail/', views.soldier_detail, name='soldier_detail'),
    path('view-list/', view_list, name='view_list'),
    path('login/', views.login_view, name='login'),
    path('add_soldier/', views.add_soldier, name='add_soldier'),
    path('delete/<int:soldier_id>/', views.delete_soldier, name='delete_soldier'),
    path('edit/<int:soldier_id>/', views.edit_soldier, name='edit_soldier'),
    path('logout/', views.logout_view, name='logout'),
    path('bty_champ/', views.bty_champ_view, name='bty_champ'),
    path('save_bty_champ/', views.save_bty_champ_view, name='save_bty_champ'),
    path('soldier_btychamp/', soldier_btychamp_view, name='soldier_btychamp'),
    path('update_scores/', update_scores, name='update_scores'),
    path('p_bty/', views.p_bty_view, name='p_bty_view'),
    path('q_bty/', views.q_bty_view, name='q_bty_view'),
    path('r_bty/', views.r_bty_view, name='r_bty_view'),
    path('s_bty/', views.s_bty_view, name='s_bty_view'),
]
