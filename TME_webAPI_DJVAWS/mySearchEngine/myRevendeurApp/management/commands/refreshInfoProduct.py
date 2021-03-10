from django.core.management.base import BaseCommand, CommandError
from myRevendeurApp.config import baseUrl
from myRevendeurApp.models import InfoProduct
from myRevendeurApp.serializers import InfoProductSerializer
import requests
import time
from random import randrange

class Command(BaseCommand):
    help = 'Refresh the list of products which are on sale.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        InfoProduct.objects.all().delete()
        for product in jsondata:
                serializer = InfoProductSerializer(data={'quantityInStock':str(randrange(15)), 'tigID':str(product['id']), 'sale':str(product['sale']), 'discount':str(product['discount'])})
                if serializer.is_valid():
                    serializer.save()
                    self.stdout.write(self.style.SUCCESS('['+time.ctime()+'] Successfully added product id="%s"' % product['id']))
        self.stdout.write('['+time.ctime()+'] Data refresh terminated.')
