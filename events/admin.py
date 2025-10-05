from django.contrib import admin
from .models import User, Event, Category, Favorite, Registration

# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Registration)
