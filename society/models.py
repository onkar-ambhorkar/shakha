from django.db import models


class AbstractSociety(models.Model):
    class Meta:
        verbose_name = "सोसायटी"
        verbose_name_plural = "सोसायटी"
        abstract = True

    society_Name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.society_Name}"
