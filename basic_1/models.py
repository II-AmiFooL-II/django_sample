from django.db import models

# Create your models here.
class tb_1(models.Model):  
    name    = models.CharField(max_length=100) 
    age     = models.IntegerField()
    class Meta:  
        db_table = "tb_1"  