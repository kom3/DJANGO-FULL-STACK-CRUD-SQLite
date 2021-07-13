from django.db import models


class Todo(models.Model):
    task =  models.CharField(max_length=200)
    create_date = models.DateField(auto_now=True)
    owner = models.CharField(max_length=100)
    status  = models.CharField(max_length=10)
class meta:
    db_table="todolist"