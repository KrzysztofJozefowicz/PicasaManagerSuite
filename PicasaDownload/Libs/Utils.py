'''
Created on 24-03-2013

@author:  j00zef.git@gmail.com
'''
import os
import unicodedata
import gdata.photos.service
import re
from GetAlbumsUrl import GetAllAlbumsUrl


def SetProxy(Flags):
    if Flags['Proxy'] != None:
        os.environ['http_proxy'] = "http://" + Flags['Proxy']
        os.environ['https_proxy'] = "https://" + Flags['Proxy']


def ConvertToAscii(TextString):
    return(unicodedata.normalize('NFD', TextString.decode('utf-8')).encode('ascii', 'ignore'))


def GetFeed(Feed):  # Get PicasaWeb service feed with reconnect posibility
    reconnect = 0
    while reconnect < 3:
        try:
            return(Feed)
        except gdata.photos.service.GooglePhotosException:
            reconnect += 1
            print "PicasaWeb server error 500 - need to reconnect"
            if reconnect == 3:
                print "Connection to Google PicasaWeb failed,try to run script again"
                exit(-1)


def RemoveForbiddenCharsFromName(String):
    String = String.replace('/', '')
    String = String.replace('*', '')
    String = String.replace('\\', '')
    String = String.replace('?', '')
    return(String)


def KeepFileOrder(FileCounter, photo, Flags):
    if Flags['KeepFileOrder'] == True:

        if len(str(FileCounter)) == 1:
            photo.title.text = '00' + str(FileCounter) + '-' + photo.title.text
        if len(str(FileCounter)) == 2:
            photo.title.text = '0' + str(FileCounter) + '-' + photo.title.text


def CrateAlbumDirectory(DirectoryName, Flags):
    dir_name = Flags['WorkingDirectory'] + '/' + DirectoryName + '/'

    if os.path.exists(dir_name) == False:  # create directory for download album as album name
        try:
            os.mkdir(dir_name)
        except WindowsError:
            print "Unable to create directory " + dir_name
            exit()
    return(dir_name)


def CreateWorkingDirectory(Flags):
    if os.path.exists(Flags['WorkingDirectory']) == False:  # create directory for download album as album name
        try:
            os.mkdir(Flags['WorkingDirectory'])
        except WindowsError:
            print "Unable to create directory " + Flags['WorkingDirectory'] + " pointed by WorkingDirectory parameter."
            exit()


def GetAlbumList(Flags):
    AlbumList = []
    if Flags['PicasaAlbumsUrlFile'] != None:
        lines = [line.strip() for line in open(Flags['PicasaAlbumsUrlFile'])]
        for i in lines:
            AlbumList.append(i)

    elif Flags['AlbumUrl'] != None:
        AlbumUrl = Flags['AlbumUrl']
        AlbumUrl = re.split("(&.*)|(\#.*)|(\?.*)", AlbumUrl)[0]
        AlbumList.append(AlbumUrl)

    else:
        AlbumList = GetAllAlbumsUrl(Flags['PicasaUser'], Flags['PicasaAlbumsVisability'], Flags['Username'], Flags['Password'])

    for i in range(len(AlbumList)):
        AlbumList[i] = re.split("/", AlbumList[i])[-1]  # get rid of everything except album title url - workaround to download non user public albums as username is not present in public album urls
    return(AlbumList)


def Autorize(Flags):
    try:
        gd_client = gdata.photos.service.PhotosService()
        gd_client.email = Flags['Username']
        gd_client.password = Flags['Password']
        gd_client.source = 'exampleCo-exampleApp-1'
        gd_client.ProgrammaticLogin()
    except Exception, error:
        print "Incorect username:" + Flags['Username'] + " or password:" + Flags['Password']
        print str(error)
        exit()
    return(gd_client)


def GetProperUrlPart(url):
    return(re.split("(\?.*)", re.split("/", url)[-1])[0])
