'''
Created on 25-03-2013

@author: j00zef.git@gmail.com
'''
import gdata
import os
from oauth2client import client

def Autorise(Flags):
    # using http://stackoverflow.com/questions/20248555/list-of-spreadsheets-gdata-oauth2/29157967#29157967 (thanks)
    # copy-paste-changed from https://github.com/leocrawford/picasawebsync (thanks x2 )!
    from oauth2client.file import Storage
    filename = 'user_credidentials.txt'
    storage = Storage(filename)
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        flow = client.flow_from_clientsecrets(Flags['ClientSecret'],scope='https://picasaweb.google.com/data/',redirect_uri='urn:ietf:wg:oauth:2.0:oob')
        auth_uri = flow.step1_get_authorize_url()
        print 'Authorization URL: %s' % auth_uri
        auth_code = raw_input('Enter the auth code: ')
        credentials = flow.step2_exchange(auth_code)
        storage.put(credentials)
    if credentials.access_token_expired:
        try:
            credentials.refresh(httplib2.Http())
        except Exception as error:
            print "Either your credidentials has expired and cannot be refreshed or httplib2 is not installed."
            print "Try to delete user_credidentials.txt and run script again or install http2lib with pip install httplib2"
            print "Error: "+str(error)
            exit(-1)
    gd_client = gdata.photos.service.PhotosService(email='default',additional_headers={'Authorization' : 'Bearer %s' % credentials.access_token})

    return(gd_client)


def SetProxy(Flags):
    if Flags['Proxy']!=None:
        os.environ['http_proxy'] = "http://"+Flags['Proxy']
        os.environ['https_proxy'] = "https://"+Flags['Proxy']


