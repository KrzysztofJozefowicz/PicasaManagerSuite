'''
Created on 25-03-2013

@author: j00zef.git@gmail.com
'''
import gdata
import os

def Autorise(Flags):
    try:
        gd_client = gdata.photos.service.PhotosService()
        gd_client.email =Flags['Username']
        gd_client.password =Flags['Password']
        gd_client.source = 'PMS-Uploader'
        gd_client.ProgrammaticLogin()
    except Exception,error:
        print "Incorect username:"+Flags['Username']+" or password:"+Flags['Password']
        print str(error)
        exit()
    return(gd_client)

def SetProxy(Flags):
    if Flags['Proxy']!=None:
        os.environ['http_proxy'] = "http://"+Flags['Proxy']
        os.environ['https_proxy'] = "https://"+Flags['Proxy']