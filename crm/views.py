from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Agent, Campaign, CampaignResult
from .serializers import AgentSerializer, CampaignSerializer, CampaignResultSerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'language']

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['status']

class CampaignResultViewSet(viewsets.ModelViewSet):
    queryset = CampaignResult.objects.all()
    serializer_class = CampaignResultSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'outcome']
