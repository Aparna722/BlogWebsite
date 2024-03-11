from django.urls import path
from userapp import views


urlpatterns=[
    #path('index',views.index,name="index"),
    path('',views.post,name="post"),
    
    path('blogview',views.blogview,name="blogview"),
    path('blog_view/', views.blog_view, name='blog_view'), 
    path('blog_view/<int:id>', views.blog_view, name='blog_view'),
    path('blogdetail',views.check,name="blogdetail"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('userregister',views.userregister,name='userregister'),
    path('userblog',views.userblog,name="userblog"),
    path('about',views.about,name="about"),
    path('seeblog/<int:bid>',views.seeblog,name="seeblog"),
    path('user_profile/<int:user_id>/', views.user_profile, name='user_profile'),




]