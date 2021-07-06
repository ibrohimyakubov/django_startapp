from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    STARTAPPER = "Startapper"
    DEVELOPER = "Developer"
    PRACTITIONER = "Practitioner"

    USER_TYPE = [
        (STARTAPPER, 'Startapper'),
        (DEVELOPER, 'Developer'),
        (PRACTITIONER, 'Practitioner'),
    ]
    full_name = models.CharField('full name', max_length=200, blank=False, null=False)
    email = models.EmailField('email address', blank=True, null=True, unique=True)
    user_type = models.CharField(max_length=30, choices=USER_TYPE)
    phone = models.CharField(max_length=30, blank=False, null=False, unique=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)


TASHKENT = 'Tashkent'
NEWYORK = 'NewYork'
COUNTRY = [
    (TASHKENT, 'Tashkent'),
    (NEWYORK, 'NewYork'),
]


class Startapper(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...", max_length=400)
    country = models.CharField(max_length=50, blank=True, null=True, choices=COUNTRY)
    image = models.ImageField(upload_to='startapper_file/startapp_image', blank=True)

    def __str__(self):
        return self.user.username


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...", max_length=400)
    country = models.CharField(max_length=50, blank=True, null=True, choices=COUNTRY)
    image = models.ImageField(upload_to='staff_image', blank=True)

    def __str__(self):
        return f"{self.user.username} ----- {self.user.user_type}"


class IdeaStartapper(models.Model):
    user = models.ForeignKey(Startapper, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='media/startapper_idea', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username}  - {self.file}"


class ApplicationStaff(models.Model):
    user = models.ForeignKey(Staff, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    resume = models.FileField(upload_to='media_staff_resume', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} -       {self.user.user.user_type}       - {self.resume}"
