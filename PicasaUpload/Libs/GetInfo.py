'''
Created on 27-03-2013

@author: j00zef.git@gmail.com
'''

import os
def ReadAlbumInfo(AlbumDirectory,Flags):
    AlbumDirectory=AlbumDirectory.replace("\\",'/') #normalize slashes in Directory paths
    Properites={}
    Properites['Title']=None
    Properites['Summary']=None
    Properites['Published']=None
    Properites['Location']=None
    Properites['Access']=None
    
    if os.path.exists(AlbumDirectory+'/AlbumInfo.txt'):
        
        lines=[line.strip() for line in open(AlbumDirectory+'/'+'AlbumInfo.txt')]
        
        for i in lines:
     
            if len(i.split("="))==1:
                Properites[i.split("=")[0].capitalize()]=None
            else:
                Properites[i.split("=")[0].capitalize()]=i.split("=")[1]
        if Properites['Published']:
                Properites['Published']=Properites['Published'][0:10].split("-")
                    
        if Flags['TitleFromAlbumInfo']==False:
            Properites['Title']=AlbumDirectory.split("/")[-1]
        if Flags['SummaryFromAlbumInfo']==False:
            Properites['Summary']=None
        if Flags['PublishedFromAlbumInfo']==False:
            Properites['Published']=None
        if Flags['LocationFromAlbumInfo']==False:
            Properites['Location']=None
        if Flags['AccessFromAlbumInfo']==False:
            Properites['Access']=None
    else:
          Properites['Title']=AlbumDirectory.split("/")[-1] 
    return Properites


def ReadFileInfo(file):
    Properites={}

    tmp=''
    
    Properites['Comment']=None
    Properites['GPS']=None
    Properites['Summary']=None
    
    
    
    if os.path.exists(file+"-comment.txt"):
        lines=[line.strip() for line in open(file+"-comment.txt")]
        for i in lines:
             tmp+=i+'\n'
        Properites['Comment']=tmp

    if os.path.exists(file+"-gps.txt"):
        lines=[line.strip() for line in open(file+"-gps.txt")]
        Properites['GPS']=lines[0]+' '+lines[1]
    tmp=''
    if os.path.exists(file+"-title.txt"):
        lines=[line.strip() for line in open(file+"-title.txt")]
        for i in lines:
            tmp+=i+'\n'
        Properites['Summary']=tmp

    Properites['FileName']=os.path.basename(file)
    
    if os.path.exists(file):
        Properites['FilePath']=file
    else:
        Properites['FilePath']=None
    
    return(Properites)

