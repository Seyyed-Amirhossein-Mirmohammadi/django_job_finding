from django.db import models



class Employer(models.Model):
    name = models.CharField(null=True, blank=True,max_length=150)
    company = models.CharField(null=True, blank=True,max_length=150)
    adress = models.CharField(null=True, blank=True,max_length=250)
    code_posti = models.CharField(null=True, blank=True, max_length= 250)
    date = models.DateField(null=True, blank=True)
    ph_number = models.CharField(null=True, blank=True,max_length=150)
    job = models.CharField(null=True, blank=True,max_length=150)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('No diffrence', 'No_diffrence')
    )
    gender = models.CharField(max_length=20 ,choices=GENDER_CHOICES, default= None)
    def __str__(self):
        return  self.name




