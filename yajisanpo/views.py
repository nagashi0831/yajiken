from django.shortcuts import render
from django.views import generic
from yajisanpo.models import StoreType, Log

class TopView(generic.ListView):
    template_name = 'yajisanpo/top.html'
    context_object_name = "search_log"
    queryset = Log.objects.all()
# Create your views here.
