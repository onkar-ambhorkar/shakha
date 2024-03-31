import re

from django import forms


class AbstractSwayamsevakForm(forms.ModelForm):
    class Meta:
        abstract = True

    GANAVESH_OPTIONS = [
        ('Topi', 'Topi'),
        ('Shirt', 'Shirt'),
        ('Pant', 'Pant'),
        ('Belt', 'Belt'),
        ('Socks', 'Socks'),
        ('Shoes', 'Shoes'),
        ('Danda', 'Danda')
    ]

    GHOSH_VADYA_OPTIONS = [
        ('Aanak', 'Aanak'),
        ('Venu', 'Venu'),
        ('Shankha', 'Shankha'),
        ('Panav', 'Panav')
    ]

    ganavesh = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=GANAVESH_OPTIONS
    )

    ghosh_Vadya = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=GHOSH_VADYA_OPTIONS
    )

    def clean_ganavesh(self):
        ganavesh = re.sub(r"[\"['\]]", "", f"{self.cleaned_data.get('ganavesh')}")
        return ganavesh

    def clean_ghosh_Vadya(self):
        ganavesh = re.sub(r"[\"['\]]", "", f"{self.cleaned_data.get('ghosh_Vadya')}")
        return ganavesh

    def __init__(self, *args, **kwargs):
        super(AbstractSwayamsevakForm, self).__init__(*args, **kwargs)
        if not f"{kwargs}".__contains__("'initial': {}") and not f"{kwargs}".__contains__("'instance': None"):
            self.get_selected_ganavesh(**kwargs)
            self.get_selected_ghosh_vadya(**kwargs)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def get_selected_ganavesh(self, **kwargs):
        ganavesh_str = kwargs.pop('instance').ganavesh
        ganavesh_list = ganavesh_str.split(',')
        ganavesh_list_selected = []
        for index, ganavesh in enumerate(ganavesh_list):
            ganavesh = ganavesh.strip()
            ganavesh_list_selected.insert(index, ganavesh)
        self.initial['ganavesh'] = ganavesh_list_selected

    def get_selected_ghosh_vadya(self, **kwargs):
        ghosh_vadya_str = kwargs.pop('instance').ghosh_Vadya
        ghosh_vadya_list = ghosh_vadya_str.split(',')
        ghosh_vadya_list_selected = []
        for index, ghosh_vadya in enumerate(ghosh_vadya_list):
            ghosh_vadya = ghosh_vadya.strip()
            ghosh_vadya_list_selected.insert(index, ghosh_vadya)
        self.initial['ghosh_Vadya'] = ghosh_vadya_list_selected
