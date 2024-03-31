import abc
import datetime
import os

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from birthday import BirthdayField, BirthdayManager

from shakha_dayitva.models import Model


class AbstractModelMeta(abc.ABCMeta, type(models.Model)):
    pass


class AbstractSwayamsevak(models.Model, metaclass=AbstractModelMeta):
    class Meta:
        verbose_name = "स्वयंसेवक"
        verbose_name_plural = "शाखा पट"
        abstract = True

    SHIKSHA_VARG_OPTIONS = [
        ('Prarambhik', 'Prarambhik'),
        ('Prathamik', 'Prathamik'),
        ('Pratham', 'Pratham'),
        ('Dvitiya', 'Dvitiya'),
        ('Tritiya', 'Tritiya')
    ]

    first_Name = models.CharField(max_length=15)
    middle_Name = models.CharField(max_length=15)
    last_Name = models.CharField(max_length=20)
    phone = PhoneNumberField(null=True, blank=False, unique=True)
    date_of_birth = BirthdayField()
    house_Flat_No = models.CharField(max_length=20, verbose_name="House/Flat No")
    ganavesh = models.CharField(max_length=100, default='', blank=True)
    shiksha_Varg = models.CharField(max_length=12, choices=SHIKSHA_VARG_OPTIONS, default='', blank=True)
    ghosh_Vadya = models.CharField(max_length=100, default='', blank=True)
    dayitva = models.ForeignKey(Model, on_delete=models.DO_NOTHING, null=True, default='', blank=True)

    objects = BirthdayManager()

    def swayamsevak(self) -> str:
        return f"{self.first_Name} {self.last_Name}"

    def __str__(self) -> str:
        return f"{self.first_Name} {self.last_Name}"

    def date_of_birth_and_age(self):
        today = datetime.date.today()
        born = self.date_of_birth
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return f"{born.strftime('%d %b %Y')} | {age}Yr"

    date_of_birth_and_age.short_description = 'Date Of Birth'

    def ganavesh_status(self):
        if not self.ganavesh == "":
            ganavesh_list = f"{self.ganavesh}".split(',')
            if len(ganavesh_list) == 7:
                return "Complete"
            elif len(ganavesh_list) > 0:
                return "Partial"
        else:
            return "None"

    ganavesh_status.short_description = "Ganavesh"
