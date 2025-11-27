from django.contrib import admin
from .models import Film , FilmScore, FilmComment

# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ('title',"genre" ,'description', 'photoname')
    list_filter = ('title', 'genre')
    search_fields = ('title', 'genre')
    ordering = ('title', 'genre')

class FilmCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'film', 'comment', 'publication_date')
    list_filter = ('user', 'film', 'publication_date')
    search_fields = ('user', 'film', 'publication_date')
    ordering = ('user', 'film', 'publication_date')

class FilmScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'film', 'score')
    list_filter = ('user', 'film', 'score')
    search_fields = ('user', 'film')
    ordering = ('user', 'film', 'score')

admin.site.register(Film, FilmAdmin)
admin.site.register(FilmScore, FilmScoreAdmin)
admin.site.register(FilmComment, FilmCommentAdmin)