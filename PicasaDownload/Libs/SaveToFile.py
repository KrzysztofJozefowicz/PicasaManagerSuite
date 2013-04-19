'''
Created on 25-03-2013

@author:  j00zef.git@gmail.com
'''

import urllib2
import Utils


def SaveFile(url, filename):  # saves file from given URL source to given direcotry&filename. Filename parameter must contain directory part
    file = open(filename, 'wb')
    file.write(urllib2.urlopen(url).read())
    file.close()


def SaveComment(text, filename):  # saves comment from given photo to given directory&filename. Filename parameter must contain directory part.Output filename has suffix -comment.txt
    file = open(filename + '-comment.txt', 'wb')
    file.write(text)
    file.close()


def SaveTitle(text, filename):  # saves title from given photo to given directory&filename. Filename parameter must contain directory part.Output filename has suffix -title.txt
    file = open(filename + '-title.txt', 'wb')
    file.write(text)
    file.close()


def SaveGps(latitude, longitude, filename):  # saves gps from given photo to given directory&filename. Filename parameter must contain directory part.Output filename has suffix -gps.txt
    file = open(filename + '-gps.txt', 'wb')
    file.write(str(latitude) + '\r\n')
    file.write(str(longitude))
    file.close()


def SaveAlbumInfo(info, filename):  # saves gps from given photo to given directory&filename. Filename parameter must contain directory part.Output filename has suffix -gps.txt
    file = open(filename, 'wb')
    file.write('title=' + str(info['Title']) + '\r\n')
    file.write('summary=' + str(info['Summary']) + '\r\n')
    file.write('published=' + str(info['Published']) + '\r\n')
    file.write('location=' + str(info['Location']) + '\r\n')
    file.write('access=' + str(info['Access']) + '\r\n')
    file.close()


def SaveAllAlbumsUrlToFile(AlbumList, filename):
    file = open(filename, 'wb')
    for i in AlbumList:
        file.write(i + '\r\n')
    file.close()


def SaveVideoToFile(text, filename):
    file = open(filename, 'wb')
    file.write(text)
    file.close()


def SaveAlbumInfoToFile(album, dir_name, Flags):
    if Flags['SaveAlbumInfoToFile'] == True:
        if Flags['ConvertToAscii'] == 'True' or Flags['ConvertToAscii'] == 'Text':
            album.title.text = Utils.ConvertToAscii(album.title.text)
            if album.summary.text != None:
                album.summary.text = Utils.ConvertToAscii(album.summary.text)

    albumInfo = {}
    albumInfo['Title'] = album.title.text
    if album.summary.text:
        albumInfo['Summary'] = album.summary.text
    else:
        albumInfo['Summary'] = ''
    albumInfo['Published'] = album.published.text[0:10]
    if album.location.text:
        albumInfo['Location'] = album.location.text
    else:
        albumInfo['Location'] = ''
    albumInfo['Access'] = album.access.text
    SaveAlbumInfo(albumInfo, dir_name + 'AlbumInfo.txt')
    print album.title.text + " album info saved to file"


def SaveAlbumThumbToFile(album, dir_name, Flags):
    if Flags['SaveAlbumThumbToFile'] == True:
        SaveFile(album.media.thumbnail[0].url, dir_name + 'Album-Cover.jpg')
        print album.title.text + " album thumbnail saved to file"
