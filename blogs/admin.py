from django.contrib import admin
from blogs.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('title', 'created_at')
    ordering = ('-created_at',)
    fields = ('title', 'content')
    readonly_fields = ('created_at',)
