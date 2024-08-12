from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404

# Create your views here.
from django.shortcuts import render,redirect
from django.views import View 
from .forms import signin,change_password,haritha,STAFF,SubjectForm,StudentMarksForm
from django.http import HttpResponse
from .models import Subject,Deletesub,StaffDetails,Student_Marks
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

# Create your views here.
# class log(View):
#     def get(self,request):
#         logins=login
#         ctx={
#              'logins':logins
#         }
#         return render(request,'myth.html',ctx)

class myth(View): 
    
    def get(self,request):
        form=haritha()
        ctx={
            'form': form
        }
        return render(request,'student.html',ctx)
    
    def post(self,request):
        form = haritha(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('marks')
        else:
          return render(request,'incorrect.html',{'form':form})


class log(View):
    def get(self,request):
        form=signin()
        ctx={
             'form': form
        }
        return render(request,'login.html',ctx)
    
    def post(self,request):
        form = signin(request.POST)
        if form.is_valid():
            # form.save()
            return render(request,'home.html')
        else:
            return render(request,'incorrect.html',{'form':form})
        
class Home_Page(View):
    
    def get(self,request):
        form = change_password
        ctx={
            'form':form
        }
        return render(request,'home.html',ctx)


class Staff(View):
    
    def get(self,request):
        form=STAFF()
        ctx={
            'form': form
        }
        return render(request,'staff.html',ctx)
    
    def post(self,request):
        form = STAFF(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('Staff_Home')
        else:
            return render(request,'incorrect.html',{'form':form})
    


    
    

class changepassword(View):
    
    def get(self,request):
        form = change_password
        ctx={
            'form':form
        }
        return render(request,'password.html',ctx)

    def post(self,request):
        forms=change_password(request.POST)
        if forms.is_valid():
            return render(request,'changed.html')
        else:
            return render(request,'mismatch.html') 







def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'list.html', {'subjects': subjects})

def del_list(request):
    subjects = Subject.objects.all()
    return render(request, 'delete_list.html', {'subjects': subjects})

def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('List')
    else:
        form = SubjectForm()
    return render(request, 'add_subject.html', {'form': form})


def update_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('List')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'modify.html', {'form': form})



def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('List')
    return render(request, 'delete.html', {'subject': subject})

def list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})





def student_marks_list(request):
    marks = Student_Marks.objects.all()
    return render(request,'student_marks_list.html',{'marks':marks})

def student_marks_add(request):
    if request.method == "POST":
        form = StudentMarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_marks_list')
    else:
        form = StudentMarksForm()
    return render(request,'marks_form.html',{'form':form})

def student_marks_modify(request,pk):
    mark = get_object_or_404(Student_Marks,pk=pk)
    if request.method == "POST":
        form = StudentMarksForm(request.POST,instance=mark)
        if form.is_valid():
            form.save()
            return redirect('student_marks_list')
    else:
        form = StudentMarksForm(instance=mark)
    return render(request, 'marks_form.html',{'form':form})

def student_marks_delete(request,pk):
    mark = get_object_or_404(Student_Marks,pk=pk)
    if request.method =="POST":
        mark.delete()
        return redirect('student_marks_list')
    return render(request,'marks_delete.html',{'mark':mark})


class StaffView(View):
    def get(self,request):
        data = StaffDetails.objects.all().values()
        context = {
        'data': data,
        }
        return render(request,'details.html',context)
    
class StaffHome(View):
    def get(self,request):
        data = StaffDetails.objects.all().values()
        context = {
        'data': data,
        }
        return render(request,'sfhome.html',context)
    


class StudentView(View):
    def get(self,request):
        data = Student_Marks.objects.all().values()
        context ={
            'data':data,
        }    
        return render(request,'students.html',context)


   
        
class Subject_Page(View):
    def get(self,request):
        data = StaffDetails.objects.all().values()
        context = {
        'data': data,
        }
        return render(request,'subject_page.html',context)
    
class Marks_Page(View):
    def get(self,request):
        data = StaffDetails.objects.all().values()
        context = {
        'data': data,
        }
        return render(request,'Marks_Page.html',context)
    

def student_list(request):
    marks = Student_Marks.objects.all()
    return render(request,'modify_list.html',{'marks':marks})  


def student_delete_list(request):
    marks = Student_Marks.objects.all()
    return render(request,'delete_student.html',{'marks':marks})