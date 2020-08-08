from django.contrib import admin
from . models import User, Listing, Category, Watchlist, Bid, UserComment

# Register your models here.

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Watchlist)
admin.site.register(Bid)
admin.site.register(UserComment)    