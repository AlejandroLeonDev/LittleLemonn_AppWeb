from django.urls import path
from .views import home, about, menu_item, display_menu_item, book, reservations, bookings

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('menu/', menu_item, name='menu'),
    path('menu_item/<int:pk>/', display_menu_item, name="menu_item"),
    path('book/', book, name="book"),
    path('reservations/', reservations, name="reservations"),
    path('bookings', bookings, name='bookings'),
]