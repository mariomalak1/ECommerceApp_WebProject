from django.urls import path, include

urlpatterns = [
    path("auth/", include("Authentication.urls")),
    path("products/", include("Product.urls")),
    path("orders/", include("Order.urls")),
]