from django.db import models

# Create your models here.
 
class UserInfo(models.Model):
    name =models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age =models.IntegerField()
     

class Department(models.Model):
    title=models.CharField(max_length=26)
    
# Department.objects.create(title='超人部')’

# UserInfo.objects.create(name='迪迦',password='556',age='99') 
# UserInfo.objects.create(name='迪第',password='126',age='9')  
 
# class Page(models.Model):
#     name =models.CharField(max_length=32)
#     password = models.CharField(max_length=64)
 

class Upcontent(models.Model):
    title=models.CharField(max_length=100, null=False, blank=False)
    text=models.TextField(null=False, blank=True, default='')   
    def __str__(self):
     if self.title is not None:
         return self.title
     else:
          return "Untitled"
