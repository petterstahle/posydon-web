from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse
from django.urls import reverse_lazy
from django.template.loader import get_template
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    View
)
from .models import Flow
from .forms import FlowForm
from .graph.genGraph import genGraph

# Create your views here.
#these are class based views. Django recommends these.

class FlowCreateView(CreateView):
    """Used to create a new flow. Called when requesting /sims/create/ url."""
    model = Flow
    # form_class = FlowForm
    template_name = 'flows/flow_create.html'
    fields = ['title', 'content', 'comment']
    # success_url = 'success'

class FlowDetailView(DetailView):
    """Used to display details of a flow."""
    template_name = 'flows/flow_detail.html'
    model = Flow

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class FlowListView(ListView):
    """Used to list al flows with their title, and primary key
    Called when requesting /sims/,
    Returns flow_list.html template"""
    template_name = 'flows/flow_list.html'
    queryset = Flow.objects.all()

class FlowUpdateView(UpdateView):
    model = Flow
    fields = ['title', 'content', 'comment']
    template_name = 'flows/flow_update.html'

class FlowDeleteView(DeleteView):
    model = Flow
    template_name = 'flows/flow_delete.html'
    success_url = reverse_lazy('sims:flow-list')



class FlowGraphView(View):
    """When /sims/<id>/graph url is requested, this view generates an image of the flow graph with the flow primary key as id.
    by default, it displays .png file
    options: download, change format to pdf
    The location of generated files is in /sims/graph/outputs"""
    def get(self, request, *args, **kwargs):
        #get the flow object from database
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Flow, pk=pk)
        flow = obj.content
        title = obj.title

        #PARAMS
        #get format for image
        #default is png, other choice is pdf
        format = request.GET.get('format')
        if format != 'pdf':
            format = 'png'
        #if user want to download file as attachment
        dl = False
        if (request.GET.get("download")):
            dl = True

        #generate image using the genGraph method
        render_path = './sims/graph/outputs/'
        genGraph(flow=flow, title=title, path=render_path, format=format)
        full_path = render_path + title + '.' + format

        response = FileResponse(open(full_path, 'rb'), as_attachment = dl)
        return response
