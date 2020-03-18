from django.shortcuts import render
from .models import Model, Brand
from rest_framework import generics
from django.core import serializers
from .serializers import ModelSerializer
from django.http import JsonResponse
from .forms import AirConCalc

class ModelAPIListView(generics.ListAPIView):
    lookup_field = 'pk'
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

def json(request):
    model_json = serializers.serialize('json', Model.objects.all())
    data = {'modeljson':model_json}
    return JsonResponse(data)

def home(request):
    brand = Brand.objects.all()
    form = AirConCalc()
    return render(request, 'airconapp/home.html', {"brand":brand, "form":form})


def result(request):
    return render(request, 'airconapp/result.html')