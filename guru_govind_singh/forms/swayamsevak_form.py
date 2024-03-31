from guru_govind_singh.models.swayamsevak import Swayamsevak
from swayamsevak.form import AbstractSwayamsevakForm


class SwayamsevakForm(AbstractSwayamsevakForm):
    class Meta:
        model = Swayamsevak
        exclude = ("",)
