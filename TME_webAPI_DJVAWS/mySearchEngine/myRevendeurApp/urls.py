from django.urls import path, register_converter
from myRevendeurApp import views

class FloatUrlParameterConverter:
    regex = '[0-9]+\.?[0-9]+'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)

register_converter(FloatUrlParameterConverter, 'Paramfloats')

urlpatterns = [
    path('infoproduct/<int:pk>/', views.ViewInfoProduct.as_view()),
    path('infoproducts/', views.ViewInfoProducts.as_view()),
    path('putonsale/<int:pk>/<Paramfloats:newprice>/', views.ViewPutOnSale.as_view()),
    path('removesale/<int:pk>/', views.ViewRemoveSale.as_view()),
    path('incrementStock/<int:pk>/<int:number>/', views.ViewIncrementStock.as_view()),
    path('decrementStock/<int:pk>/<int:number>/', views.ViewDecrementStock.as_view()),
]

