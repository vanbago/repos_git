from django.contrib import admin
from blog.models import Article, Categorie, Contact

# Register your models here.



"""classe pour la personalisation de l'affichage de nos notre site d'aministration,
   pour la gestion de nos site facilement
   la class Modeladmin contient des outils qui permet de modifier l'interface d'administration
   a notre guise
"""

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    list_filter = ('author', 'category',)
    date_hierarchy = 'date'
    ordering = ('title', )
    search_fields = ('title','content')
    fields = ('title', 'author', 'category', 'content', 'slug')
    
    
            

    
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
admin.site.register(Contact)


