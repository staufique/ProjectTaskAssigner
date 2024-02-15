"""
URL configuration for Project_Minute project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Tickets import views
# from Tickets.views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name='home-page'),
    # path('<str:unwanted>/', views.handler404,name='home-page'),
    # path('parser/',views.parser),
    # path('users/',views.userMasterView),
    # path('users-bulk-data/',views.UserMasterBulkDataView),
    path('assign-tasks/',views.AssignTasks,name='assign-tasks'),
    path('view-tasks/',views.ViewTasks,name='view-tasks'),
    path('delete-tasks/<int:id>/', views.DeleteTask, name='delete-tasks'),
    path('update-task/<int:id>/', views.update, name='update-task'),
    path('about/', views.aboutpage, name='about-page'),
    path('adduser/', views.adduser, name='add-user'),
    path('add-multiple-users/', views.addmultipleusers, name='add-multiple-users'),
    path('add-state/', views.addState, name='add-state'),
    path('add-multiple-states/', views.addMultipleState, name='add-multiple-states'),

    # page not found
    # path('<str:first>/', views.handler404,name='not-found'),
]


