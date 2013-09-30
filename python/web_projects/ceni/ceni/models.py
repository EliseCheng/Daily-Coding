from django.db import models

class test(models.Model):
    col1 = models.CharField(max_length=30)
    col2 = models.URLField()
