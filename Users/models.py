from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractUser, BaseUserManager
from PIL import Image

class EmployeeManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Employee(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1,choices=[('M', 'Male'), ('F', 'Female')],default='M')
    # unit = models.ForeignKey('Unit',on_delete=models.SET_NULL,null=True,blank=True)
    unit = models.ForeignKey('Core.Unit', on_delete=models.PROTECT, null=True, blank=True, related_name='employees')

    def get_unit(self):
        Unit = apps.get_model('Core', 'Unit')
        return Unit.objects.get(pk=self.unit_id)
    
    position = models.CharField(max_length=20, null=True, blank= True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    job_title = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    hired_date = models.DateTimeField(auto_now_add=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = EmployeeManager()
    
    class Meta:
        ordering = ['last_name', 'first_name']

class Profile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.employee.email}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and hasattr(self.image, 'path'):
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

class Group(models.Model):
    unit = models.ForeignKey('Core.Unit', on_delete=models.CASCADE, null=True, blank=True, related_name='groups')

    def get_unit(self):
        Unit = apps.get_model('Core', 'Unit')
        return Unit.objects.get(pk=self.unit_id)
    name = models.CharField(max_length=255)
    employee = models.ManyToManyField(Employee, related_name='group')

    def __str__(self):
        return self.name