from django.contrib import admin
from .models import Branch, Server, Reception, Periphery, QA

# Register your models here.
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'branch')

class ReceptionAdmin(admin.ModelAdmin):
    list_display = ('ip', 'phone', 'branch')

class PeripheryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class QAAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


admin.site.register(Branch, BranchAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(Reception, ReceptionAdmin)
admin.site.register(Periphery, PeripheryAdmin)
admin.site.register(QA, QAAdmin)