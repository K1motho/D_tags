from django.shortcuts import render
import datetime
from.models import Blog
import markdown
from django.utils.safestring import mark_safe

# Create your views here.
def index(request):
    return render(request, 'index.html',{"x":"welcome to django"})

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def filter_demo(request):
        context = {
             "my_string" : 'Hello WORLD!',
             "my_date": datetime.date(2025,6,18),
             "long_str": "Here's a clean and professional Contact section you can use on a website or project.",
             "defuser" : "",
             "example": 'foreign',
              'quote': "The first line.\nAnd this is the second line.\nThird one here.",
              'fruits': ['apple', 'banana', 'cherry']
        }
        return render(request, "filters.html", context)

def signup(request):
     return render(request, 'signup.html')
def login(request):
     return render(request, 'login.html')

def blog_list(request):
     blogs = Blog.objects.prefetch_related('editors').all()
     for blog in blogs:
          blog.rendered_text = mark_safe(markdown.markdown(blog.text))
     return render(request ,'blog_list.html', {'blogs': blogs})