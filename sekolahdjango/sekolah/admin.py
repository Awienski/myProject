from django.contrib import admin
from .models import Sekolah

# Register your models here.
class SekolahAdmin(admin.ModelAdmin):
    list_display=('name_school', 'address')

admin.site.register(Sekolah, SekolahAdmin)
