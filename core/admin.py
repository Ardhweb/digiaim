from django.contrib import admin

# Register your models here.
from .models import Invoice , InvoiceDetail



# class InvoiceDetailInline(admin.TabularInline):
#     model = InvoiceDetail


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("invoice_no","date",)
    #inlines = [InvoiceDetailInline]


@admin.register(InvoiceDetail)
class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ('id',)