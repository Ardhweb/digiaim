from core.models import Invoice , InvoiceDetail
from rest_framework import serializers


class InvoiceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceDetail
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    invoice_detail = InvoiceDetailSerializer(many=True)
   
    class Meta:
        model = Invoice
        fields = ['date', 'invoice_no', 'customer_name','invoice_detail']



    
    def create(self, validated_data):
        invoice_detail_data = validated_data.pop('invoice_detail')
        invoice = Invoice.objects.create(**validated_data)
        for invoice_detail_data in invoice_detail_data:
            InvoiceDetail.objects.create(invoice=invoice, **invoice_detail_data)
        return invoice

    
    
    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.invoice_no = validated_data.get('invoice_no', instance.invoice_no)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)

        invoice_details_data = validated_data.pop('invoice_detail')
        invoice_details = (instance.invoice_detail).all()
        invoice_details = list(invoice_details)
        for invoice_detail_data in invoice_details_data:
            if 'id' in invoice_detail_data:
                id = invoice_detail_data['id']
                invoice_detail = [x for x in invoice_details if x.id == id][0]
                invoice_details.remove(invoice_detail)
                invoice_detail.description = invoice_detail_data.get('description', invoice_detail.description)
                invoice_detail.quantity = invoice_detail_data.get('quantity', invoice_detail.quantity)
                invoice_detail.unit_price = invoice_detail_data.get('unit_price', invoice_detail.unit_price)
                invoice_detail.price = invoice_detail_data.get('price', invoice_detail.price)
                invoice_detail.save()
            else:
                InvoiceDetail.objects.create(invoice=instance, **invoice_detail_data)

        for invoice_detail in invoice_details:
            invoice_detail.delete()

        instance.save()
        return instance



