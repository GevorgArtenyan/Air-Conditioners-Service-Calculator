from django.db import models

class Brand(models.Model):
    ac_brand_name = models.CharField(max_length=200)

    def __str__(self):
        return self.ac_brand_name

class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    ac_model_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.brand} - {self.ac_model_name}"