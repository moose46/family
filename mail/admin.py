from django.contrib import admin

# Register your models here.
from .models import Mail

from mail.models import Mail, Address


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass