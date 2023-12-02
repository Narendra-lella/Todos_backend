from django.db import models

# Create your models here.

class Totomodel(models.Model):
    tittle = models.TextField(max_length=30)
    discription = models.TextField(max_length=400)
    is_done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'todos'
