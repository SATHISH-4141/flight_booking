from django.db import models

# Create your models here.


class Enrollment(models.Model):
    fname = models.CharField(max_length=30, default=True, null=True)
    lname = models.CharField(max_length=20, default=True, null=True)
    email = models.EmailField(max_length=40, default=True, null=True)
    username = models.CharField(max_length=30,unique=False,null=True)
    mobile_number = models.CharField(max_length=15,default=True, null=True)
    password = models.CharField(max_length=20, default=True, null=True)
    confirm_password = models.CharField(max_length = 20, default=True, null=True) 
    dob = models.DateField(default=True, null=True)
   


    def __str__(self):
        return f'{self.fname},{self.lname},{self.mobile_number},{self.email},{self.password},{self.confirm_password},{self.dob}'


class Searchflight(models.Model):
    departure = models.CharField(max_length=30, default=True, null=True)
    arrival = models.CharField(max_length=30, default=True, null=True)
    date = models.DateField(max_length=30, default=True, null=True)
    return_date = models.DateTimeField(max_length=30, default=True, null=True)
    cabin_class = models.CharField(max_length=30, default=True, null=True)

    def __str__(self):
        return f'{self.departure},{self.arrival},{self.cabin_class}'

class Reservation(models.Model):
    total_no_of_seats = models.IntegerField(default=True, null=True)
    no_of_seats_reserved = models.IntegerField( default=True, null=True)
    week_availability = models.CharField(max_length=30, default=True, null=True)
    flight_numbers = models.IntegerField( default=True, null=True)
    depaturedatetime = models.DateTimeField()
    arrivaldatatime = models.DateTimeField()
    return_datetime = models.DateTimeField(default = True,null=True)
    fare = models.FloatField(default=True)

    def __str__(self):
        return f'{self.total_no_of_seats},{self.no_of_seats_reserved},{self.week_availability},{self.flight_numbers},{self.return_date_time},{self.fare}'

class Myaccount(models.Model):
    fname = models.ForeignKey(Enrollment,related_name = 'Myaccount',on_delete=models.CASCADE)
    lname = models.ForeignKey(Enrollment,max_length=30,related_name = 'lastname',on_delete=models.CASCADE)
    email = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
    sourse = models.ForeignKey(Searchflight,related_name = 'departure_place',max_length=30, on_delete=models.CASCADE)
    destination = models.ForeignKey(Searchflight,related_name='arrival_place', on_delete=models.CASCADE)
    date = models.ForeignKey(Searchflight,related_name='travel_date',on_delete=models.CASCADE)
    amount =models.ForeignKey(Reservation, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.fname},{self.lname},{self.email},{self.sourse},{self.destination},{self.date},{self.amount}'
       

class Flight_status(models.Model):
    flight_number = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    departure_city = models.ForeignKey(Searchflight,related_name='departure_city',on_delete=models.CASCADE)
    arrival_city = models.ForeignKey(Searchflight, on_delete=models.CASCADE)
    status_of_flight = models.CharField(max_length=30, default=True, null=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.flight_number},{self.departure_city},{self.arrival_city},{self.status_of_flight},{self.check_in},{self.check_out}'

class Passengers(models.Model):
    firstname = models.ForeignKey(Enrollment,related_name="enrollment",on_delete=models.CASCADE)
    middlename = models.CharField(max_length=30, default=True, null=True)
    lastname = models.ForeignKey(Enrollment,on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100, default=True, null=True)
    tot_no_of_passengers_onboard = models.IntegerField(default=True, null=True)
    boarding_status = models.CharField(max_length=30, default=True, null=True)
    no_of_passengers_cancelled = models.IntegerField( default=True, null=True)
    departure_from = models.ForeignKey(Searchflight,related_name="searchflight",on_delete=models.CASCADE)
    destinations = models.ForeignKey(Searchflight,related_name="destination", on_delete=models.CASCADE)


    def __str__(self):
         return f'{self.firstname},{self.middlename},{self.lastname},{self.gender},{self.address},{self.tot_no_of_passengers_onboard},{self.boarding_status},{self.no_of_passengers_cancelled},{self.departure_from},{self.destinations}'