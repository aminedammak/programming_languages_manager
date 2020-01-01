from django.shortcuts import render
from .serializers import LanguageSerializer, ParadigmSerializer
from .models import Language, Paradigm
from rest_framework import viewsets


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

