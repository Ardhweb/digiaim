from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _

import uuid

def get_uuid_only_int_6digits():
    uuid_int = uuid.uuid4().int
    uuid_6digits = uuid_int % 10**6
    return uuid_6digits

class Invoice(models.Model):
    date = models.DateField(auto_now_add=True,blank=True, null=True)
    invoice_no = models.CharField(default=get_uuid_only_int_6digits(),
    max_length=7,blank=True, 
    null=True,editable=False)
    customer_name = models.CharField(max_length=20, blank=True, null=True, verbose_name="Customer Full Name")

    def __str__(self):
        return str(f'{self.invoice_no}{self.customer_name}')

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE,null=True, related_name='invoice_detail')
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name="Description")
    quantity = models.PositiveIntegerField(blank=True, null=True,)
    unit_price =  models.PositiveIntegerField(blank=True, null=True,)
    price =  models.DecimalField(max_digits=6,decimal_places=2)