from django.shortcuts import render,redirect,get_object_or_404
from .models import Movie1,Booking
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from .form import RegistrationForm
from django.http import JsonResponse
import uuid
from django.conf import settings
import random
import razorpay

# Create your views here.
def indexx(req):
    movies = Movie1.objects.all()
    context = {}
    context['movie'] = movies
    return render(req,"indexx.html",context)

def Mdetails(req,pid):
    movies=Movie1.objects.get(movie_id = pid)
    context={'movie':movies}
    return render(req,"details.html",context)

def about(req):
    return render(req,"about.html")

def engList(req):
    queryset =Movie1.mov.Eng_list()
    print(queryset)
    context= {'movie':queryset}
    return render(req,"indexx.html",context)

def hinList(req):
    queryset =Movie1.mov.Hin_list()
    print(queryset)
    context= {'movie':queryset}
    return render(req,"indexx.html",context)

def marList(req):
    queryset =Movie1.mov.Mar_list()
    print(queryset)
    context= {'movie':queryset}
    return render(req,"indexx.html",context)

def souList(req):
    queryset =Movie1.mov.sou_list()
    print(queryset)
    context= {'movie':queryset}
    return render(req,"indexx.html",context)

def register(req):
    form = RegistrationForm()
    if req.method == "POST":
        form = RegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,("User Created Successfully"))
            return redirect("/login")
        else:
            messages.error(req,"Incorrect Password Format")
    context = {'form':form}
    return render(req,"register.html",context)

def login(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        user = authenticate(req,username=username,password=password)
        if user is not None:
            auth_login(req, user)
            messages.success(req,("You have been logged in!!"))
            return redirect("/")
        else:
            messages.error(req,"Incorrect Username or Password")
            return redirect("/login")
    else:
        return render(req,"login.html")
    
def logout_user(req):
    logout(req)
    messages.success(req,("You have logged out Successfully"))
    return redirect("/")


def booknow(req,pid):
    if req.user.is_authenticated:
        movie = get_object_or_404(Movie1, movie_id=pid)
        # available_seats = Seat.objects.create(Movie=movie, is_booked=False)
        if req.method == 'POST':
            print(req.method)
            selected_seats = req.POST.get('selected_seats')  # Assuming 'seat' is the name of the seat selection input
            selected_date = req.POST.get('selected_date')  # Assuming 'date' is the name of the date selection input
            selected_time = req.POST.get('selected_time')  # Assuming 'time' is the name of the time selection input
            print(selected_seats,selected_date,selected_time)
            # Process the selected seats, date, and time as needed
            total_price = len(selected_seats) * 100  # Assuming each seat costs $10
            print(total_price)

            booking = Booking.objects.create(
            user=req.user,
            movie=movie,
            selected_seats=selected_seats,
            selected_date=selected_date,
            selected_time=selected_time,
            total_price=total_price
            )
            return render(req,"payment_gateway.html",{
                'movie': movie,
                #  'available_seats': available_seats,
                'selected_seats': selected_seats,
                'selected_date': selected_date,
                'selected_time': selected_time,
                'total_price': total_price,
                })
                          
            
        else:
           print(req.method)
           return render(req, 'booknow.html', {'movie': movie})
    else:
        return redirect("/login")
    
def payment_form(req):
    return render(req,'payment_form.html')

client = razorpay.Client(auth=("rzp_test_tpO74EdCcW0Zok", "OtjOc1GIQnDyCNE9jvFccCrg"))
def payment_gateway(req):
#     movies = Booking.objects.filter(user=req.user, is_booked=False) 
    
#     # Calculate total price for all selected seats in these movies
#     total_price = 0
#     price_per_seat= 100
#     for movie in movies:
#         # total_price= (movie.total_price * movie.selected_seats)
#         total_price += (movie.price_per_seat * movie.selected_seats)
#         oid = str(movie.movie)  # Assuming movie_id is the order ID
#         print(total_price)
#         print(oid)
    
#     # Create Razorpay client
#     client = razorpay.Client(auth=("rzp_test_tpO74EdCcW0Zok", "OtjOc1GIQnDyCNE9jvFccCrg"))
    
#     # Create data for Razorpay order
#     data = {
#         "amount": total_price * 100,  # Amount should be in paisa (Indian currency)
#         "currency": "INR",
#         "receipt": str(oid)  # Convert OID to string for receipt
#     }
    
#     # Create Razorpay order
#     payment = client.order.create(data=data)
#     print(payment)
    
#     # Prepare context data
#     context = {
#         'data': payment,
#         'amount': payment["amount"]
#     }
    
#     return render(req, 'payment_gateway.html', context)
  movies = Booking.objects.filter(user=req.user, is_booked=False)
  total_price = 0
  oid_list = []  # List to store order IDs
    
  for movie in movies:
        total_price += (movie.price_per_seat * movie.selected_seats)
        oid_list.append(str(movie.movie))  # Append each movie's ID to the list
        
  total_price *= 100  # Convert to smallest currency unit
    
    # Create data for Razorpay order
  data = {
        "amount": total_price,
        "currency": "INR",
        "receipt": ", ".join(oid_list)  # Convert list of OIDs to string for receipt
    }
    
  try:
        # Create Razorpay order
        payment = client.order.create(data=data)
        print(payment)
        
        # Prepare context data
        context = {
            'data': payment,
            'amount': payment["amount"]
        }
        
        return render(req, 'payment_gateway.html', context)
  except Exception as e:
        # Handle any errors gracefully
        print(f"Error creating Razorpay order: {e}")
        return render(req, 'error_page.html', {'error': e})