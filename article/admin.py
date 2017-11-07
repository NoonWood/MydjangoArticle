from django.contrib import admin
from article.models import Article, Comments

# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    #fields = ['Article_title, Article_text, Article_date']
    inlines = [ArticleInline]
    list_filter = ['Article_date']

admin.site.register(Article, ArticleAdmin)