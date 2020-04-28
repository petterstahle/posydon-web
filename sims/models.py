"""These are the definitions of the models (as classes) for the objects stored in the database.
Currently contains the Flow object, and SimProp object is being implemented."""

from django.db import models
from django.urls import reverse

# Create your models here.

class Flow(models.Model):
    """Model representing a simulation flow.
    The flow itself is stored in the 'content' field, as a dictionary (see genGraph.py).
    The rest is metadata, and includes: title, date of creation, comment field."""

    #title: title to document the flow (ex. "flow1", "bob's flow",etc...)
    title = models.CharField(max_length=30)

    #time: time of creation
    date = models.DateField(auto_now=True),

    #comment: possibility for the user to add a comment about the flow (Not Required)
    comment = models.TextField(blank = True, default = '')

    #content: this is where the flow is described
    content = models.TextField(default='')

    def get_absolute_url(self):
        """Returns the url to access a particular flow instance."""
        return reverse('sims:flow-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class SimProp(models.Model):
    #title: title to document the flow (ex. "flow1", "bob's flow",etc...)
    title = models.CharField(max_length=30)

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
    mesa_phi = models.DecimalField(null=True,blank=True,max_digits=6,decimal_places=3) #add validator 0<x<2pi
    mesa_cos_theta = models.DecimalField(null=True,blank=True,max_digits=6,decimal_places=3) #add validator -1<x<1
    mesa_mean_anomaly = models.DecimalField(null=True,blank=True,max_digits=6,decimal_places=3) #add validator 0<x<2pi
    mesa_mass_central_BH = models.DecimalField(null=True,blank=True,max_digits=6,decimal_places=3) #add validator >0
    mesa_neutrino_mass_loss_fraction = models.DecimalField(max_digits=6,decimal_places=3) #add validator 0<x<1
    mesa_neutrino_AM_loss = models.BooleanField()
    mesa_PISN = models.CharField(max_length=20,blank=True,default='None')#add choises of number or string 'Marchant+19'
    mesa_log_scale = models.BooleanField()
    mesa_verbose = models.BooleanField()

    #additional args
    #step_end
    step_end = models.CharField(max_length=20,default='end', blank=True)
    max_time = models.FloatField()

    def get_absolute_url(self):
        """Returns the url to access a particular simprop instance."""
        return reverse('sims:sim_prop-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title
