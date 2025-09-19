from django.contrib import admin

# Register your models here.
# blog/admin.py
from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):  # show comments inside Post page
    model = Comment
    extra = 1  # one empty comment form by default

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    list_filter = ("author", "created_at")
    search_fields = ("title", "content")
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at")
    list_filter = ("author", "created_at")
    search_fields = ("content",)
