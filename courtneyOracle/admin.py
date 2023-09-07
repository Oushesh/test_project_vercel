from django.contrib import admin

# Register your models here.
from .models import BlogPost, UserActivity
admin.site.register(BlogPost) #admin registerign the Django Data Model

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ["slug", "image", "result", "created_at"]
