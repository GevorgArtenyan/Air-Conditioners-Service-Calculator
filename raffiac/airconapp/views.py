from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import ACServiceCalc, Model, Brand
from .forms import ACServiceCalcForm

class ACServiceCalcListView(ListView):
    model = ACServiceCalc
    context_object_name = 'calcs'


class ACServiceCalcCreateView(CreateView):
    model = ACServiceCalc
    form_class = ACServiceCalcForm
    success_url = reverse_lazy('calc_list')


class ACServiceCalcUpdateView(UpdateView):
    model = ACServiceCalc
    form_class = ACServiceCalcForm
    success_url = reverse_lazy('calc_list')


def load_models(request):
    brand_id = request.GET.get('brand')
    models = Model.objects.filter(brand_id=brand_id).order_by('name')
    return render(request, 'airconapp/model_dropdown_list_options.html', {'models': models})