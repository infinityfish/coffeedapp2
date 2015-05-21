# Create your views here.
# from django.shortcuts import render
from django.views.generic.base import TemplateView
# from django.http import HttpResponse
# Create your views here.

# def TestView(request, **kwargs):
# 	return HttpResponse("Hello 237SPACES")

class LandingView(TemplateView):
	template_name = "base/index.html"
