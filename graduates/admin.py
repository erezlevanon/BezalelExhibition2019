from django.contrib import admin

from .models import Graduate, GraduateAdmin, Class

admin.site.register(Graduate, GraduateAdmin)
admin.site.register(Class)
