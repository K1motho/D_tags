from django.contrib import admin
from .models import Blog , Editor, Subscriber

# Register your models here.
admin.site.register(Blog)

admin.site.register(Editor)

admin.site.register(Subscriber)