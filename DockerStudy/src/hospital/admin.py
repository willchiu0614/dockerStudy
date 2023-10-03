from django.contrib import admin
from .models import Hospital, Department

class HospitalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hospital._meta.fields]

class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.fields]

admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Department,DepartmentAdmin)
