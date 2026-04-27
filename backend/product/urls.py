from django.urls import path
from .views import (
    get_all_products,
    get_product_by_id,
    create_product,
    delete_product,
    update_product,
    create_product_review,
    update_product_reivew,
    delete_product_review,
)

app_aname='product'
urlpatterns = [
    path('products/',get_all_products,name='get_all_products'),
    path('products/<str:pk>/',get_product_by_id,name='get_product_by_id'),
    path('products/create/',create_product,name='create_product'),
    path('products/<str:pk>/delete/',delete_product,name='delete_product'),
    path('products/<str:pk>/update/',update_product,name='update_product'),
    path('products/<str:pk>/reviews/create/',create_product_review,name='create_product_review'),
    path('products/reviews/<str:pk>/update/',update_product_reivew,name='update_product_reivew'),
    path('products/reviews/<str:pk>/delete/',delete_product_review,name='delete_product_review'),]