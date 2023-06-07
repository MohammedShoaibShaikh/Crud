from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.

def Index(request):
    emp = Employee.objects.all()
    context = {
        'emp' : emp
    }
        
    return render(request, 'index.html', context)

def Add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        location = request.POST.get('location')
        phone = request.POST.get('phone')

        emp = Employee (
            name = name,
            email = email,
            location = location,
            phone = phone
        )
        emp.save()
        return redirect('home')
    return render(request, 'index.html')

def Edit(request):
    emp = Employee.objects.all()
    context = {
        'emp' : emp
    }
    return render(request, 'index.html', context)

def Update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        location = request.POST.get('location')
        phone = request.POST.get('phone')

        emp = Employee(
            id = id,
            name = name,
            email = email,
            location = location,
            phone = phone
        )
        emp.save()
        return redirect('home')
    return render(request, 'index.html')

def Delete(request, id):
    
    try:
        emp = Employee.objects.get(id = id)
        emp.delete()
        
        return JsonResponse({'status':'success'})
    except Employee.DoesNotExist:
        return JsonResponse({'status':'error'})
    # emp = Employee.objects.filter(id = id)
    # emp.delete()
    # context = {
    #     'emp' : emp,
    # }
    # return redirect('home')
    
def Search(request):
    return render(request, 'index.html') 

def employee_ajax(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        location = request.POST.get('location')
        phone = request.POST.get('phone')

        emp = Employee(name=name, email=email, location=location, phone=phone) 
        emp.save()
        # updated data
        upd_data = Employee.objects.values()
        # print(upd_data)
        emp_data = list(upd_data)
        data = {'status': 'success', 'emp_data': emp_data}
        return JsonResponse(data)
    else:
        data = {'status': 'error', 'message': 'Invalid AJAX request'}
        return JsonResponse(data)