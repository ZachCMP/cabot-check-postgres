from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from cabot.cabotapp.models import StatusCheck
from cabot.cabotapp.views import (CheckCreateView, CheckUpdateView,
                                  StatusCheckForm, base_widgets)

from .models import PostgresStatusCheck


class PostgresStatusCheckForm(StatusCheckForm):
    symmetrical_fields = ('service_set', 'instance_set')

    class Meta:
        model = PostgresStatusCheck
        fields = (
            'name',
            'host',
            'port',
            'dbname',
            'user',
            'password',
            'timeout',
            'frequency',
            'active',
            'importance',
            'debounce',
        )

        widgets = dict(**base_widgets)
        widgets.update({
            'host': forms.TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'service.arachnys.com',
            })
        })


class NetworkCheckCreateView(CheckCreateView):
    model = PostgresStatusCheck
    form_class = PostgresStatusCheckForm


class NetworkCheckUpdateView(CheckUpdateView):
    model = PostgresStatusCheck
    form_class = PostgresStatusCheckForm


def duplicate_check(request, pk):
    pc = StatusCheck.objects.get(pk=pk)
    npk = pc.duplicate()
    return HttpResponseRedirect(reverse('update-status-check', kwargs={'pk': npk}))
