from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
  
  
admin.site.register(Employee, EmployeeAdmin)
