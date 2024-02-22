from django.contrib import admin
from .models import Movie1,Booking

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=["movie_id","movie_name","movie_type","movie_certificate","language","duration","director","cast","description","image","youtube_link"]

admin.site.register(Movie1,MovieAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'selected_date', 'selected_time', 'total_price','selected_seats','is_booked',)
    list_filter = ('selected_date', 'selected_time')
    search_fields = ('user__username', 'movie__name')
admin.site.register(Booking,BookingAdmin)