from django.db import models
from django.contrib.admin import ModelAdmin


class Class(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Graduate(models.Model):
    # Hebrew
    project_title_he = models.CharField(max_length=100)
    name_he = models.CharField(max_length=25)

    # English
    project_title_en = models.CharField(max_length=100)
    name_en = models.CharField(max_length=25)

    # Arabic
    project_title_ar = models.CharField(max_length=100)
    name_ar = models.CharField(max_length=25)

    # Contact Information
    instagram = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    personal_website = models.CharField(max_length=60)
    bezalel_catalog = models.CharField(max_length=60)

    year = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_he + ' (' + str(self.year) + ')'


class GraduateAdmin(ModelAdmin):
    fieldsets = (
        ('Contact Information', {
            'fields': (
                       'instagram',
                       'email',
                       'personal_website',
                       'bezalel_catalog',
                       'year',
                       )
        }),
        ('Hebrew', {
            'fields': (
                 'name_he',
                 'project_title_he',
            ),
        }),
        ('English', {
            'fields': (
                'name_en',
                'project_title_en',
            ),
        }),
        ('Arabic', {
            'fields': (
                'name_ar',
                'project_title_ar',
            ),
        }),
    )
