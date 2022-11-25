from django.db import models
from django.utils import timezone

class TodoMdel(models.Model):
    title = models.CharField(max_length=100,default=True)
    description = models.TextField(blank=True,null=True)
    Status_opetions = (('complete','complete'),('pending','pending'))
    status = models.CharField(max_length=30,choices=Status_opetions)
    date_created = models.DateTimeField(default=timezone.now,blank=True,null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


