from django import forms


class AbstractSocietyForm(forms.ModelForm):
    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(AbstractSocietyForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
