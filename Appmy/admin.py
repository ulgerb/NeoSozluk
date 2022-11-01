from django.contrib import admin
from .models import Contentt, Comments
# Register your models here.



class ContenttAdmin(admin.ModelAdmin):
    '''Admin View for Contentt'''

    list_display = ('title','new_date','yazar')
    list_editable= ('yazar',)
    search_fields = ('yazar',)


class CommentsAdmin(admin.ModelAdmin):
    '''Admin View for Contentt'''

    list_display = ('name',)


admin.site.register(Contentt, ContenttAdmin)
admin.site.register(Comments, CommentsAdmin)
