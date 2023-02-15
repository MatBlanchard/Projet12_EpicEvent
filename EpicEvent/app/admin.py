from django.contrib import admin
from app.models import User, Client, Contract, Event


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'role']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id']


class ContractAdmin(admin.ModelAdmin):
    list_display = ['id']


class EventAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
