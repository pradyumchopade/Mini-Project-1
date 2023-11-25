from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hostel_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = 'cammess'

class Seat(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()
    is_booked = models.BooleanField(default=False)
    unique_identifier = models.CharField(max_length=50, unique=True)

    class Meta:
        app_label = 'cammess'

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu_images/')
    day = models.DateField()
    meal_time = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'cammess'
