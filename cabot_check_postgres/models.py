import socket
import psycopg2

from django.db import models

from cabot.cabotapp.models import StatusCheck, StatusCheckResult


class PostgresStatusCheck(StatusCheck):
    check_name = 'postgres'
    edit_url_name = 'update-postgres-check'
    duplicate_url_name = 'duplicate-postgres-check'
    icon_class = 'glyphicon-hdd'
    host = models.TextField(
        help_text='Postgres host',
    )
    port = models.PositiveIntegerField(
        help_text='Postgres port',
    )
    dbname = models.TextField(
        help_text='Postgres database name'
    )
    dbuser = models.TextField(
        help_text='Postgres user'
    )
    dbpassword = models.TextField(
        help_text='Postgres password'
    )

    def _run(self):
        result = StatusCheckResult(status_check=self)

        try:
            conn = psycopg2.connect(dbname=self.dbname, user=self.dbuser, password=self.dbpassword, host=self.host, port=self.port)
            conn.close()
        except Exception as e:
            result.error = u'Error occurred: %s' % (e.message)
            result.succeeded = False
        else:
            result.succeeded = True

        return result
