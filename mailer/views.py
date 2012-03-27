from django.http import HttpResponse
from mailer.models import Emailer, SmsMessage
from django.conf import settings
import threading
import Queue
email_queue = Queue.Queue()
from django.core.mail import EmailMultiAlternatives
from settings import PROJECT_DIR
import os

"""
EmailData Class object is used to send email.
"""
class EmailData( object ):
    
    def __init__( self, to_mail, email_key, data_dict = {}, attachment_file = None ):
        self.to_mail = to_mail
        self.email_key = email_key
        self.data_dict = data_dict
        self.from_mail = settings.DEFAULT_FROM_EMAIL
        self.attachment = attachment_file

    def send_mail( self ) :
        
        def mail_msg():
            data = email_queue.get()
            bcc_mail = settings.BCC_MAIL
            
            try:
                msg = EmailMultiAlternatives( data['subject'], data['txt_body'], self.from_mail, to = data['send_to'], bcc = [bcc_mail] )
                msg.content_subtype = "html"
                if not self.attachment is None: 
                    file_name = self.attachment
                    attachment = os.path.join( PROJECT_DIR, 'downloads/attachments/%s' % file_name ).replace( '\\', '/' )
                    msg.attach_file( attachment )
                msg.send()
            except Exception:
                pass
        try:
            email_obj = Emailer.objects.get( email_key = self.email_key , send_flag = True )
            email_data = {}
            mail_body = ( email_obj.body ) % self.data_dict
            email_data['txt_body'] = str( mail_body ) 
            email_data['subject'] = str( email_obj.subject ) % self.data_dict
            send_to = self.to_mail
            if type( send_to ) in ( str, unicode ) :
                email_data['send_to'] = [send_to]
            elif isinstance( send_to, list ):
                email_data['send_to'] = send_to
            email_queue.put( email_data )
            email_thread = threading.Thread( target = mail_msg, )
            email_thread.setDaemon( True )
            email_thread.start()
        except Exception:
            pass
