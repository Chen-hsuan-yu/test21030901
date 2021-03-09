from django.contrib import admin
from myapp.models import NewTable
from myapp.models import Post
from myapp.models import Product

# Register your models here.


admin.site.register(NewTable)
admin.site.register(Post)
admin.site.register(Product)

