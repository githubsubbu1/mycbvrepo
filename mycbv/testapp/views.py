from django.shortcuts import render
from.models import  Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

class CompanyListView(ListView):
    model=Company

class CompanyDetailView(DetailView):
    model=Company
class CompanyCreateView(CreateView):
    model=Company
    fields='__all__'
class CompanyUpdateView(UpdateView):
    model=Company
    fields = ('name','ceo')

class CompanyDeleteView(DeleteView):
    model=Company
    success_url =reverse_lazy('companies')