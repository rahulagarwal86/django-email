from django.conf import settings
from mailer.views import EmailData
from django.http import HttpResponse

"""
Example view to explain how this utility works
"""
def example( request ):
    
    data_dict = {'name':'Test User', 'message':'Its great'}
    to_mail = settings.BCC_MAIL
    email_key = 'TEST_MAIL'
    email_obj = EmailData( to_mail = to_mail, email_key = email_key, data_dict = data_dict )
    email_obj.send_mail()
    return HttpResponse( 'True' )

