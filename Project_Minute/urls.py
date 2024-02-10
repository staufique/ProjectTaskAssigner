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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parser/',views.parser),
    path('users/',views.userMasterView),
    path('users-bulk-data/',views.UserMasterBulkDataView),
    path('',views.task),
    path('view-tasks/',views.ManipulateTasks,name='view-tasks'),
    # Add this line to your urlpatterns
    path('delete-tasks/<int:id>/', views.DeleteTask, name='delete-tasks'),
    path('update-task/<int:id>/', views.update, name='update-task'),

]
