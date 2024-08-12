from django.urls import path
from .views import log,Home_Page,Subject_Page,Marks_Page,changepassword,myth,Staff,list,student_delete_list,student_list,subject_list,add_subject,delete_subject,update_subject,StaffView,StudentView,del_list,StaffHome,student_marks_list,student_marks_add,student_marks_modify,student_marks_delete




urlpatterns=[
    path('login',log.as_view()),
    path('new',changepassword.as_view()),
    path('',Home_Page.as_view(), name='Home'),
    path('student',myth.as_view(),name='student'),
    path('staff',Staff.as_view(),name='Staff'),
    path('<int:pk>/edit/',update_subject, name='modify_subject'),
    path('List',list,name='List'),
    path('list',subject_list,name='subject_list'),
    path('delete',delete_subject,name='Delete'),
    path('add',add_subject, name='add_subject'),
    path('<int:pk>/delete/', delete_subject, name='delete_subject'),
    path('StaffView',StaffView.as_view()),
    path('marks',StudentView.as_view(),name='marks'),
    path('del_list',del_list,name='delete_list'),
    path('Staff_Home',StaffHome.as_view(), name='Staff_Home'),
    path('marks_list',student_marks_list, name='student_marks_list'),
    path('add/',student_marks_add, name='student_marks_add'),
    path('modify/<int:pk>/',student_marks_modify, name='student_marks_modify'),
    path('delete/<int:pk>/',student_marks_delete, name='student_marks_delete'),
    path('Subject_Page',Subject_Page.as_view(),name='Subject_Page'),
    path('Marks_Page',Marks_Page.as_view(),name='Marks_Page'),    
    path('Student_List',student_list,name='Student_List'),
    path('Student_delete_List',student_delete_list,name='Student_delete_List'),
    
 ]











