from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    img_path = models.CharField(max_length=300)

    def __str__(self): #하나의 객체를 문자열로 표현
        return self.name