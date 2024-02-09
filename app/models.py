from django.db import models
from datetime import datetime


# Create your models here.
class Player(models.Model):
    """
    Bablablabla
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class ODS(models.Model):
    code_commune = models.CharField(max_length=7, default=None)
    commune = models.CharField(max_length=150, default=None)
    code_qpv = models.CharField(max_length=10, blank=True, null=True, default=None)
    name_qpv = models.CharField(max_length=150, blank=True, null=True, default=None)
    department = models.CharField(max_length=150, default=None)
    region = models.CharField(max_length=150, blank=True, null=True, default=None)
    statut_geo = models.CharField(max_length=150, blank=True, null=True, default=None)
    code_fede = models.IntegerField(default=None)
    federation = models.CharField(max_length=100, blank=True, null=True, default=None)
    clubs = models.IntegerField(default=None)
    epa = models.IntegerField(blank=True, null=True, default=None)
    total = models.IntegerField(default=None)
    date = models.DateField(datetime.now())

    def __str__(self) -> str:
        return f'{self.clubs} {self.federation}'
