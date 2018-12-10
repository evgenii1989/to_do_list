from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name='Task')
    status = models.CharField(max_length=200, null=False, blank=False, default='new', verbose_name='Status')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Task description')

    def __str__(self):
        return f'{self.pk}. {self.name} ({self.status})'

# Create your models here.
