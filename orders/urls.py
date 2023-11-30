from django.urls import path

from . import views

urlpatterns = [
    path("create/",views.OrdercreateView.as_view(), name='order_create'),
    path("detail/",views.OrderDetailView.as_view(), name='order_detail'),
]
