from django.contrib import admin

from .models import *

# admin.site.register(Genre)
# admin.site.register(Tag)
admin.site.register(StillCut)
admin.site.register(TrailerYouTube)
# admin.site.register(Movie)
admin.site.register(MovieToMember)
admin.site.register(UserToMovie)
admin.site.register(MovieToGenre)


class TagListInline(admin.TabularInline):
    model = Movie.tag.through


class GenreListInline(admin.TabularInline):
    model = Movie.genre.through


class TagAdmin(admin.ModelAdmin):
    inlines = [
        TagListInline,
    ]


class GenreAdmin(admin.ModelAdmin):
    inlines = [
        GenreListInline,
    ]


class MovieAdmin(admin.ModelAdmin):
    inlines = [
        GenreListInline, TagListInline,
    ]
    exclude = ('genre', 'tag',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Movie, MovieAdmin)
