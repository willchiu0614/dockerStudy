from django.db import models

class Hospital(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)
    established_date = models.DateTimeField('date established')
    capacity = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Department(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    name = models.TextField(max_length=200)
    floor = models.IntegerField(default=1)
    def __str__(self):
        return self.name