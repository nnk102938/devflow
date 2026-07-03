from django.contrib import admin
from .models import Category, Reference,Flow,FlowStep

admin.site.register(Category)
admin.site.register(Flow)
admin.site.register(FlowStep)

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
    )