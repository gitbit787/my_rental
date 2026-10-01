from django.contrib import admin
from .models import Renter, Property

# Register your models here.
admin.site.register(Renter)
admin.site.register(Property)