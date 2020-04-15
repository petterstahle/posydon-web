"""These are the definitions of the models (as classes) for the objects stored in the database.
Currently contains the Flow object."""

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
