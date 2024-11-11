from django.contrib import admin
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display=('id','title','description')
    search_fields = ['title','description']
    list_editable = ('title','description')

# Register your models here.
admin.site.register(Book,BookAdmin)
