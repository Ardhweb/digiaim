from django.shortcuts import render,get_object_or_404
from core.api.serializers import InvoiceSerializer,InvoiceDetailSerializer
from rest_framework import viewsets
from ..models import Invoice, InvoiceDetail

from rest_framework.response import Response

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer   
    
    # #@action(detail=False, methods=['GET'])
    def list(self, request):
     
        invoice = self.queryset.all()
        serializer = self.serializer_class(invoice, many=True)
        return Response(serializer.data)
    
    def get(self, request, pk):
        try:
            obj = self.queryset.get(pk=pk)
        except MyModel.DoesNotExist:
            
            return Response(status=404)

        return Response(obj.data)
    