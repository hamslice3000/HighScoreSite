from django.contrib import admin
from entries.models import Entry 

# Register your models here.

# admin.site.register(Entry)

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['text']}),
        ('Score',            {'fields': ['score'],}),
        ('Date information', {'fields': ['pub_date'],}),
        ('Voted',            {'fields': ['voted'],}),
    ]
    # inlines = [ChoiceInline]
    list_display = ('text','score','pub_date', 'was_published_recently','voted')
    list_filter = ['pub_date']
    search_fields = ['text']
    
admin.site.register(Entry, EntryAdmin)

