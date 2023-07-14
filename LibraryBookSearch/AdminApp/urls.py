from django.urls import path
from AdminApp import views
urlpatterns=[
    path('adminlogin',views.adminlogin),
    path('LogAction',views.LogAction),
    path('adminhome',views.adminhome),
    path('AddBooks',views.AddBooks),
    path('AddBookAction',views.AddBookAction),
    path('ViewBooks',views.ViewBooks),
    ]
