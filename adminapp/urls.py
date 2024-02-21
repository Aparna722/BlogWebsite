from django.urls import path
from adminapp import views

urlpatterns=[
    path('index1',views.index1,name="index1"),
    path('indexad',views.indexad,name="indexad"),
    path('blogdetailad',views.checkad,name="blogdetailad"),

]