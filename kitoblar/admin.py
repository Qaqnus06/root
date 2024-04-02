from django.contrib import admin
from .models  import Book,Ega,KitobEga,Til,Comment


class BookAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields=('firstname',)
class EgaAdmin(admin.ModelAdmin):
    list_display = ('first_name','age','email','phone')
    search_fields=('age','first_name')    

class KitobEgaAdmin(admin.ModelAdmin):
    list_display = ('kitob','ega')
    search_fields=('kitob','ega')
    list_display_links = ('kitob',)




admin.site.register(Til)
admin.site.register(Book,BookAdmin)
admin.site.register(Ega,EgaAdmin)
admin.site.register(KitobEga,KitobEgaAdmin)
admin.site.register(Comment)
