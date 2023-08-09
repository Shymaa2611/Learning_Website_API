from django.contrib import admin
from .models import userCustom,profile

class userCustomAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'track')
    list_filter = ('track',)
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(userCustom, userCustomAdmin)  # Corrected registration

admin.site.register(profile)
