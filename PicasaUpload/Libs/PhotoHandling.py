'''
Created on 27-03-2013

@author: j00zef.git@gmail.com
'''
import os
import gdata 
#import time
#from gdata import *

def GetPhotoContainer(Photos_entry,PhotoInfo):
    for i in Photos_entry:
        if i.title.text==PhotoInfo['FileName']:
            return (i)

def UpdatePhotoMetadata(PhotoInfo,photo, gd_client):
    Retry=True
    while Retry==True:
 
 
        try:
            gd_client.UpdatePhotoMetadata(photo)                
            print PhotoInfo['FileName']+" :Photo info updated "
            Retry=False
        except Exception,e:
            print PhotoInfo['FileName']+" :Photo info update failed.Try again"
            print str(e)
            Retry=True
                
            
def UpdatePhotoComment(PhotoInfo,photo,Flags,album,gd_client):
    if PhotoInfo['Comment']  and Flags['CommentsFromFile']==True:
        url = '/data/feed/api/user/%s/albumid/%s/photoid/%s' % (Flags['Username'], album.gphoto_id.text, photo.gphoto_id.text)
        Retry=True
        while Retry==True:
            
            try:

                gd_client.InsertComment(url, PhotoInfo['Comment'])
                print PhotoInfo['FileName']+" :comments updated"
                Retry=False
            except Exception,e:
                print PhotoInfo['FileName']+" :comments update failed"
                print str(e)
                Retry=True
            
            


def PhotoUpload(PhotoInfo,PhotosInAlbum,album_url,gd_client):

    if not PhotoInfo['FileName'] in PhotosInAlbum:
        try:
            photo=gd_client.InsertPhotoSimple(album_url,PhotoInfo['FileName'],PhotoInfo['Summary'],PhotoInfo['FilePath'])
            print PhotoInfo['FileName']+" :photo file added,summary updated"
        except Exception,e :
            print PhotoInfo['FileName']+" :file upload failed. "+str(e)

def PhotoInfoUpdate(PhotoInfo,Flags,photo):
    
    if PhotoInfo['Summary'] and Flags['SummaryFromFile']==True:
        photo.summary.text=PhotoInfo['Summary'] 
        print PhotoInfo['FileName']+" :Summary info updated"
                          
    if PhotoInfo['GPS'] and Flags['GpsFromFile']==True:
        if not photo.geo.Point:
            photo.geo.Point = gdata.geo.Point()
            photo.geo.Point.pos = gdata.geo.Pos(text=PhotoInfo['GPS']) 
            print PhotoInfo['FileName']+" :GPS info updated"
    return(photo)  

def GetPhotosFromAlbum(Photos):
    
    PhotosInAlbum=[]
    for i in Photos.entry:

        PhotosInAlbum.append(i.title.text)  
    return(PhotosInAlbum)                  