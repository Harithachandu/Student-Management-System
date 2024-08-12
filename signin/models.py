from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=150)
    password =models.IntegerField()

    class Meta:
        verbose_name_plural = 'Login'



    def __str__(self):
        return self.username



class hari(models.Model):
    Student_Name = models.CharField(max_length=200)
    Register_No = models.CharField(max_length=20)
    Student_Semister=models.IntegerField(default=None)

    class Meta:
        verbose_name_plural = 'Student'

    def __str__(self):
        return self.Student_Name
    
    
class staff(models.Model):
    Staff_Name = models.CharField(max_length=250)
    Password = models.IntegerField()



    def __str__(self):
        return self.Staff_Name
    


class Subject(models.Model):
    Subject_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Subject_Name
    


class Deletesub(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class StaffDetails(models.Model):
    subject_choices=(('PYTHON','Python'),('SQL','SQL'),('FRONTEND','Frontend'),('DJANGO','Django'))
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Subject = models.CharField(max_length=20,choices=subject_choices)
    Experience = models.IntegerField()
     
    
    def _str_(self):
        return self.Name
    

# class studentresult(models.Model):
#     name=models.CharField(max_length=100)
#     Roll_No=models.IntegerField()
#     Course =models.CharField(max_length=20)
#     Sem_Result=models.IntegerField()
#     Subject_List=models.CharField(max_length=70)



class Student_Marks(models.Model):
    Name =models.CharField(max_length=100)
    Reg_No =models.CharField(max_length=20)
    Sem =models.IntegerField()
    Sql =models.IntegerField(default=None)
    Frontend=models.IntegerField(default=None)
    python=models.IntegerField(default=None)
    Django=models.IntegerField(default=None)
    Maximum_Marks=models.IntegerField(default=100)
    Obtained_Marks=models.IntegerField(default=None)
    Total_Marks=models.IntegerField(default=None)
    Percentage=models.CharField(max_length=5)

    def __str__(self):
        return self.Name
    

    def save(self, *args, **kwargs):
        sql_marks = self.Sql if self.Sql is not None else 0
        frontend_marks = self.Frontend if self.Frontend is not None else 0
        python_marks = self.python if self.python is not None else 0
        django_marks = self.Django if self.Django is not None else 0

        self.Obtained_Marks = sql_marks + frontend_marks + python_marks + django_marks
        self.Total_Marks = 4 * self.Maximum_Marks  
        
        
        if self.Total_Marks > 0:
            self.Percentage = f"{(self.Obtained_Marks / self.Total_Marks) * 100:.2f}"
        else:
            self.Percentage = "0.00"

        super().save(*args, **kwargs)



