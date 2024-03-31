from guru_govind_singh.forms.society_form import SocietyForm
from society.admin import AbstractSocietyAdmin


class SocietyAdmin(AbstractSocietyAdmin):
    form = SocietyForm
