from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import User

# Create your models here.
class CustomManager(models.Manager):
    def Eng_list(self):
        return self.filter(language__exact="english")
    def Hin_list(self):
        return self.filter(language__exact="hindi")
    def Mar_list(self):
        return self.filter(language__exact="marathi")
    def sou_list(self):
        return self.filter(language__exact="south Indian")
    

class Movie1(models.Model):
    movie_id=models.IntegerField(primary_key=True)
    movie_name=models.CharField(max_length=100)
    movie_type=models.CharField(max_length=75)
    certificate=(("U/A","U/A"),("18+","18+"))
    movie_certificate=models.CharField(max_length = 25,choices = certificate)
    lang =(("hindi","hindi"),("english","english"),("marathi","marathi"),("south Indian","south Indian"))
    language=models.CharField(max_length=100,choices = lang)
    duration=models.CharField(max_length=25)
    director=models.CharField(max_length=200)
    cast=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to ="pics")
    youtube_link=models.URLField(blank=True,null=True)
    
    mov = CustomManager()
    objects=models.Manager()

# class Seat(models.Model):
#     Movie = models.ForeignKey(Movie1, on_delete=models.CASCADE)
#     seat_Booked= models.CharField(max_length=5)
#     date = models.PositiveIntegerField()
#     time=models.IntegerField()
#     is_booked = models.BooleanField(default=False)
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie1, on_delete=models.CASCADE)
    selected_seats = models.CharField(max_length=100)  # Adjust the max_length as needed
    selected_date = models.DateField()
    selected_time = models.TimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2) 
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.movie.movie_name} - {self.selected_date}"