from django.urls import path
from User import views
urlpatterns=[
    path('',views.index),
    path('Users',views.userlogin),
    path('register',views.register),
    path('RegAction',views.RegAction),
    path('LogAction',views.LogAction),
    path('userhome',views.userhome),
    path('Profile',views.Profile),
    path('SearchByTitle',views.SearchByTitle),
    path('SearchTitleAction',views.SearchTitleAction),
    path('SearchByAuthor',views.SearchByAuthor),
    path('SearchAuthorAction',views.SearchAuthorAction),
    path('SearchByYear',views.SearchByYear),
    path('SearchYearAction',views.SearchYearAction),
      
	]
