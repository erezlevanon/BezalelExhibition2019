from django.db import models


class Graduate(models.Model):
    name = models.CharField(max_length=25)
