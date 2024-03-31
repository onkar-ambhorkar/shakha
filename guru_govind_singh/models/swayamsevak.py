

from swayamsevak.models import AbstractSwayamsevak, models
from .society import Society


class Swayamsevak(AbstractSwayamsevak):
    society = models.ForeignKey(Society, on_delete=models.DO_NOTHING)
