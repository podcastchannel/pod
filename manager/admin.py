from django.contrib import admin
from .models import Manager,Listener,Program, Announcement, LocalNew, GlobalNew

admin.site.register(Manager)
admin.site.register(Listener)
admin.site.register(Program)
admin.site.register(Announcement)
admin.site.register(LocalNew)
admin.site.register(GlobalNew)
