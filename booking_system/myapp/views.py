from django.shortcuts import render, redirect
from .models import Building, Room, Booking
from .forms import BookingForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def book(request):
    buildings = Building.objects.all()
    
    return render(request, 'myapp/book.html', {'buildings': buildings})

def book_building(request, id_building):
    first_name = request.user.first_name
    buildings = Building.objects.all()
    rooms = Room.objects.filter(building_id=id_building)

   
    context = {
        'first_name': first_name, 
        'buildings': buildings,
        'id_building': id_building,
        'rooms': rooms
    }
    return render(request, 'myapp/book.html', context)

def book_room(request, id_building):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            room_id = form.cleaned_data['room']
            start_date = form.cleaned_data['start_date']
            start_hour = form.cleaned_data['start_hour']
            end_hour = form.cleaned_data['end_hour']


            # Create a new Booking object and save it to the database
            booking = Booking(
                user=request.user,  # Assuming the user is logged in
                room=room_id,
                start_date=start_date,
                start_hour=start_hour,
                end_hour=end_hour
            )
            booking.save()

            # Redirect to a success page or home page
            messages.success(request, ("Booking seccessful"))
            return render(request, 'myapp/manage_booking.html')
        else:
            messages.success(request, ("There was an error Booking, Try again!"))
            return redirect('/book')
   
    else:
        return render(request, 'myapp/manage_booking.html')

def manage_booking(request):
    user_id = request.user.id
    bookings = Room.objects.filter(id=user_id)

    return render(request, 'myapp/manage_booking.html', {"bookings":bookings})


def contact(request):
    return render(request, 'myapp/contact.html')

def about(request):
    return render(request, 'myapp/about.html')

