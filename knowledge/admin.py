from django.contrib import admin
from knowledge.models import Manual, Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'text']

    search_fields = ['title', 'text']

    list_display = ['title', 'author','status','created_at']

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Manual)
admin.site.register(Comment)
