from django.contrib import admin
from .models import Notes
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'content')
    search_fields = ('title', 'content', 'author__username')

admin.site.register(Notes, NotesAdmin)
