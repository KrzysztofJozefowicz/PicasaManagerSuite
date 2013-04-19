'''
Created on 27-03-2013

@author: j00zef.git@gmail.com
'''
import os

def GetDirectoryList(Flags):
    DirectoryList=[]
    if os.path.isfile(Flags['AlbumListToUpload']):
        lines=[line.strip() for line in open(Flags['AlbumListToUpload'])]
        for i in lines:
            if os.path.isdir(i):
                DirectoryList.append(i)
    if os.path.isdir(Flags['AlbumListToUpload']):
        DirectoryList=GetAllDirs(Flags['AlbumListToUpload'])
    
    return(DirectoryList)

def GetAllDirs(WorkingDirectory):
    DirList=[]
    for paths,dir,files in os.walk(WorkingDirectory):
       if files:
           DirList.append(paths)
       
    return(DirList)

def RemoveSuffixFromFileList(entry):
    entry=entry.replace('-comment.txt','')
    entry=entry.replace('-title.txt','')
    entry=entry.replace('-gps.txt','')
    return entry

def GetFileList(AlbumDirectory,SupportedFileTypes,Flags):
    FileList=[]
    PhotoList=[]
    
    for paths,dir,files in os.walk(AlbumDirectory):
       if files:
           FileList=files
       break
    


    for i in FileList:
        
        
        if  (Flags['AlbumCoverUpload']=='False' and i.lower()=='album-cover.jpg') or i.lower()=='albuminfo.txt':
            continue
        else: 
            if i[len(i)-3:len(i)].lower() in SupportedFileTypes:            
                PhotoList.append(i)
    PhotoList=map(RemoveSuffixFromFileList,PhotoList)
    PhotoList=list(set(PhotoList))
    return PhotoList