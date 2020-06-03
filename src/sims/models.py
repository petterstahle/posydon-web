"""
Module Models
=============

These are the definitions of the models (as classes) for the objects stored in the database.
Contains the SimProp model."""

from django.db import models
from django.urls import reverse

# Create your models here.

class SimProp(models.Model):
    """Django database model representing a set of simulation properties for a given simulation. An instance of this model class will be given a primary key, which will serve as its unique identifier for simulations.
    """

    #title: title to document the flow (ex. "flow1", "bob's flow",etc...)
    title = models.CharField(max_length=30)

    metallicity = models.FloatField(default=0) #add validator 0<x<1

    #flow is like content described in Flow Object
    flow = models.TextField(default='')

    #step_cosmic args
    cosmic_end = models.CharField(max_length=20, choices=[('PostSN', 'PostSN'),('CO+He', 'CO+He')])
    cosmic_evolve_dict = models.TextField(default='')

    #step_mesa args
    mech_choices = [
        ('Fryer+12-rapid','Fryer+12-rapid'),
        ('Fryer+12-delayed','Fryer+12-delayed'),
        ('Fryer+12-delayed-full_kicks','Fryer+12-delayed-full_kicks'),
        ('direct','direct'),
        ('Sukhbold+16-N20-engine','Sukhbold+16-N20-engine')]
    mesa_mechanism = models.CharField(max_length=40,choices=mech_choices)
    mesa_sigma_kick = models.DecimalField(max_digits=6,decimal_places=3) #add validator >0
    mesa_mass_central_BH = models.DecimalField(null=True,blank=True,max_digits=6,decimal_places=3) #add validator >0
    mesa_neutrino_mass_loss = models.DecimalField(max_digits=6,decimal_places=3) #add validator 0<x<1
    mesa_PISN = models.CharField(max_length=20,blank=True,default='None')#add choises of number or string 'Marchant+19'
    mesa_log_scale = models.BooleanField()
    mesa_verbose = models.BooleanField()

    #additional args
    #step_end
    step_end = models.CharField(max_length=20,default='end', blank=True)
    max_time = models.FloatField(default=0)

    def get_absolute_url(self):
        """Returns the url to access a particular simprop instance."""
        return reverse('sims:sim_prop-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title
