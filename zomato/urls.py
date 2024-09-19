from django.urls import path
from .import views
urlpatterns=[
    path("",views.index,name="index"),
    path("food/",views.food,name="food"),
    path("home",views.home,name="home"),
    path("registration",views.registration,name="registration"),
    path('add/<int:product_id>/', views.order_now, name='order_now'),
    path("cart",views.cart,name="cart"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("checkout",views.checkout,name="checkout"), 
    path("continue shop",views.continue_shop,name="continue shop"),
    path("logout",views.logout,name="logout"),
]