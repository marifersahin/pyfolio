from django.contrib import admin
from entry.models import Entry, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('created_date',)
admin.site.register(Category, CategoryAdmin)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('created_date',)
admin.site.register(Entry, EntryAdmin)
