from django.contrib import admin
import core.models as coremodels

admin.site.register(coremodels.Location)
admin.site.register(coremodels.Review)