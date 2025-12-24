

from django.contrib import messages
from datetime import date

from .models import *
from .forms import CustomerForm, LoginForm, ProgramForm, EventForm, FeedbackForm


def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')



from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect,get_object_or_404
from django.core.files.storage import FileSystemStorage

from .models import *
from decimal import Decimal
from django.db.models import F, Sum

from django.db import transaction
from django.http import HttpResponseServerError

def first(request):
    return render(request,'index.html')
     
    
def index(request):
    return render(request,'index.html')

def reg(request):
    form = CustomerForm()
    return render(request, 'register.html', {'form': form})


def addreg(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('index')
    else:
        form = CustomerForm()
    return render(request, 'register.html', {'form': form})    


def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logint(request):
    email = request. POST.get('email')
    password = request.POST.get('password')
   # print("\n\n\n\n\n\n",email,password)
    if email == 'admin@gmail.com' and password == 'admin':
        request.session['logintdetail'] = email
        request.session['logint'] = 'admin'
        messages.success(request, 'Admin login successful!')
        return redirect('index')

    elif Customer_Details.objects.filter(email=email,password=password).exists():
        userdetails=Customer_Details.objects.get(email=request.POST['email'], password=password)
        #print("hello")
        if userdetails.password == request.POST['password']:
            request.session['uid'] = userdetails.id
            messages.success(request, 'User login successful!')
            return redirect('index')

    elif event.objects.filter(email=email,password=password).exists():
        ups=event.objects.get(email=email,password=password)
        request.session['s_id']=ups.id
        messages.success(request, 'Event organizer login successful!')
        return redirect('index')

        
    
    else:
        messages.error(request, 'Invalid username or password!')
        return render(request, 'login.html', {'status': 'INVALID USERID OR PASSWORD'})     



def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    messages.success(request, 'Logged out successfully!')
    return redirect(first)


def prgmss(request):
    return render(request,'program.html')

def addprogram(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program added successfully!')
            return redirect('index')
    else:
        form = ProgramForm()
    today = date.today()
    return render(request, 'program.html', {'form': form, 'today': today})


def events(request):
    return render(request,'event.html')

def addevent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event organizer added successfully!')
            return redirect('index')
    else:
        form = EventForm()
    return render(request, 'addevent.html', {'form': form})

def addfeedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            if 'uid' in request.session:
                feedback.user_id = request.session['uid']
            feedback.save()
            messages.success(request, 'Feedback added successfully!')
            return redirect('index')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def viewuser(request):
    users = Customer_Details.objects.all()
    return render(request, 'viewuser.html', {'users': users})

def viewevents(request):
    programs = program_tbl.objects.all()
    return render(request, 'viewevents.html', {'programs': programs})


def book_event(request, program_id):
    if request.method == 'POST':
        if 'uid' not in request.session:
            messages.error(request, 'Please log in to book an event.')
            return redirect('login')
        program = get_object_or_404(program_tbl, pk=program_id)
        booking_date = request.POST.get('event_date', program.date)
        booking_tbl.objects.create(
            event_id=str(program_id),
            user_id=str(request.session.get('uid')),
            date=booking_date,
            status='pending'
        )
        messages.success(request, 'Booking created successfully!')
        return redirect('viewevents')
    return redirect('viewevents')

def viewbooking(request):
    # Admin view: show all bookings with event and user info
    bookings = []
    for b in booking_tbl.objects.all():
        # Get event and user objects for display
        try:
            event_obj = program_tbl.objects.get(id=b.event_id)
        except program_tbl.DoesNotExist:
            evee
        try:
            user_obj = Customer_Details.objects.get(id=b.user_id)
        except Customer_Details.DoesNotExist:
            user_obj = None
        bookings.append({
            'id': b.id,
            'event': event_obj,
            'user': user_obj,
            'date': b.date,
            'status': b.status,
        })
    return render(request, 'viewbooking.html', {'bookings': bookings})

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def approve_booking(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(booking_tbl, id=booking_id)
        booking.status = 'approved'
        booking.save()
        messages.success(request, 'Booking approved!')
    return redirect('viewbooking')

@csrf_exempt
def reject_booking(request, booking_id):
    if request.method == 'POST':
        booking = get_object_or_404(booking_tbl, id=booking_id)
        booking.status = 'rejected'
        booking.save()
        messages.success(request, 'Booking rejected!')
    return redirect('viewbooking')




def books(request):
    if 'uid' not in request.session:
        messages.error(request, 'Please log in to view your bookings.')
        return redirect('login')
    sel = booking_tbl.objects.filter(user_id=request.session['uid'])
    bookings = []
    for b in sel:
        try:
            event_obj = program_tbl.objects.get(id=b.event_id)
        except program_tbl.DoesNotExist:
            event_obj = None
        bookings.append({
            'id': b.id,
            'event': event_obj,
            'date': b.date,
            'status': b.status,
        })
    return render(request, 'books.html', {'bookings': bookings})


def viewfeedback(request):
    feedbacks = []
    for f in feedback_tbl.objects.all():
        try:
            user = Customer_Details.objects.get(id=f.user_id)
            user_name = user.name
        except Customer_Details.DoesNotExist:
            user_name = f.user_id
        feedbacks.append({
            'id': f.id,
            'user_name': user_name,
            'feedback': f.feedback,
        })
    return render(request, 'viewfeedback.html', {'feedbacks': feedbacks})



def viewprogm(request):
    users = program_tbl.objects.all()
    return render(request, 'viewprogm.html', {'users': users})


def vieworganizer(request):
    organizers = event.objects.all()
    return render(request, 'vieworganizer.html', {'organizers': organizers})

def update_organizer(request, organizer_id):
    organizer = get_object_or_404(event, id=organizer_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=organizer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Organizer updated successfully!')
            return redirect('vieworganizer')
    else:
        form = EventForm(instance=organizer)
    return render(request, 'addevent.html', {'form': form, 'update': True, 'organizer_id': organizer_id})

def delete_organizer(request, organizer_id):
    organizer = get_object_or_404(event, id=organizer_id)
    organizer.delete()
    messages.success(request, 'Organizer deleted successfully!')
    return redirect('vieworganizer')
def viewadmin(request):
    events = event.objects.all()
    return render(request, 'viewadmin.html', {'events': events})

from django.shortcuts import redirect

def update_event(request, event_id):
    ev = get_object_or_404(event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=ev)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('viewadmin')
    else:
        form = EventForm(instance=ev)
    return render(request, 'addevent.html', {'form': form, 'update': True, 'event_id': event_id})

def delete_event(request, event_id):
    ev = get_object_or_404(event, id=event_id)
    ev.delete()
    messages.success(request, 'Event deleted successfully!')
    return redirect('viewadmin')