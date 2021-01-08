
from django.urls import path
from . import views

app_name = 'my_blog'

urlpatterns = [

    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),




]
