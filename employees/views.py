from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from employees.models import Employee
# Create your views here.
def employee_detail(request ,pk ):
    employee =  get_object_or_404(Employee, pk=pk)
    contaxt={
        "employee":employee
    }   
    return render(request,"employee_detail.html",contaxt)