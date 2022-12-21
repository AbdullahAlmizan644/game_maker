from django.contrib import admin
from .models import Contact,Category,Blog,Team,Tournament,Match,Pointable

# Register your models here.
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Tournament)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Pointable)