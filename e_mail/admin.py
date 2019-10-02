from django.contrib import admin

from .models import Email, Inbox, Sent

admin.site.register(Email)
admin.site.register(Inbox)
admin.site.register(Sent)
