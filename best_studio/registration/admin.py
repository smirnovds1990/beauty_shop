from django.contrib import admin

from .models import Master, Procedure


class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_master', 'price')


class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty')


admin.site.register(Master, MasterAdmin)
admin.site.register(Procedure, ProcedureAdmin)
