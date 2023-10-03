from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('hospital/',views.hospital_detail, name='hospital'),
    
    path('hospital/<int:hospital_id>/',views.department, name='department_name'),

    path('hospital/form',views.hospital_create, name='hospital_form_name'),
    path('hospital/form/hospital/create',views.hospital_create, name='hospital_create_name'),
    path('hospital/form/hospital/delete/<int:hospital_id>',views.hospital_delete, name='hospital_delete_name'),
    path('hospital/form/hospital/edit',views.hospital_edit, name='hospital_edit_name'),
    path('hospital/form/hospital/edit/<int:hospital_id>/<int:status>',views.hospital_edit, name='hospital_edit_name'),
    path('hospital/form/department/create/',views.department_create, name='department_create_name'),
    path('hospital/form/department/create/<str:param>',views.department_create, name='department_create_name'),
    path('hospital/form/department/create/<str:param>/<int:status>/',views.department_create, name='department_create_name'),
    path('hospital/form/department/delete/<int:department_id>/<int:status>/',views.department_delete, name='department_delete_name'),
    
]