from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .models import Flight, Passenger, Reservation, Payment
from .forms import ReservationForm, PaymentForm, SignUpForm, LoginForm

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights.html', {'flights': flights})

def reserve_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        payment_form = PaymentForm(request.POST)

        if reservation_form.is_valid() and payment_form.is_valid():
            passenger = reservation_form.save(commit=False)
            passenger.user = request.user  # Assigning logged-in user to passenger
            passenger.save()

            reservation = Reservation.objects.create(
                reservation_date=timezone.now(),
                status='Reserved',
                flight=flight,
                passenger=passenger
            )

            payment = payment_form.save(commit=False)
            payment.payment_date = timezone.now()
            payment.reservation = reservation
            payment.save()

            return redirect('reservation_success')
    else:
        reservation_form = ReservationForm()
        payment_form = PaymentForm()

    return render(request, 'reserve_flight.html', {
        'flight': flight,
        'reservation_form': reservation_form,
        'payment_form': payment_form
    })

def reservation_success(request):
    return render(request, 'reservation_success.html')

def chatgpt_view(request):
    # Render the ChatGPT iframe view
    return render(request, 'chatgpt.html')




