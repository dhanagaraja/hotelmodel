from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinLengthValidator

# Create your models here.
   
class Booking(models.Model):
    TYPES = (('Junior Suite', 'Junior Suite'), ('Executive Suite', 'Executive Suite'), ('Super Deluxe', 'Super Deluxe'))
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(_('Name'), max_length=255)
    email = models.EmailField(_('Email'), max_length=255)
    phone = models.IntegerField(_('Phone'), null=True)
    check_in = models.DateField(_('Check In'))
    check_out = models.DateField(_('Check Out'))
    adult = models.IntegerField(_('Adult'), null=True)
    child = models.IntegerField(_('Child'), null=True)
    room_type = models.CharField(_('Type'), choices=TYPES, max_length=25)
    description = models.TextField(_('Description'), null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'booking'
        verbose_name = _('Booking')
        verbose_name_plural = _('Bookings')
        ordering = ('id',)

class Room(models.Model):
    TYPES = (('Junior Suite', 'Junior Suite'), ('Executive Suite', 'Executive Suite'), ('Super Deluxe', 'Super Deluxe'))
    type = models.CharField(_('Type'), choices=TYPES, max_length=25)
    number = models.IntegerField(_('Number'), null=True)
    floor = models.IntegerField(_('Floor'), null=True)
    occupied= models.ForeignKey(Booking, verbose_name=_("bookings"), on_delete=models.CASCADE, null=True)
    
    # def __str__(self):
    #     return self.number
    
    class Meta:
        db_table = 'room'
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')
        ordering = ('number',)

class staff(models.Model):
    TYPES = (('Manager', 'Manager'), ('Executive', 'Executive'), ('Staff', 'Staff'), ('Cook', 'Cook'))
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(_('Name'), max_length=255)
    age = models.IntegerField(_('Age'))
    phone = models.IntegerField(_('Phone'), null=True)
    email = models.EmailField(_('Email'), null=True)
    designation = models.CharField(_('Type'), choices=TYPES, max_length=25, default='Staff')
    image = models.ImageField(_('Photo'), default='media/default.jpg', upload_to='media/')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'staff'
        verbose_name = _('Staff')
        verbose_name_plural = _('Staffs')
        ordering = ('id',)

class News_Letter(models.Model):
    email = models.EmailField(_('Email'))
    
    def __str__(self) -> str:
        return self.email
    
    class Meta:
        db_table = 'news_letter'
        verbose_name = _('News Letter')
        verbose_name_plural = _('News Letters')