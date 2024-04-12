from django.contrib import admin

# Register your models here.
from .models import Submit, Reading

admin.site.register(Submit)
admin.site.register(Reading)