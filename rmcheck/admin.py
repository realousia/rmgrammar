from django.contrib import admin
from .models import Ramyeon
# Register your models here.

class Radmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'company', 'sort', 'size', 'calories')
	list_display_links = ('id', 'name', 'company', 'sort', 'size', 'calories')
	search_fields = ('name', 'company')

admin.site.register(Ramyeon, Radmin)

