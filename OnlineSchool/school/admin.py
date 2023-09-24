from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')


class TutorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'video_url', 'video_length')


class UserTutorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'tutorial', 'watch_time', 'watch_status', 'last_watch')


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(UserTutorial, UserTutorialAdmin)
