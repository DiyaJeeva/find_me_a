from django.contrib import admin
from .models import Interest, Mentor, Notification, UserProfile

# Register your models here.

admin.site.register(Interest)
admin.site.register(UserProfile)
admin.site.register(Mentor)
admin.site.register(Notification)