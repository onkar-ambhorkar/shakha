import abc

from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class AbstractFilterMeta(abc.ABCMeta, type(admin.SimpleListFilter)):
    pass


class AbstractBirthdayFilter(admin.SimpleListFilter, metaclass=AbstractFilterMeta):
    class Meta:
        abstract = True

    title = _("Birthday's")
    parameter_name = 'birthdays'

    def lookups(self, request, model_admin):
        return (
            ('today', _('Today')),
            ('next_30_days', _('Next 30 Days')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'today':
            return self.get_todays_birthday()
        if self.value() == 'next_30_days':
            return self.get_next_30_days_birthday()

    @abc.abstractmethod
    def get_todays_birthday(self):
        pass

    @abc.abstractmethod
    def get_next_30_days_birthday(self):
        pass
