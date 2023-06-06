from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")
        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

    

  
class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    company_name=models.CharField(verbose_name="company name", max_length=100, unique=False)
    phone=models.CharField(verbose_name="phone", max_length=15)
    profile_image = models.ImageField(upload_to='media/', blank=True, null=True)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    # Role_Choices = (
    #         ('MULTI TEACHER', 'MULTI TEACHER'),
    #         ('PHYSICS TEACHER', 'PHYSICS TEACHER'),
    #         ('CHEMISTRY TEACHER', 'CHEMISTRY TEACHER'),
    #         ('BIOLOGY TEACHER', 'BIOLOGY TEACHER'),
    #         ('ENGLISH TEACHER', 'ENGLISH TEACHER'),
    #         ('CIVICS TEACHER', 'CIVICS TEACHER'),
    #         ('MATHEMATICS TEACHER', 'MATHEMATICS TEACHER'),
    #         ('HISTORY TEACHER', 'HISTORY TEACHER'),
    #         ('GEOGRAPHY TEACHER', 'GEOGRAPHY TEACHER'),
    #         ('KISWAHILI TEACHER', 'KISWAHILI TEACHER'),
    #     )

    # role=models.CharField(verbose_name="role", choices=Role_Choices, max_length=50)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Universities(models.Model):

    UniversityName = models.CharField(max_length=200)
    UniversityPlace = models.CharField(max_length=100,blank=True,null=True)
    UniversityImage = models.ImageField(upload_to='media/UniversityImage/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
    	verbose_name_plural = "Universities"

    def __str__(self):
    	return self.UniversityName


class UniversityCourses(models.Model):

    university = models.ManyToManyField(Universities,max_length=200)
    CourseName = models.CharField(max_length=100,blank=True,null=True)
    CourseImage = models.ImageField(upload_to='media/UniversityImage/',blank=True,null=True)
    CourseDepartment = models.CharField(max_length=100,blank=True,null=True)
    CourseCapacity = models.IntegerField(blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "UniversityCourses"

    def __str__(self):
        return self.CourseName

class Modules(models.Model):

    university = models.ManyToManyField(Universities,max_length=200)
    course = models.ForeignKey(UniversityCourses,max_length=200,on_delete=models.CASCADE)
    ModuleName = models.CharField(max_length=100,blank=True,null=True)
    Year = models.CharField(default="First Year",max_length=100,blank=True,null=True)
    ModuleImage = models.ImageField(upload_to='media/ModuleImage/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.ModuleName


class AllProjects(models.Model):

    university = models.ForeignKey(Universities,max_length=200, on_delete=models.CASCADE)
    ProjectName = models.CharField(max_length=500,blank=False,null=False)
    StudentName = models.CharField(max_length=100,blank=False,null=False)
    Year = models.CharField(max_length=50,blank=False,null=False)
    ProjectBody = RichTextUploadingField(blank=True,null=True)
    pdf = models.FileField(upload_to="media/ProjectsPDF",blank=True,null=True)
    
    Gender_Choices = (
        ('Male','Male'),
        ('Female', 'Female')
        )


    Gender = models.CharField(max_length=100,choices=Gender_Choices, blank=True,null=True)
    CourseName = models.ForeignKey(UniversityCourses, max_length=100,on_delete=models.CASCADE, blank=False,null=False)
    ProjectImage = models.ImageField(upload_to='media/UniversityImage/',blank=True,null=True)
    PdfFile = models.CharField(default="https://programmers.pythonanywhere.com/admin/DimosoApp/uploadfiles/32/change/pdfs/test_01__test_02.pdf", max_length=1000,blank=True,null=True)
    
    VideoLink = models.CharField(default="www.youtube.com/dimosojunior", max_length=200,blank=True,null=True)
    StudentEmail = models.EmailField(default="@gmail.com", max_length=100,blank=True,null=True)
    StudentPhoneNumber = models.CharField(default="+255", max_length=50,blank=True,null=True)
    Github = models.CharField(default="https://github.com/dimosojunior/", max_length=1000,blank=True,null=True)
    Youtube = models.CharField(default="www.youtube.com", max_length=1000,blank=True,null=True)
    WhatsappLink = models.CharField(default="www.whatsapp.com", max_length=1000,blank=True,null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "AllProjects"

    def __str__(self):
        return self.ProjectName



class Articles(models.Model):

    ArticlesName = models.CharField(max_length=1000,blank=False,null=False)
    ArticleImage = models.ImageField(upload_to='media/ArticlesImage/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.ArticlesName


class ArticlesCategory(models.Model):

    ArticlesName = models.ForeignKey(Articles,on_delete=models.CASCADE, max_length=1000,blank=False,null=False)
    WrittenBy = models.CharField(default="Dimoso Junior",max_length=100,blank=True,null=True)
    ArticleBody = RichTextUploadingField(blank=True,null=True)
    ShortDescription = RichTextUploadingField(blank=True,null=True)
    ArticleImage = models.ImageField(upload_to='media/ArticlesImage/',blank=True,null=True)
    Github = models.CharField(default="www.github.com",max_length=1000,blank=True,null=True)
    Youtube = models.CharField(default="www.youtube.com",max_length=1000,blank=True,null=True)
    year = models.CharField(default="2023",max_length=100,blank=True,null=True)
    pdf = models.FileField(upload_to="media/ArticlesPDF/",blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "ArticlesCategory"

    def __str__(self):
        return self.ArticlesName.ArticlesName




class Hob(models.Model):

    
    CategoryName = models.CharField(max_length=1000,blank=False,null=False)
    CategoryImage = models.ImageField(upload_to='media/HobImage/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Hob"

    def __str__(self):
        return self.CategoryName




class Experts(models.Model):

    CategoryName = models.ForeignKey(Hob,on_delete=models.CASCADE, max_length=1000,blank=False,null=False)
    StudentName = models.CharField(max_length=500,blank=False,null=False)
    StudentPlace = models.CharField(max_length=100,blank=True,null=True)
    Body = RichTextUploadingField(blank=True,null=True)
    ShortDescription = RichTextUploadingField(blank=True,null=True)
    StudentImage = models.ImageField(upload_to='media/Hob/',blank=True,null=True)
    Github = models.CharField(default="www.github.com",max_length=1000,blank=True,null=True)
    Youtube = models.CharField(default="www.youtube.com",max_length=1000,blank=True,null=True)
    Email = models.CharField(default="juniordimoso@gmail.com",max_length=500,blank=True,null=True)
    Instagram = models.CharField(default="www.instagram.com",max_length=1000,blank=True,null=True)
    Whatsapp = models.CharField(default="www.whatsapp.com",max_length=1000,blank=True,null=True)
    Phone = models.CharField(default="+255 628 431 507",max_length=13,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Experts"

    def __str__(self):
        return self.StudentName




class Students(models.Model):

    university = models.ForeignKey(Universities,max_length=200,on_delete=models.CASCADE)
    course = models.ForeignKey(UniversityCourses,max_length=200,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=100,blank=False,null=False)
    LastName = models.CharField(max_length=100,blank=False,null=False)
    Email = models.EmailField(default="@gmail.com", max_length=100,blank=False,null=False)
    Phone = models.CharField(default="+255", max_length=13,blank=False,null=False)
    StudentImage = models.ImageField(upload_to='media/StudentImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return self.FirstName + " " + self.LastName


class Teachers(models.Model):

    university = models.ForeignKey(Universities,max_length=200,on_delete=models.CASCADE)
    course = models.ManyToManyField(UniversityCourses,max_length=200)
    FirstName = models.CharField(max_length=100,blank=False,null=False)
    LastName = models.CharField(max_length=100,blank=False,null=False)
    Email = models.EmailField(default="@gmail.com", max_length=100,blank=False,null=False)
    Phone = models.CharField(default="+255", max_length=13,blank=False,null=False)
    TeacherImage = models.ImageField(upload_to='media/StudentImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.FirstName + " " + self.LastName