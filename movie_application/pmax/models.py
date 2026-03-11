from django.db import models
# user database 
class User(models.Model):
    username=models.CharField(max_length=200,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=200)

    def __str__(self):
        return self.username


# movie database 
class Movie(models.Model):
    name=models.CharField(max_length=200)
    language=models.CharField(max_length=100)
    duration=models.PositiveBigIntegerField()
    image=models.ImageField(upload_to="movie/")

    def __str__(self):
        return self.name
    

#theatre database 
class Theatre(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name

   
# show database to determine which theatre is providing the number of shows 
class Show(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE) # one to one relation ship connected to movie table 
    theatre=models.ForeignKey(Theatre,on_delete=models.CASCADE) # one to one relation ship connected to theathre  table
    show_time=models.TimeField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available_seats=models.IntegerField()
    
    def __str__(self):
        return f"{self.movie.name} - {self.theatre.name}"


#review databse    
class Review(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    rating=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True) # automatically stores the date and time if not added then have to give it manually 
    
    def __str__(self):
        return self.user.username


class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    show=models.ForeignKey(Show,on_delete=models.CASCADE)
    seats=models.CharField(max_length=100)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    booking_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked"



    



