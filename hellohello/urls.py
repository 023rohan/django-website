
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('about/',views.about,name="about"),
    path('Tracker/',views.tracker,name="tracker"),
    path('contact/',views.contact,name="contact"),
    path('search/',views.search,name="search"),
    path("prodview/<int:myid>",views.productView,name="prodview"),
    path('checkout',views.checkout,name="checkout"),
]