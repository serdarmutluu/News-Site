from django.contrib import admin
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth
from .models import *
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    class Meta:
        model=Post

class AdAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    class Meta:
        model=Post

    """def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False"""


admin.site.site_header = 'Haber Sitesi'
admin.site.register(Post,PostAdmin)
admin.site.register(Ad,AdAdmin)
admin.site.register(Slider)
admin.site.unregister(auth.models.Group)