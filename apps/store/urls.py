from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<slug:category_slug>/', views.filtered_products, name='filtered_products'),
    path('<slug:category_slug>/<slug:product_slug>/', views.single_product, name='single_product')
    , 
]
