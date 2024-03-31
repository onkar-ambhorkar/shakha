from django.contrib import admin


class AbstractSocietyAdmin(admin.ModelAdmin):
    list_display = ("society_Name",)
