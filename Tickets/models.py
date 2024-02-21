from django.db import models

# Create your models here.
from datetime import datetime
class State(models.Model):
    state_name = models.CharField(max_length=200)
    state_code = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=datetime.today())
    updated_date = models.DateTimeField(default=datetime.today())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.state_name

    def save(self, *args, **kwargs):
        # Update the updated_date field when the object is being updated
        if self.pk is not None:  # If the object already exists (i.e., being updated)
            self.updated_date = datetime.today()
        super().save(*args, **kwargs)
    

class UserMaster(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.BigIntegerField()
    city = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    joining_date = models.DateField()
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.today())
    updated_date = models.DateTimeField(default=datetime.today())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Update the updated_date field when the object is being updated
        if self.pk is not None:  # If the object already exists (i.e., being updated)
            self.updated_date = datetime.today()
        super().save(*args, **kwargs)


class TaskMaster(models.Model):
    task_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    assign_date= models.DateField()
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=datetime.today())
    updated_date = models.DateTimeField(default=datetime.today())
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Update the updated_date field when the object is being updated
        if self.pk is not None:  # If the object already exists (i.e., being updated)
            self.updated_date = datetime.today()
        super().save(*args, **kwargs)
