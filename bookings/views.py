
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from urllib.parse import urlparse
from bookings.tasks import add

def index(request):
    addition = add.delay(5,5)
    print(addition)
    context = {
        "bookings" : Booking.objects.all().count(),
        "rooms" : Room.objects.all().count(),
        "staffs" : staff.objects.all().count()
    }
    return render(request, 'index.html', context)

def booking(request):
    if request.POST:
        booking = Booking.objects.create(
            name = request.POST.get('name',""),
            email = request.POST.get('email'),
            phone = request.POST.get('phone', 9638527410),
            check_in = request.POST.get('check_in'),
            check_out = request.POST.get('check_out'),
            adult = request.POST.get('adult', 1),
            child = request.POST.get('child', 1),
            room_type = request.POST.get('room_type'), 
            description = request.POST.get('description', "")
            )
        messages.success(request, 'Your room booked successfully!')
        return render(request, 'booking.html', context={'index':booking, 'message': "Your room booked successfully!"})

    context = {
        "bookings" : Booking.objects.all().count(),
        "rooms" : Room.objects.all().count(),
        "staffs" : staff.objects.all().count()
    }
    return render(request, 'booking.html', context)

def contact(request):
    context = {
        "bookings" : Booking.objects.all().count(),
        "rooms" : Room.objects.all().count(),
        "staffs" : staff.objects.all().count()
    }
    return render(request, 'contact.html', context)

def service(request):
    context = {
        "bookings" : Booking.objects.all().count(),
        "rooms" : Room.objects.all().count(),
        "staffs" : staff.objects.all().count()
    }
    return render(request, 'service.html', context)

def team(request):
    context = {
        "bookings" : Booking.objects.all().count(),
        "rooms" : Room.objects.all().count(),
        "staffs" : staff.objects.all().count(),
        "all_team" : staff.objects.all()
    }
    return render(request, 'team.html', context)

def testimonials(request):
    context = {
        "bookings" : Booking.objects.all().count(),
        "rooms" : Room.objects.all().count(),
        "staffs" : staff.objects.all().count()
    }
    return render(request, 'testimonial.html', context)

def about(request):
    context = {
        "bookings" : Booking.objects.all().count(),
        "rooms" : Room.objects.all().count(),
        "staffs" : staff.objects.all().count()
    }
    return render(request, 'about.html', context)

def news_letter(request):
    letter = News_Letter.objects.create(
        email = request.POST.get('email')
        )
    messages.success(request, 'Subscribed successfully!')
    refer = request.META.get('HTTP_REFERER')
    if refer:
        parsed_url = urlparse(refer)
        return redirect(parsed_url.path)
    return render(request, 'index.html')