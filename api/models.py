import uuid
from django.db import models

# Create your models here.


class student(models.Model):
    student_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    matric = models.CharField(max_length=10, unique=True)
    department = models.TextField()
    level = models.CharField(max_length=4)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    sup_id = models.TextField(default="")
    password = models.TextField()


class organization(models.Model):
    org_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    org_name = models.CharField(max_length=200)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    department = models.CharField(max_length=100)
    job_desc = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    lga = models.CharField(max_length=200)
    student_id = models.TextField(default=None)


class supervisor(models.Model):
    sup_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    password = models.TextField()


class message(models.Model):
    id = models.AutoField(primary_key=True, editable=False, default=None)
    content = models.TextField()
    sup_id = models.TextField()
    created_at = models.DateField(auto_now_add=True)


class message_count(models.Model):
    id = models.AutoField(primary_key=True, editable=False, default=None)
    sup_id = models.TextField()
    count = models.IntegerField()


class report(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    mon = models.TextField()
    tue = models.TextField()
    wed = models.TextField()
    thur = models.TextField()
    fri = models.TextField()
    mon_date = models.DateField()
    tue_date = models.DateField()
    wed_date = models.DateField()
    thur_date = models.DateField()
    fri_date = models.DateField()
    student_id = models.TextField()
    is_signed = models.BooleanField(default=False)
    date_signed = models.DateField()
