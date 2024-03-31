from guru_govind_singh.models.society import Society
from society.form import AbstractSocietyForm


class SocietyForm(AbstractSocietyForm):
    class Meta:
        model = Society
        exclude = ("",)
