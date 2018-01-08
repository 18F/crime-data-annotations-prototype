from django.contrib import admin
from .models import Agency, Annotation, USState, Year

class AgencyAdmin(admin.ModelAdmin):
    list_display = ('ori', 'name', 'agency_type', 'us_state')
    list_filter = ('agency_type', 'us_state')
    search_fields = ('ori', 'name')

class AnnotationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'data_type', 'annotation_type', 'offense', 'us_state')
    list_filter = ('data_type', 'annotation_type',  'us_state')

class USStateAdmin(admin.ModelAdmin):
    pass

class YearAdmin(admin.ModelAdmin):
    pass


admin.site.register(Agency, AgencyAdmin)
admin.site.register(Annotation, AnnotationAdmin)
admin.site.register(USState, USStateAdmin)
admin.site.register(Year, YearAdmin)
