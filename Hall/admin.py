from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import *

# Register your models here.



admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Picture)
admin.site.register(Videos)
admin.site.register(Messages)
admin.site.register(Recepteur)
admin.site.register(Comment)