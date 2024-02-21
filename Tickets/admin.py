from django.contrib import admin

# Register your models here.
from .models import State,UserMaster,TaskMaster

@admin.register(State)
class StateModel(admin.ModelAdmin):
    list_display = ['id','state_name','state_code','created_date','updated_date','is_active']
    search_fields=('state_name','state_code')
    list_filter=('is_active',)


@admin.register(UserMaster)
class UserMasterAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password','phone','city','gender','joining_date','state','created_date','updated_date','is_active']
    search_fields=('name','city')
    list_filter=('is_active','state')

@admin.register(TaskMaster)
class TaskMaster(admin.ModelAdmin):
    list_display = ['id','task_id','title','description','assign_date','state','created_date','updated_date','user_id','is_active']
    search_fields = ('title','user_id__name')
    list_filter = ('is_active', 'state')

# class CustomAdminSite(admin.AdminSite):
    #here we are changing admin panels heading name
#     site_header = 'Project Task Assigner'
#     site_title = 'Welcome Taufique'

# admin_site = CustomAdminSite(name='customadmin')