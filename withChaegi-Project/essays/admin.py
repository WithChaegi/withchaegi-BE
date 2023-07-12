from django.contrib import admin

from .models import Essay, Comment

class CommentInline(admin.StackedInline):
    # 가로는 TabularInline
    model = Comment
    extra = 3
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

@admin.register(Essay)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'essay_title', 'writer', 'book_title', 'book_author', 'essay_content', 'created_at', 'view_count')
    #search_fields = ('book_title')
    inlines = [CommentInline]
    readonly_fields = ('created_at', )

# admin.site.register(Comment)