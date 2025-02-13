from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Role, Department
from .forms import EmployeeForm

from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm


from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    employees = User.objects.exclude(is_superuser=True)
    is_admin = request.user.is_superuser
    is_hr_manager = False
    if request.user.role:
        is_hr_manager = request.user.role.name == "HR Manager"
    
    return render(request, 'dashboard.html', {
        'employees': employees,
        'is_admin': is_admin,
        'is_hr_manager': is_hr_manager,
    })


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def update_employee(request, employee_id):
    employee = get_object_or_404(User, employee_id=employee_id) 
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)  
        if form.is_valid():
            form.save()  
            return redirect('dashboard')  
    else:
        form = EmployeeForm(instance=employee) 

    return render(request, 'update_employee.html', {'form': form, 'employee': employee})


def delete_employee(request, employee_id):
    employee = get_object_or_404(User, employee_id=employee_id)
    employee.delete()
    return redirect('dashboard')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
