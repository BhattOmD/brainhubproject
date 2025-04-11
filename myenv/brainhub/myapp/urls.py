"""
URL configuration for brainhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.homepage,name='home'),
    #path('about/',views.aboutpage,name='about'),
    
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('newlearner/',views.newlearner,name='newlearner'),
    path('profile/',views.profile,name='profile'),
    path('all-learners/',views.all_learners,name='all-learners'),
    path('learner_profile/',views.learner_profile,name='learner_profile'),
    path('add_category/',views.add_category,name='add_category'),
    path('all_category/',views.all_category,name='all_category'),
    path('edit_category/<int:pk>',views.edit_category,name='edit_category'),
    path('update_category/',views.update_category,name='update_category'),
    path('del_category/<int:pk>',views.del_category,name='del_category'),
    path('add_course/',views.add_course,name='add_course'),
    path('add_company/',views.add_company,name='add_company'),
    path('all_course_list/',views.all_course_list,name='all_course_list'),
    path('all_company_list/',views.all_company_list,name='all_company_list'),
    path('view_company/',views.view_company,name='view_company'),
    path('edit_course/<int:pk>',views.edit_course,name='edit_course'),
    path('update_course/',views.update_course,name='update_course'),
    path('del_course/<int:pk>',views.del_course,name='del_course'),
    
    path('edit_company/<int:pk>',views.edit_company,name='edit_company'),
    path('update_company/',views.update_company,name='update_company'),
    path('del_company/<int:pk>',views.del_company,name='del_company'),
    path('view_course/',views.view_course,name='view_course'),
    path('course_enroll/<int:pk>',views.course_enroll,name='course_enroll'),
    path('add_enroll_course/<int:pk>',views.add_enroll_course,name='add_enroll_course'),
    path('all_request/',views.all_request,name='all_request'),
    
    
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('reset_password/',views.reset_password,name='reset_password'),
    
    path('accept_request/<int:pk>',views.accept_request,name='accept_request'),
    path('reject_request/<int:pk>',views.reject_request,name='reject_request'),

    ]
#http: //127.0.0.1:8000/myapp/home/
    

#http: //127.0.0.1:8000/myapp/home/
#http: //127.0.0.1:8000/myapp/about/
#http: //127.0.0.1:8000 ---actual url