from django.urls import path
from .views import *


app_name = "sims"
urlpatterns = [
    #sim_props
    #list
    path('', SimPropListView.as_view(), name='sim_prop-list'),
    #create
    path('create/', SimPropCreateView.as_view(), name='sim_prop-create'),
    #update
    path('<int:pk>/update/', SimPropUpdateView.as_view(), name='sim_prop-update'),
    #delete
    path('<int:pk>/delete/', SimPropDeleteView.as_view(), name='sim_prop-delete'),
    #detail
    path('<int:pk>/', SimPropDetailView.as_view(), name='sim_prop-detail'),
    #handle graph
    path('<int:pk>/graph/', SimPropGraphView.as_view(), name='sim_prop-graph'),
    #generate evolution script
    path('<int:pk>/download-script/', SimScriptView.as_view(), name='sim_script-dl'),
    #send and run evolution script on cluster
    path('<int:pk>/evolve/', SimEvolView.as_view(), name='sim-evolve'),
    #results page - get logs and results from evolution
    path('<int:pk>/results/', SimResultsView.as_view(), name='sim-results')
]
