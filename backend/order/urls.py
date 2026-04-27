from django.urls import path
from .views import(
    create_new_order,
    login_user_order,
    get_user_orders,
    get_order_by_id,
)

app_name='order'
urlpatterns = [
    path('orders/create/',create_new_order,name='create_new_order'),
    path('orders/login/',login_user_order,name='login_user_order'),
    path('orders/user/',get_user_orders,name='get_user_orders'),
    path('orders/<str:pk>/',get_order_by_id,name='get_order_by_id'),
]
