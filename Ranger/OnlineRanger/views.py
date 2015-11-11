# Create your views here.
from django.shortcuts import render_to_response

from blog.models import posts

def home(request):
        content = {
                'title' : 'My First Post',
                'author' : 'Althaf',
                'date' : '12th of Nov 2015',
                'body' : 'this is the test message............'
        }
        return render_to_response('index.html', content)
