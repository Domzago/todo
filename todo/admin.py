from django.contrib import admin

from . models import Todo

# Register your models here.
admin.site.site_header  = 'Zago Admin Area'
admin.site.index_title = 'The Real Zone'

admin.site.register(Todo)
