from django.db import models

class Togri(models.Model):
    soz = models.CharField(max_length=50)
    def __str__(self):
        return  self.soz
class Natogri(models.Model):
    natogri_soz = models.CharField(max_length=50)
    togri = models.ForeignKey(Togri, on_delete=models.CASCADE)
    def __str__(self):
        return  self.natogri_soz