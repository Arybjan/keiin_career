from django.contrib import admin
from .models import User, Genders


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "username",
        "email",
        "birthday_date",
        "genders",
        "created_at",
    ]


admin.site.register(User, UserAdmin)


class GendersAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title"
    ]


admin.site.register(Genders, GendersAdmin)
