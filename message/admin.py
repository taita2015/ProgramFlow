from django.contrib import admin

# Register your models here.


from .models import SystemToUserMessage
from .models import UserMessageStatus
from .models import UserToUserMessage
from .models import EventMessage



class SystemToUserMessageAdmin(admin.ModelAdmin):
    list_display = ['','']

admin.site.register(SystemToUserMessage)
admin.site.register(UserMessageStatus)
admin.site.register(UserToUserMessage)
admin.site.register(EventMessage)