#django specific
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.template.loader import get_template
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    View
)
#models & forms
from .models import Flow, SimProp
from .forms import FlowForm, SlurmForm
#custom functions
from .graph.genGraph import genGraph
from .properties.genScript import genScript
from .evolve.manage_job import run_sim

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
    """When /sims/<id>/graph url is requested, this view generates an image of the flow graph with the flow from a given SimProp object.
    By default, it displays .png file
    options: download, change format to pdf
    The location of generated files is in /sims/graph/outputs"""
    def get(self, request, *args, **kwargs):
        #get the flow object from database
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(SimProp, pk=pk)
        flow = obj.flow
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

        #get additionnal info for step_default options
        options = {
            'cosmic_end': obj.cosmic_end
        }

        #generate image using the genGraph method
        render_path = './sims/graph/outputs/'
        genGraph(flow=flow, title=title, path=render_path, format=format, **options)
        full_path = render_path + title + '.' + format

        response = FileResponse(open(full_path, 'rb'), as_attachment = dl)
        return response


class SimPropCreateView(CreateView):
    """Used to create a new Simulation Properties object. Called when requesting /sims/props/create/ url."""
    model = SimProp
    # form_class = FlowForm
    template_name = 'sim_props/sim_prop_create.html'
    fields = ['title', 'metallicity', 'flow', 'cosmic_end', 'cosmic_evolve_dict', 'mesa_mechanism', 'mesa_sigma_kick', 'mesa_mass_central_BH', 'mesa_neutrino_mass_loss', 'mesa_PISN', 'mesa_log_scale', 'mesa_verbose', 'step_end', 'max_time']


class SimPropListView(ListView):
    """Used to list al sim. props. with their title, and primary key
    Called when requesting /sims/props,
    Returns sim_prop_list.html template"""
    template_name = 'sim_props/sim_prop_list.html'
    queryset = SimProp.objects.all()


class SimPropUpdateView(UpdateView):
    model = SimProp
    fields = ['title', 'metallicity', 'flow', 'cosmic_end', 'cosmic_evolve_dict', 'mesa_mechanism', 'mesa_sigma_kick', 'mesa_mass_central_BH', 'mesa_neutrino_mass_loss', 'mesa_PISN', 'mesa_log_scale', 'mesa_verbose', 'step_end', 'max_time']
    template_name = 'sim_props/sim_prop_update.html'

class SimPropDeleteView(DeleteView):
    model = SimProp
    template_name = 'sim_props/sim_prop_delete.html'
    success_url = reverse_lazy('sims:sim_prop-list')


class SimScriptView(View):
    def generateScript(pk):
        obj = get_object_or_404(SimProp, pk=pk)
        #generate simulation script
        filename = obj.title+'.py'
        filepath = './sims/properties/outputs/' + filename
        genScript(obj,filepath)

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        generateScript(pk)
        response = FileResponse(open(filepath, 'rb'), as_attachment = True)
        return response


class SimPropDetailView(DetailView):
    """Used to display details of a simulation properties object."""
    template_name = 'sim_props/sim_prop_detail.html'
    model = SimProp
    # form_class = SlurmForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SimEvolView(View):
    # form_class = SlurmForm
    # template_name = 'sim_props/sim_prop_detail.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        SimScriptView.generateScript(pk) #generate script (uses code from SimScriptView)
        run_sim('petter.stahle@etu.unige.ch', 'Test') #execute script

        return HttpResponseRedirect(reverse('sims:sim_evolve-success', kwargs={'pk': pk}))


    #
    # def post(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     SimScriptView.generateScript(pk) #generate script (uses code from SimScriptView)
    #     form = self.form_class(request.POST)
    #
    #     #debug
    #     print(form.is_valid())
    #
    #     if form.is_valid():
    #         email = form.cleaned_data('email')
    #
    #         ## DEBUG:
    #         print(email)
    #         # run_sim(email)
    #         return HttpResponseRedirect(reverse('sims:sim_evolve-success', kwargs={'pk': pk}))
    #         # return HttpResponseRedirect(reverse('sims:sim_prop-detail', kwargs={'pk': pk}))
    #
    #     # return HttpResponseRedirect(reverse('sims:sim_prop-detail', kwargs={'pk': pk}))
    #     return render(request, 'sim_props/sim_prop_detail.html', {'form': form})


class SimEvolSuccessView(View):
    template_name = 'sim_props/success.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'sim_props/success.html', {})
    # TODO
    #add view logs functionnality
    #add retrieve results functionnality
