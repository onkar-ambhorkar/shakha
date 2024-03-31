from django.db import models


class Model(models.Model):
    class Meta:
        verbose_name = "शाखा दायित्व"
        verbose_name_plural = "शाखा दायित्व"

    shakha_Dayitva = models.CharField(max_length=30)

    def __str__(self):
        return self.shakha_Dayitva
