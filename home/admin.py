from django.contrib import admin
from .models import Contact,Category,Blog,Team,Tournament,Match,Pointable,Comment,Match_Video


admin.site.index_title="Game Maker Dashboard"
admin.site.site_title="Game Maker Dashboard"
admin.site.site_header="Admin-Panel"
# Register your models here.
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register((Blog,Comment))
admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Pointable)
admin.site.register(Match_Video)