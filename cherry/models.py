from django.db import models

# Create your models here.

class Bank(models.Model):
    BName=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.BName

class Branch(models.Model):
    BName=models.ForeignKey(Bank,on_delete=models.CASCADE)
    IFSC=models.CharField(max_length=11,primary_key=True)
    BRANCH=models.CharField(max_length=29)
    ADDRESS=models.TextField()
    CONTACT=models.IntegerField()
    CITY=models.CharField(max_length=22)
    DISTRICT=models.CharField(max_length=29)
    STATE=models.CharField(max_length=29)


    def __str__(self) -> str:
        return self.BRANCH