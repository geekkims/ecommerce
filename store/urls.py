from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name='store'


urlpatterns = [

    path('',views.store,name="store"),
    path('category/<slug:category_slug>/',views.store,name="product_by_category"),
    path('category/<slug:category_slug>/<slug:product_slug>/',views.product_detail,name="product_detail"),
    path('search/',views.search,name='search'),
    path('search-income', csrf_exempt(views.search_product),
         name="search_product"),
]