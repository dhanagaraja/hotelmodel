from django.contrib import admin
from .models import Room, Booking, staff, News_Letter

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['type', 'number', 'floor', 'occupied']
    fields = ['type', 'number', 'floor', 'occupied']
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'check_in', 'check_out']
    fields = ['name', 'email', 'phone', 'check_in', 'check_out', 'room_type', 'description']
    
@admin.register(staff)
class staffAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email', 'phone', 'designation', 'image']
    fields = ['name', 'age', 'email', 'phone', 'designation', 'image']

@admin.register(News_Letter)
class NewsLetterAdmin(admin.ModelAdmin):
    fields = ['email']