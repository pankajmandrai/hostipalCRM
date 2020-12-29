from django.contrib import admin

from usersapp.models import *
# Register your models here.

admin.site.register(Clients)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Staff)
admin.site.register(DoctorMore)
