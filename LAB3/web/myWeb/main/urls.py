from django.urls import path
from . import views
urlpatterns = [
    path('', views.main_page, name="home"),
    path('faq', views.faq, name="faq"),
    path('signin', views.sign_in, name="signin"),
    path('signup', views.sign_up, name="signup"),
    path('ad/<int:pk>/', views.ad_detail, name='ad_detail'),
    path('ad/new', views.add_new, name='add_new'),
    path('ad/<int:pk>/edit', views.ad_edit, name='ad_edit'),
    path('ad/<int:pk>/del', views.ad_delete, name='ad_del'),
    path('ad/<int:pk>/user', views.us_profile, name='user_profile'),
    path('logout/', views.do_logout, name='logout'),

]
