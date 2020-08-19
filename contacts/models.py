from django.db import models

class sqlserverconn(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)

    #int kenttä olisi vastaavsti IntegerField(...)
    