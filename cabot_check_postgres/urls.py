from django.conf.urls import url

from .views import (PostgresCheckCreateView, PostgresCheckUpdateView,
                    duplicate_check)

urlpatterns = [

    url(r'^postgrescheck/create/',
        view=PostgresCheckCreateView.as_view(),
        name='create-postgres-check'),

    url(r'^postgrescheck/update/(?P<pk>\d+)/',
        view=PostgresCheckUpdateView.as_view(),
        name='update-postgres-check'),

    url(r'^postgrescheck/duplicate/(?P<pk>\d+)/',
        view=duplicate_check,
        name='duplicate-postgres-check')

]
