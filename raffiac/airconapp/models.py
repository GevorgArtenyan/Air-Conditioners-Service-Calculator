from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ACServiceCalc(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    square_feet = models.IntegerField()
    number_of_rooms = models.IntegerField()