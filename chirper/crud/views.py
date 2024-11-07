from django.shortcuts import render, redirect, get_object_or_404
from .forms import student_form, course_form, search_student_form
from .models import student

# Create your views here.

def crud_home(request):
    return render(request,'crud_home.html')

def create_student(request):
    if request.method == "POST":
        form = student_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crud_home')
    else:
        form = student_form()
    return render(request, 'create_student.html', {'form': form})

def create_course(request):
    if request.method == "POST":
        form = course_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_home')
    else:
        form = course_form()
    return render(request,'create_course.html',{'form':form})

def search_student(request):
    if request.method == "POST":
        form = search_student_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_data = student.objects.filter(name=data['name']).values()
            return render(request,'student_list.html',{'my_data': my_data})
    else:
        form = search_student_form()
    return render(request,'search_student.html',{'form':form})

def view_student(request):
    student_data = student.objects.all()
    return render(request,'student_list.html',{'data':student_data})

def edit_student(request,student_id):
    student_data = get_object_or_404(student,pk=student_id)
    if request.method == "POST":
        form = student_form(request.POST,request.FILES,instance=student_data)
        if form.is_valid():
            form.save()
            return redirect('crud_view_student')
    else:
        form = student_form(instance=student_data)
    return render(request,'create_student.html',{'form':form})

def delete_student(request,student_id):
    student_data = get_object_or_404(student,pk=student_id)
    if request.method == "POST":
        student_data.delete()
        return redirect('crud_view_student')
    return render(request,'delete_student.html')