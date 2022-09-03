from django.contrib import admin
from .models import CustomUser , Driver , Hotel 

admin.site.register(CustomUser)
admin.site.register(Driver)
admin.site.register(Hotel)
admin.site.site_header = "Kiro Travel Admin"
admin.site.site_title = "Kiro Travel Admin Portal"
admin.site.index_title = "Welcome to Kiro Travel Portal"
