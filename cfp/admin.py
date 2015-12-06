from django.contrib import admin
from django import forms

from .models import Proposal


class ProposalReadOnlyForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProposalReadOnlyForm, self).__init__(*args, **kwargs)
        for f in self.fields.values():
            if f.widget.is_hidden:
                continue
            f.widget.attrs.setdefault('readonly', True)


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    actions = None  # prevent accidentally deleting proposals
    exclude = ['name', 'email', 'speaker_information']
    form = ProposalReadOnlyForm
