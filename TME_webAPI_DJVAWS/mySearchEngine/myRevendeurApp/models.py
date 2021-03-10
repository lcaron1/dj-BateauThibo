from django.db import models

# Create your models here.
class InfoProduct(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    quantityInStock = models.IntegerField(default=0)
    tigID = models.IntegerField(default='-1')
    discount = models.DecimalField(max_digits=20, decimal_places=2,default=0.00)
    sale = models.BooleanField(default=False)
    class Meta:
        ordering = ('tigID',)