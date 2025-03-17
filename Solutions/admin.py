from django.contrib import admin

# Register your models here.
from .models import GetinTouch,ApplyForProject,OnlineTraining


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone','subject','message')  # Fields to show in the list view
    search_fields = ('name', 'email')  # Enable search functionality by username or email
    # list_filter = ('email',)  # Add filter by email


class training(admin.ModelAdmin):
    list_display = ('name', 'email','phone','branch','year')  # Fields to show in the list view
    search_fields = ('name', 'email')  # Enable search functionality by username or email
    # list_filter = ('email',)  # Add filter by email


class work(admin.ModelAdmin):
    list_display = ('name', 'email','phone','branch','year')  # Fields to show in the list view
    search_fields = ('name', 'email')  # Enable search functionality by username or email
    # list_filter = ('email',)  # Add filter by email


admin.site.register(GetinTouch, UserAdmin)
admin.site.register(ApplyForProject, work)
admin.site.register(OnlineTraining, training)

 