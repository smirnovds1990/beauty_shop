from django.contrib import admin

from .models import Customer, Master, Procedure, Record


class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_master', 'price')


class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')


class RecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'master', 'procedure', 'customer')


admin.site.register(Master, MasterAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Record, RecordAdmin)
