
"""event_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.first, name='first'),
    path('index',views.index, name='index'),
    path('reg/addreg',views.addreg, name='addreg'),
    path('reg/',views.reg, name='reg'),
    path('prgmss/',views.prgmss, name='prgmss'),
    path('login/',views.login, name='login'),
    path('login/logint',views.logint, name='logint'),
    path('logout/',views.logout, name='logout'),
    path('addprogram', views.addprogram, name='addprogram'),
    path('addevent', views.addevent, name='addevent'),
    path('addfeedback', views.addfeedback, name='addfeedback'),
    path('viewfeedback', views.viewfeedback, name='viewfeedback'),
    path('viewuser/', views.viewuser, name='viewuser'),
    path('viewevents/', views.viewevents, name='viewevents'),
    path('book/<int:program_id>/', views.book_event, name='book_event'),
    path('books', views.books, name='books'),
    path('viewbooking', views.viewbooking, name='viewbooking'),
    path('approve_booking/<int:booking_id>/', views.approve_booking, name='approve_booking'),
    path('reject_booking/<int:booking_id>/', views.reject_booking, name='reject_booking'),
    path('books', views.books, name='books'),
    path('viewprogm/', views.viewprogm, name='viewprogm'),
    path('viewadmin', views.viewadmin, name='viewadmin'),
    path('update_event/<int:event_id>/', views.update_event, name='update_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('vieworganizer', views.vieworganizer, name='vieworganizer'),
    path('update_organizer/<int:organizer_id>/', views.update_organizer, name='update_organizer'),
    path('delete_organizer/<int:organizer_id>/', views.delete_organizer, name='delete_organizer'),
  
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
