## Create View
# blog/views.py
# Define the views for the blog app:
#from django.shortcuts import render
from .models import *
from django.views.generic import ListView #ListView is a custom component which displays a list of the model

#class-based view
class ShowAllView(ListView):
    '''Create a subclass of ListView to display all blog articles.'''
    model = Article # retrieve objects of type Article from the database
    template_name = 'blog/show_all.html'
    context_object_name = 'articles' # how to find the data in the template file (context variable)
