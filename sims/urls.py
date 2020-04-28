from django.urls import path
from .views import *


app_name = "sims"
urlpatterns = [
    #flows
    path('', FlowListView.as_view(), name='flow-list'),
    path('create/', FlowCreateView.as_view(), name='flow-create'),
    path('<int:pk>/update/', FlowUpdateView.as_view(), name='flow-update'),
    path('<int:pk>/delete/', FlowDeleteView.as_view(), name='flow-delete'),
    path('<int:pk>/', FlowDetailView.as_view(), name='flow-detail'),
    path('<int:pk>/graph/', FlowGraphView.as_view(), name='flow-graph'),
    #sim_props
    #list
    path('props/', SimPropListView.as_view(), name='sim_prop-list'),
    #create
    path('props/create/', SimPropCreateView.as_view(), name='sim_prop-create'),
    #update
    path('props/<int:pk>/update/', SimPropUpdateView.as_view(), name='sim_prop-update'),
    #delete
    path('props/<int:pk>/delete/', SimPropDeleteView.as_view(), name='sim_prop-delete'),
    #detail
    path('props/<int:pk>/', SimPropDetailView.as_view(), name='sim_prop-detail'),
    #generate properties file
    path('props/<int:pk>/dl/', SimPropGenView.as_view(), name='sim_prop-dl')
]
