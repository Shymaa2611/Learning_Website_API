from django.contrib import admin
from .models import userCustom,profile,Contact

class userCustomAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'track')
    list_filter = ('track',)
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(userCustom, userCustomAdmin)  

admin.site.register(profile)
admin.site.register(Contact)
