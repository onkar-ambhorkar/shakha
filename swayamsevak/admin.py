from django.contrib import admin


class AbstractSwayamsevakAdmin(admin.ModelAdmin):
    list_display = (
        "swayamsevak",
        "phone",
        "house_Flat_No",
        "society",
        "dayitva",
        "ganavesh_status",
        "shiksha_Varg",
        "ghosh_Vadya",
        "date_of_birth_and_age",

    )

    search_fields = ["first_Name", "last_Name", "phone"]


admin.site.site_header = "Shakha"
admin.site.site_title = "Shakha"
admin.site.index_title = "Shakha Administration"
