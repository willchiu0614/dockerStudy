import json
from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.urls import reverse
from django.http import Http404
from django.template import loader 
from .models import Hospital,Department
def index(req):
    return HttpResponse('medical index')

def hospital_detail(req):
    info_list = Hospital.objects.all()
    context = {'hospital_list':info_list}
    # return render(req,'medical/hospital.html',context)
    template = loader.get_template('medical/hospital.html')
    return HttpResponse(template.render(context,req))

def department(req,hospital_id):
    fk = get_object_or_404(Hospital, pk=hospital_id)
    # try:
    #     fk = Hospital.objects.get(pk=hospital_id)
    # except Hospital.DoesNotExist:
    #     raise Http404("Hospital does not exist")
    department_list = list(Department.objects.filter(hospital=fk))
    context = {'department_list':department_list,'hospital_id':hospital_id,'hospital_name':fk.name}
    return render(req,'medical/detail.html',context)

def hospital_create(req):
    print(req)
    if req.method == "POST":
        name_value = req.POST.get("hospital_name")
        address_value = req.POST.get("address_name")
        established_date = req.POST.get("established_date")
        capacity_value = req.POST.get("capacity_name")
        Hospital.objects.create(name=name_value, address=address_value, established_date=established_date, capacity=capacity_value)
        
        param = name_value
        url1 = reverse('department_create_name',args={param})
        return redirect(url1)
    else:    
        return render(req,"medical/hospital_create.html")
def hospital_edit(req,hospital_id=-1,status=-1):
    print(req)
    if req.method == "POST":
        id_value=req.POST.get("hospital_id")
        # name_value = req.POST.get("hospital_name")
        hospital_instance = Hospital.objects.get(id=id_value)
        hospital_instance.address = req.POST.get("address_name")
        hospital_instance.established_date = req.POST.get("established_date")
        hospital_instance.capacity = req.POST.get("capacity_name")
        hospital_instance.save()
        department_list = list(Department.objects.filter(hospital=hospital_instance)) 
        for department in department_list:
            department.name = req.POST.get(f'department_name_{department.id}')
            department.floor = req.POST.get(f'floor_name_{department.id}')
            department.save()
        return hospital_detail(req)
    else:   
        hospital_instance = Hospital.objects.get(id=hospital_id) 
        department_list = list(Department.objects.filter(hospital=hospital_instance)) 
        context = {'department_list':department_list,'hospital':hospital_instance,'date':str(hospital_instance.established_date.date())}
        
        return render(req,'medical/hospital_edit.html',context)
    
def hospital_delete(req,hospital_id): 
    try:
        hospital_instance = Hospital.objects.get(id=hospital_id)  
    except Hospital.DoesNotExist:
        raise Http404("Hospital : "+str(hospital_id)+" does not exist")
    else:
        hospital_instance.delete()
        return hospital_detail(req)

def department_create(req,param=1,status=-1):
    print("department_create")
    if req.method == "POST":
        name_value = req.POST.get("department_name")
        floor_value = req.POST.get("floor_name")
        hospital_value = req.POST.get("hospital_name")
        print("~~~~~~~",hospital_value)
        hospital_instance = Hospital.objects.get(name=hospital_value)
        department_instance = Department.objects.create(hospital=hospital_instance, name=name_value, floor=floor_value)
        department_list = list(Department.objects.filter(hospital=hospital_instance))
        context = {'department_list':department_list,'hospital_id':hospital_instance.id, 'hospital_context':hospital_value}
        # return redirect('hospital')
        return render(req,"medical/department_create.html",context)
    elif status == 2:
        hospital_instance = Hospital.objects.get(name=param)
        department_list = list(Department.objects.filter(hospital=hospital_instance))

        context = {'department_list':department_list, 'hospital_context':param, 'hospital_id':hospital_instance.id}

        return render(req,"medical/department_create.html",context)
    else:    
        context = {'hospital_context':param}
        return render(req,"medical/department_create.html",context)
        
def department_delete(req,department_id,status=1): 
    try:
        department_instance = Department.objects.get(id=department_id)  
    except Department.DoesNotExist:
        raise Http404("Department : "+str(department_id)+" does not exist")
    else:
        hospital_name = department_instance.hospital
        department_instance.delete()
        try:
            hospital_instance = Hospital.objects.get(name=hospital_name)
        except Hospital.DoesNotExist:
            raise Http404("Hospital : "+str(hospital_name)+" does not exist")
        else:
            if status == 1:  #detail過程刪除
                return department(req,hospital_instance.id)
            else: #創建過程刪除
                print("??-------------",hospital_name)
                param=hospital_name
                status=2
                url1 = reverse('department_create_name',args=(param,status))
                return redirect(url1)

