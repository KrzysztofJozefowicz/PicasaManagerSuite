'''
Created on 27-03-2013

@author: j00zef.git@gmail.com
'''
import os
import gdata 
import time
def AlbumCreate(AlbumInfo,gd_client,Flags):
        print '#################'
        print AlbumInfo['Title']+' :processing'
        
        ### Album create ###
        albums=gd_client.GetUserFeed(user=Flags['Username'])
        

        Unique=True
        for album in albums.entry:
            if album.title.text==AlbumInfo['Title']:
                Unique=False
                break
            
        
        if Unique==True:
            try:
                
                album = gd_client.InsertAlbum(AlbumInfo['Title'], AlbumInfo['Summary'])
                print "Album: "+AlbumInfo['Title']+" :created,summary added"
            except:
                 print AlbumInfo['Title']+" :album creation failed"
                 exit()
def AlbumUpdate(AlbumInfo,gd_client,Flags):           
        albums=gd_client.GetUserFeed(user=Flags['Username'])
        for album in albums.entry:
            if album.title.text==AlbumInfo['Title']:
                if AlbumInfo['Access']:
                    album.access.text=AlbumInfo['Access']
                if AlbumInfo['Location']:
                    album.location.text=AlbumInfo['Location']
                if AlbumInfo['Published']:
                    album.timestamp = gdata.photos.Timestamp(text="%d000" % time.mktime((int(AlbumInfo['Published'][0]), int(AlbumInfo['Published'][1]), int(AlbumInfo['Published'][2]), 12, 00, 00, -1, -1, -1)))
                
                try:
                    updated_album = gd_client.Put(album, album.GetEditLink().href,converter=gdata.photos.AlbumEntryFromString)
                except Exception,e:
                    print e
                print "Album "+AlbumInfo['Title']+" :information updated."
                break
        
        