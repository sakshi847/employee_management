from django.contrib import admin
from .models import User, Department, Role

class UserAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name', 'username', 'email', 'dept', 'role', 'reporting_manager', 'date_of_joining', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'username', 'mobile')
    list_filter = ('dept', 'role', 'date_of_joining')
    ordering = ('-created_at',)
    filter_horizontal = ('groups', 'user_permissions') 

admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(Role)
