from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.AutoField
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    sclass = models.CharField(max_length=50)
    join_dt = models.DateField()

    class Meta:
        db_table = 'student'

    """
    image = models.ImageField(upload_to="shop/images",default="")
   
    def __str__(self):
        return self.product_name

    """