from django.contrib import admin
from .models import Destination
from .models import PC_stock, Asset, Infrastructure, Post

# Register your models here.
admin.site.register(Destination)
admin.site.register(PC_stock)
admin.site.register(Asset)
admin.site.register(Infrastructure)
admin.site.register(Post)

