from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from .models import UserProfile, MenuItem, Seat
import stripe

# Stripe Configuration (You need to set up Stripe in your project settings)
stripe.api_key = "your_stripe_api_key"

# Welcome Page
def welcome(request):
    return render(request, 'cammess/welcome.html')

# Admin Login
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_admin:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to admin dashboard
        else:
            return render(request, 'cammess/admin_login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'cammess/admin_login.html')

# Guest Login
def guest_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_guest:
            login(request, user)
            return redirect('guest_dashboard')  # Redirect to guest dashboard
        else:
            return render(request, 'cammess/guest_login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'cammess/guest_login.html')

# Hostler Sign-Up
def hostler_signup(request):
    if request.method == 'POST':
        enrollment_number = request.POST['enrollment_number']
        name = request.POST['name']
        hostel_name = request.POST['hostel_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            user = UserProfile.objects.create_user(enrollment_number, name, hostel_name, email, phone_number, password)
            user.is_hostler = True
            user.save()
            login(request, user)
            return redirect('hostler_dashboard')  # Redirect to hostler dashboard
        else:
            return render(request, 'cammess/hostler_signup.html', {'error_message': 'Password mismatch'})

    return render(request, 'cammess/hostler_signup.html')

# Hostler Login
def hostler_login(request):
    if request.method == 'POST':
        enrollment_number = request.POST['enrollment_number']
        password = request.POST['password']
        user = authenticate(request, username=enrollment_number, password=password)
        if user is not None and user.is_hostler:
            login(request, user)
            return redirect('hostler_dashboard')  # Redirect to hostler dashboard
        else:
            return render(request, 'cammess/hostler_login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'cammess/hostler_login.html')

# Guest Sign-Up
def guest_signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            user = UserProfile.objects.create_user(phone_number, name, password)
            user.is_guest = True
            user.save()
            login(request, user)
            return redirect('guest_dashboard')  # Redirect to guest dashboard
        else:
            return render(request, 'cammess/guest_signup.html', {'error_message': 'Password mismatch'})

    return render(request, 'cammess/guest_signup.html')

#  Dashboard
@login_required
def dashboard(request):
    # Add your admin dashboard logic here
    return render(request, 'cammess/dashboard.html')

# Mess Menu Display
@login_required
def menu_display(request):
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)

    meal_time = request.GET.get('meal_time', 'breakfast')

    menu_items = MenuItem.objects.filter(
        day__gte=week_start, day__lte=week_end, meal_time=meal_time
    )

    return render(request, 'cammess/menu_display.html', {
        'today': today,
        'week_start': week_start,
        'week_end': week_end,
        'meal_time': meal_time,
        'menu_items': menu_items,
    })

# Seat Selection
@login_required
def seat_selection(request):
    # Add your seat selection logic here
    return render(request, 'cammess/seat_selection.html')

# Payment Gateway (Stripe in this example)
@login_required
def payment(request):
    if request.method == 'POST':
        amount = 1000  # Amount in cents
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
        )
        return render(request, 'cammess/payment.html', {'client_secret': intent.client_secret})
    
    return render(request, 'cammess/payment.html')

# Confirmation Page
@login_required
def confirmation(request):
    # Add your confirmation logic here
    return render(request, 'cammess/confirmation.html')

# Generate QR Code
@login_required
def generate_qr_code(request, reservation_id):
    # Add your QR code generation logic here
    return render(request, 'cammess/generate_qr_code.html')

# Add your remaining views and logic as needed
