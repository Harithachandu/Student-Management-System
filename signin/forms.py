from typing import Any
from django import forms
from .models import login,hari,staff,Subject,Student_Marks



class signin(forms.ModelForm):
    class Meta:
        model=login
        fields=('username','password')
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                user = login.objects.get(username=username)
                if user.password != password:
                    raise forms.ValidationError('incorrect username or password')
            except login.DoesNotExist:
                raise forms.ValidationError('incorrect username or password')
            return cleaned_data

        
class change_password(forms.Form):
    New_Password = forms.IntegerField()
    Confirm_Password = forms.IntegerField()


    def clean(self):
        data = self.cleaned_data
        # cleaned_data = super().clean()
        New_Password = data['New_Password']
        Enter_Password = data['Confirm_Password']
        if New_Password != Enter_Password:
            raise forms.ValidationError('Password not matching')
        return data


class haritha(forms.ModelForm):
    class Meta:
        model=hari
        fields=('Student_Name','Register_No')


    def clean(self):
        cleaned_data = super().clean()
        Student_Name = cleaned_data.get('Student_Name')
        Register_No = cleaned_data.get('Register_No')
        
        if Student_Name and Register_No:
            try:
                member = hari.objects.get(Student_Name=Student_Name )
                if member.Register_No != Register_No:
                    raise forms.ValidationError('incorrect name or register no')
            except hari.DoesNotExist:
                raise forms.ValidationError('incorrect name or register no')
            return cleaned_data
        



class STAFF(forms.ModelForm):
    class Meta:
        model=staff
        fields=('Staff_Name','Password')

    def clean(self):
        cleaned_data = super().clean()
        Staff_Name = cleaned_data.get('Staff_Name')
        Password = cleaned_data.get('Password')
        
        if Staff_Name and Password:
            try:
                user =staff.objects.get(Staff_Name=Staff_Name)
                if user.Password != Password:
                    raise forms.ValidationError('incorrect name or password')
            except staff.DoesNotExist:
                raise forms.ValidationError('incorrect name or register no')
            return cleaned_data






class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['Subject_Name']



class StudentMarksForm(forms.ModelForm):
    class Meta:
        model = Student_Marks
        fields = ['Name', 'Reg_No', 'Sem', 'Sql', 'Frontend', 'python', 'Django']