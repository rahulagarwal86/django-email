from django.contrib import admin
from mailer.models import Emailer

class EmailerAdmin( admin.ModelAdmin ):
    model = Emailer
    list_display = ['email_key']
    search_fields = ['email_key']

admin.site.register( Emailer, EmailerAdmin )
