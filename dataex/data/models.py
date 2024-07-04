from django.db import models

# Create your models here.
class Username(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Languages(models.Model):
    User = models.ForeignKey(Username,on_delete=models.CASCADE,related_name='userlang')
    Python = models.IntegerField()
    Java = models.IntegerField()
    Php = models.IntegerField()
    Cotlin = models.IntegerField()
    Golang = models.IntegerField()

