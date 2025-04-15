from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Topics)
# admin.site.register(Content)
# admin.site.register(Tutorial)

@admin.register(Topics)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")
    search_fields = ("name",)

@admin.register(Content)
class Content(admin.ModelAdmin):
    list_display = ("title", "topic", "tutorial", "content", "author", "created_at")
    list_filter = ("topic",)    
    search_fields = ("title__startswith",)

@admin.register(Tutorial)
class Tutorial(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ("user_id", "content_id", "comment", "created_at")
    list_filter = ("content_id",)