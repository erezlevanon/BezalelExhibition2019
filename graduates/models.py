from django.db import models


class Class(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Graduate(models.Model):
    name = models.CharField(max_length=25)
    year = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' (' + str(self.year) + ')'
