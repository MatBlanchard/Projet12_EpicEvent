from django.contrib import admin
from app.models import User, Client, Contract, Event


class UserAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'email',
                    'first_name',
                    'last_name',
                    'role',
                    'phone',
                    'mobile']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'email',
                    'first_name',
                    'last_name',
                    'phone',
                    'mobile',
                    'company_name',
                    'date_created',
                    'date_updated',
                    'sales_contact',
                    'status']


class ContractAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'date_created',
                    'date_updated',
                    'is_active',
                    'amount',
                    'payment_due',
                    'sales_contact',
                    'client']


class EventAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'date_created',
                    'date_updated',
                    'status',
                    'attendees',
                    'event_date',
                    'notes',
                    'support_contact',
                    'client',
                    'contract']


admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
