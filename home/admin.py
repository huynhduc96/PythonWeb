from django.contrib import admin
from .models import Category, Book, BookComment, BookHistory, BookingRequest


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, AuthorAdmin)
admin.site.register(Category, AuthorAdmin)
admin.site.register(BookComment, AuthorAdmin)
admin.site.register(BookHistory, AuthorAdmin)
