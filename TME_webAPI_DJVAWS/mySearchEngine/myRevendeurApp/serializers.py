from rest_framework.serializers import ModelSerializer
from myRevendeurApp.models import InfoProduct

class InfoProductSerializer(ModelSerializer):
    class Meta:
        model = InfoProduct
        fields = ('tigID','quantityInStock','sale','discount',)