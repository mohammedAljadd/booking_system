from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('book', views.book, name='book'),
    path('book/<int:id_building>', views.book_building, name='book_building'),
    path('book/<int:id_building>/manage-booking', views.book_room, name='book_room'),
    path('manage-booking', views.manage_booking, name='manage_booking'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
