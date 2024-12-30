from django.contrib import admin
from .models import ContactMessage, grocrey,vegitables



# Register your models here.
@admin.register(grocrey)
class grocreyAdmin(admin.ModelAdmin):
    list_display = ['id','gname','gprice','ginfo','gamm','gimg']


@admin.register(vegitables)
class vegitablesAdmin(admin.ModelAdmin):
    list_display = ['id','vname','vprice','vinfo','vamm','vimg']



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Colonnes à afficher
    list_filter = ('created_at',)  # Filtrer par date
    search_fields = ('name', 'email', 'message')