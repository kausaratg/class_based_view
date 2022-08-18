from django.shortcuts import render
from django.views.generic import View, TemplateView,  ListView, DetailView, CreateView, UpdateView, DeleteView
from basic_app import models

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school.html'



class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    


