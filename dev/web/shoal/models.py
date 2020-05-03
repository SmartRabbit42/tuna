from django.db import models

class Shoal(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    icon_url = models.CharField(max_length=1028)
    max_size =  models.IntegerField()

    def __str__(self):
        return self.name

class Fish(models.Model):
    shoal = models.ForeignKey(Shoal, on_delete=models.CASCADE)
    status = models.IntegerField()
    scalecolor = models.IntegerField()
    displayname = models.CharField(max_length=64)
    icon_url = models.CharField(max_length=1028)

    def __str__(self):
        return "{0} from {1} shoal".format(self.displayname, self.shoal.name)
