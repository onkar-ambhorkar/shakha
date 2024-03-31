from guru_govind_singh.filters.birthday_filter import BirthdayFilter
from guru_govind_singh.forms.swayamsevak_form import SwayamsevakForm
from swayamsevak.admin import AbstractSwayamsevakAdmin


class SwayamsevakAdmin(AbstractSwayamsevakAdmin):
    form = SwayamsevakForm

    list_filter = (BirthdayFilter, "shiksha_Varg",)
