from . import views

from django.urls import path

app_name = 'shopapp'

urlpatterns = [
    path('',views.allProducts,name='allProducts'),
    path('<slug:c_slug>/',views.allProducts,name='product_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='proCatdetails'),
]
