from django.urls import path
from . import views

urlpatterns = [
    
    # Welcome Page
    path('', views.welcome, name='welcome'),

    # Admin Login
    path('admin-login/', views.admin_login, name='admin_login'),

    # Guest Login
    path('guest-login/', views.guest_login, name='guest_login'),

    # Hostler Sign-Up
    path('hostler-signup/', views.hostler_signup, name='hostler_signup'),

    # Hostler Login
    path('hostler-login/', views.hostler_login, name='hostler_login'),

    # Guest Sign-Up
    path('guest-signup/', views.guest_signup, name='guest_signup'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Mess Menu
    path('menu-display/', views.menu_display, name='menu_display'),

    # Seat Selection
    path('seat-selection/', views.seat_selection, name='seat_selection'),

    # Payment Gateway (Stripe in this example)
    path('payment/', views.payment, name='payment'),

    # Confirmation Page
    path('confirmation/', views.confirmation, name='confirmation'),

    # Generate QR Code
    path('generate-qr-code/<str:reservation_id>/', views.generate_qr_code, name='generate_qr_code'),

    path('menu/', views.menu_display, name='menu_display'),
]

