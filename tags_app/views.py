from django.shortcuts import render, redirect
import datetime
from.models import Blog, Subscriber
import markdown
from django.utils.safestring import mark_safe
from django.contrib import messages

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

def subscribe(request):
    context = {}

    if request.method == 'POST':
        email = request.POST.get('email')

        if not email:
            messages.error(request, 'Please enter a valid email address.')
            return redirect('subscribe')

        if 'unsubscribe' in request.POST:
            deleted, _ = Subscriber.objects.filter(email=email).delete()
            if deleted:
                messages.success(request, f'{email} has been unsubscribed.')
            else:
                messages.info(request, f'{email} was not found in our list.')
            return redirect('subscribe')

        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
            context['existing_email'] = email  # Enables unsubscribe button
        else:
            Subscriber.objects.create(email=email)
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')

    return render(request, 'subscribe.html', context)

