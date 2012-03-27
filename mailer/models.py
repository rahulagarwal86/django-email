from django.db import models

'''
Emailer model used to Store Email Template Information
'''
class Emailer( models.Model ):
    
    email_key = models.CharField( max_length = 50, unique = True, help_text = 'Unique Email Key used for reference.' )
    subject = models.CharField( max_length = 250 , help_text = 'Subject line for email' )
    body = models.TextField( help_text = 'Email content' )
    send_flag = models.BooleanField( default = True , help_text = 'Flag to maintain sending of email' )
    description = models.TextField( blank = True, help_text = 'Email description' )
    
    def __unicode__( self ):
        return self.email_key
