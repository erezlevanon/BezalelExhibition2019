from django.db import models
from django.contrib.admin import ModelAdmin, TabularInline


class Class(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class Graduate(models.Model):
    # Hebrew
    project_title_he = models.CharField(max_length=100, default="", blank=True)
    name_he = models.CharField(max_length=35, default="", blank=True)

    # English
    project_title_en = models.CharField(max_length=100, default="", blank=True)
    name_en = models.CharField(max_length=35, default="", blank=True)

    # Arabic
    project_title_ar = models.CharField(max_length=100, default="", blank=True)
    name_ar = models.CharField(max_length=35, default="", blank=True)

    # Contact Information
    instagram = models.CharField(max_length=60, default="", blank=True)
    email = models.CharField(max_length=60, default="", blank=True)
    personal_website = models.CharField(max_length=60, default="", blank=True)
    bezalel_catalog = models.CharField(max_length=60, default="", blank=True)

    # Media
    profile_image = models.ImageField(blank=True)

    year = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_he


class ProcessImage(models.Model):
    graduate = models.ForeignKey(Graduate, on_delete=models.CASCADE)
    image = models.ImageField()


class ImageInline(TabularInline):
    model = ProcessImage


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
        ('Media', {
            'fields': (
                'profile_image',
            )
        }),
    )

    inlines = [
        ImageInline,
    ]
