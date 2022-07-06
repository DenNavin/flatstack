from django.contrib import admin
from yesnowtf.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    pass

