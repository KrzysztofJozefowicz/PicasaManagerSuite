'''
Created on 25-03-2013

@author: j00zef.git@gmail.com
'''
import sys
sys.path.append('Libs/')

import gdata.photos.service
 
import argparse
import gdata

 
from InitSetup import *
from GetInfo import *
from GetLists import *
from AlbumHandling import *
from PhotoHandling import *
from Utils import *
 
 

SupportedFileTypes=['jpg','jpeg','png','bmp','gif','txt']
Flags={}

Flags=SetFlags(ReadConfigFile('config.txt'),ArgumentParsing(argparse.ArgumentParser()))



SetProxy(Flags)
 
gd_client=Autorise(Flags)


DirectoryList=GetDirectoryList(Flags)

for Directory in DirectoryList:
        AlbumInfo={}
        AlbumInfo=ReadAlbumInfo(Directory,Flags)

        #create album if directory contains any media files
        if GetFileList(Directory,SupportedFileTypes,Flags):
            AlbumCreate(AlbumInfo,gd_client,Flags)

        ### Album Update###
        AlbumUpdate(AlbumInfo,gd_client,Flags)


        albums=gd_client.GetUserFeed(user=Flags['Username'])

        FileList=GetFileList(Directory,SupportedFileTypes,Flags)

        for album in albums.entry:

            if album.title.text==AlbumInfo['Title']:

                Photos = gd_client.GetFeed( '/data/feed/api/user/%s/albumid/%s?imgmax=d' % (Flags['Username'],album.gphoto_id.text ))
 
                ### check for file names in album to not upload them more than once###
                PhotosInAlbum=GetPhotosFromAlbum(Photos)


                for file in FileList:

                    album_url = '/data/feed/api/user/%s/albumid/%s' % (Flags['Username'], album.gphoto_id.text)
 
                    PhotoInfo=ReadFileInfo(Directory+'/'+file)

                    PhotoUpload(PhotoInfo,PhotosInAlbum,album_url,gd_client)
                    photo=GetPhotoContainer(Photos.entry,PhotoInfo) #in case of only updating meta,find relevant gdata photo container

                    if photo!=None: 
                        photo=PhotoInfoUpdate(PhotoInfo,Flags,photo) #update container with meta data
                        UpdatePhotoMetadata(PhotoInfo,photo,gd_client) #update photo title,gps
                        UpdatePhotoComment(PhotoInfo,photo,Flags,album,gd_client) #update photo comments

print "Done!"       


 
