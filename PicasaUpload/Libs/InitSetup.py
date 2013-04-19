'''
Created on 25-03-2013

@author: j00zef.git@gmail.com
'''

#import argparse
import os
import ast

def SetFlags(Settings,Arguments):
   Flags={}
   
   Flags={'Proxy':None,
       'Username':None,
       'Password': None,
       'AlbumListToUpload':None,
       'TitleFromAlbumInfo':True,
       'SummaryFromAlbumInfo':True,
       'PublishedFromAlbumInfo':True,
       'LocationFromAlbumInfo':True,
       'AccessFromAlbumInfo':True,
       'AlbumCoverUpload':False,
     
       'SummaryFromFile':True,
       'CommentsFromFile':True,
       'GpsFromFile':True,
       }  
    
   for i in Settings:
        for j in Flags:
            if i==j and Settings[i]!=None:
                Flags[i]=Settings[i]
            

   for i in Arguments:        
        for j in Flags:
            if i==j and Arguments[i]!=None:
                Flags[i]=Arguments[i]
    
    

    

   return (Flags)



def ConvertToBool(Flags):
    for items in ['TitleFromAlbumInfo','SummaryFromAlbumInfo','PublishedFromAlbumInfo','LocationFromAlbumInfo','AccessFromAlbumInfo','SummaryFromFile','CommentsFromFile','GpsFromFile'] :
        try:  
            Flags[items]=ast.literal_eval(Flags[items].capitalize())           
        except:
            Flags[items]=None
    
    return(Flags)

def ReadConfigFile(filename):
    settings={}
    if os.path.isfile(filename):
        lines=[line.strip() for line in open(filename)]
        for i in lines:
             i=i.replace("'",'')
             i=i.replace('"','')
             if len(i.split("=")[1])==0:
                    settings[i.split("=")[0]]=None
             else:
                 settings[i.split("=")[0]]=i.split("=")[1]
                 

    return(ConvertToBool(settings))      

def ArgumentParsing(parser):

   
    
    parser.add_argument("-usr", "--Username"                ,dest="Username"                , help="Sets google username to authenticate in gdata service." ) 
    parser.add_argument("-psw", "--Password"                ,dest="Password"                , help="Sets google user's password to authenticate in gdata service." )
    parser.add_argument("-px",  "--Proxy"                   ,dest="Proxy"                   , help="Sets proxy server, format IP:PORT " )       
    
    parser.add_argument("-in",  "--Input"                   ,dest="AlbumListToUpload"       , help="Album directory,directory with albums or file list with paths to albums to upload " )
    parser.add_argument("-at",  "--TitleFromAlbumInfo"      ,dest="TitleFromAlbumInfo"      , help="Use album title from album-info file instead of directory name. " )
    parser.add_argument("-as",  "--SummaryFromAlbumInfo"    ,dest="SummaryFromAlbumInfo"    , help="Update album summary from album-info file." )
    parser.add_argument("-ap",  "--PublishedFromAlbumInfo"  ,dest="PublishedFromAlbumInfo"  , help="Update album publish date from album-info file or leave it as current date." )
    parser.add_argument("-al",  "--LocationFromAlbumInfo"   ,dest="LocationFromAlbumInfo"   , help="Update album location from album-info file." )    
    parser.add_argument("-aa",  "--AccessFromAlbumInfo"     ,dest="AccessFromAlbumInfo"     , help="Update album access type from album-info file or leave it as default (public)." )   

    parser.add_argument("-ac",  "--AlbumCoverUpload"        ,dest="AlbumCoverUpload"        , help="Upload album cover file as photo to ablum." )     
    
    parser.add_argument("-ft",  "--SummaryFromFile"           ,dest="SummaryFromFile"           , help="Update file title(summary text) from <filename>-title.txt file.If not set, exif entry will be used " )      
    parser.add_argument("-fc",  "--CommentsFromFile"        ,dest="CommentsFromFile"        , help="Update file comments from <filename>-comments.txt file." )     
    parser.add_argument("-fg",  "--GpsFromFile"             ,dest="GpsFromFile"             , help="Update file gps data from <filename>-gps.txt file.If not set, exif entry will be used " )  
    
    args=parser.parse_args()
    arguments={}
    

    for property,value in vars(args).iteritems():
        arguments[property]=value

    return(ConvertToBool(arguments))
