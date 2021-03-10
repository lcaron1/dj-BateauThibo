from django.core.management.base import BaseCommand, CommandError
from myRevendeurApp.config import baseUrl
from myRevendeurApp.models import InfoProduct
from myRevendeurApp.serializers import InfoProductSerializer
import requests
import time

class Command(BaseCommand):
    help = 'Refresh the list of products which are on sale.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        for product in jsondata:
            obj = InfoProduct.objects.get(tigID=product['id'])
            InfoProduct.objects.get(tigID=product['id']).delete()
            serializer = ""
            if 16 < obj.quantityInStock and obj.quantityInStock < 64:
                serializer = InfoProductSerializer(data={'quantityInStock':str(obj.quantityInStock), 'tigID':str(obj.tigID), 'sale':str(True), 'discount':str(product['price']*0.80)})

            elif obj.quantityInStock >= 64:
                serializer = InfoProductSerializer(data={'quantityInStock':str(obj.quantityInStock), 'tigID':str(obj.tigID), 'sale':str(True), 'discount':str(product['price']*0.50)})

            else:
                serializer = InfoProductSerializer(data={'quantityInStock':str(obj.quantityInStock), 'tigID':str(obj.tigID), 'sale':str(False), 'discount':str(0.00)})

            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS('['+time.ctime()+'] Successfully added product id="%s"' % product['id']))
        self.stdout.write('['+time.ctime()+'] Data refresh terminated.')
                
