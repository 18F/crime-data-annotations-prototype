from django.contrib import admin
from .models import Agency, Annotation, USState, Year

admin.site.register(Agency)
admin.site.register(Annotation)
admin.site.register(USState)
admin.site.register(Year)
