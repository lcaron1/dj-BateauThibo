from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from myRevendeurApp.config import baseUrl
from myRevendeurApp.models import InfoProduct
from myRevendeurApp.serializers import InfoProductSerializer
from django.http import Http404
from django.http import JsonResponse

# Create your views here.
class ViewInfoProduct(APIView):
    
    def get_object(self, pk):
        try:
            return InfoProduct.objects.get(tigID=pk)
        except:
            raise Http404
        
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = InfoProductSerializer(product)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        jsondata["quantityInStock"] = serializer.data['quantityInStock']
        jsondata["sale"] = serializer.data['sale']
        jsondata["discount"] = serializer.data['discount']
        return Response(jsondata)
    
class ViewInfoProducts(APIView):
    def get_object(self, pk):
        try:
            return InfoProduct.objects.get(tigID=pk)
        except:
            pass
        
    def get(self, request, format=None):
        res=[]
        for prod in InfoProduct.objects.all():
            serializer = InfoProductSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            jsondata['quantityInStock'] = serializer.data['quantityInStock']
            jsondata["sale"] = serializer.data['sale']
            jsondata["discount"] = serializer.data['discount']
            res.append(jsondata)
        return Response(res)

class ViewPutOnSale(APIView):
    def get_object(self, pk):
        try:
            return InfoProduct.objects.get(tigID=pk)
        except:
            raise Http404
        
    def get(self, request, pk, newprice, format=None):
        product = self.get_object(pk)
        serializer = InfoProductSerializer(product)
        res = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = res.json()
        jsondata['sale'] = True
        product.sale = True
        jsondata['discount'] = newprice
        product.discount = newprice
        product.save()
        return Response(jsondata)

class ViewRemoveSale(APIView):
    def get_object(self, pk):
        try:
            return InfoProduct.objects.get(tigID=pk)
        except:
            raise Http404
        
    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = InfoProductSerializer(product)
        res = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = res.json()
        jsondata['sale'] = False
        product.sale = False
        jsondata['discount'] = 0.00
        product.discount = 0.00
        product.save()
        return Response(jsondata)

class ViewIncrementStock(APIView):
    def get_object(self, pk):
        try:
            return InfoProduct.objects.get(tigID=pk)
        except:
            raise Http404
        
    def get(self, request, pk, number, format=None):
        product = self.get_object(pk)
        serializer = InfoProductSerializer(product)
        res = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = res.json()
        quantity = serializer.data['quantityInStock'] + number
        jsondata['quantityInStock'] = quantity
        product.quantityInStock = quantity
        product.save()
        return Response(jsondata)

class ViewDecrementStock(APIView):
    def get_object(self, pk):
        try:
            return InfoProduct.objects.get(tigID=pk)
        except:
            raise Http404
        
    def get(self, request, pk, number, format=None):
        product = self.get_object(pk)
        serializer = InfoProductSerializer(product)
        res = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = res.json()
        quantity = serializer.data['quantityInStock'] - number
        jsondata['quantityInStock'] = quantity
        product.quantityInStock = quantity
        product.save()
        return Response(jsondata)

