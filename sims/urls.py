from django.urls import path
from .views import *


app_name = "sims"
urlpatterns = [
    path('', FlowListView.as_view(), name='flow-list'),
    path('create/', FlowCreateView.as_view(), name='flow-create'),
    path('<int:pk>/update/', FlowUpdateView.as_view(), name='flow-update'),
    path('<int:pk>/delete/', FlowDeleteView.as_view(), name='flow-delete'),
    path('<int:pk>/', FlowDetailView.as_view(), name='flow-detail'),
    path('<int:pk>/graph/', FlowGraphView.as_view(), name='flow-graph')
]
