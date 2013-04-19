'''
Created on 24-03-2013

@author:  j00zef.git@gmail.com
'''

import SaveToFile
import Utils
import Exif


def SavePhoto(photo, dir_name, Flags):
    if Flags['SavePhoto'] == True:
        if Flags['ConvertToAscii'] == True or Flags['ConvertToAscii'] == 'Names':
            photo.title.text = Utils.ConvertToAscii(photo.title.text)
        SaveToFile.SaveFile(photo.content.src, dir_name + photo. title.text)  # saves photo/movie to selected directory
        print photo.title.text + ': file saved'


def SavePhotoTitle(photo, dir_name, Flags):
    if photo.media.description.text != None:

        if Flags['ConvertToAscii'] == True or Flags['ConvertToAscii'] == 'Text':
            photo.media.description.text = Utils.ConvertToAscii(photo.media.description.text)

        if Flags['SaveTitleToFile'] == True:
            SaveToFile.SaveTitle(photo.media.description.text, dir_name + photo.title.text)  # saves media description(title) to text file
            print photo.title.text + ': title saved to file'

        if Flags['SaveTitleToExif'] == True and Flags['SavePhoto'] == True:
            Exif.SaveTitleToExif(photo.media.description.text, dir_name + photo.title.text)
            print photo.title.text + ': title saved to exif'


def SaveVideoTitle(photo, dir_name, Flags):
    if photo.media.description.text != None:
        if Flags['SaveTitleToFile'] == True:
            SaveToFile.SaveTitle(photo.media.description.text, dir_name + photo.title.text)  # saves media description(title) to text file
            print photo.title.text + ': title saved to file'


def SavePhotoGps(photo, dir_name, Flags):
    if len(photo.geo.location()) > 0:
        if Flags['SaveGPSToFile'] == True:
            SaveToFile.SaveGps(photo.geo.location()[0], photo.geo.location()[1], dir_name + photo.title.text)  # saves media gps coordinates to file
            print photo.title.text + ': gps coordinates saved to file'
        if Flags['SaveGPSToExif'] == True and Flags['SavePhoto'] == True:
            Exif.SaveGpsToExif(photo.geo.location()[0], photo.geo.location()[1], dir_name + photo.title.text)
            print photo.title.text + ': gps coordinates saved to exif'


def SaveCommentsToFile(photo, dir_name, comments, Flags):
    if Flags['SaveCommentsToFile'] == True and len(comments.entry) > 0:
        CommentText = ''
        for comment in comments.entry:
            CommentText += comment.title.text + ':' + comment.content.text + '\n'
        if Flags['ConvertToAscii'] == True or Flags['ConvertToAscii'] == 'Text':
            CommentText = Utils.ConvertToAscii(CommentText)

        SaveToFile.SaveComment(CommentText, dir_name + photo.title.text)  # saves media user comments coordinates to file
        print photo.title.text + ': comments saved to file'


def SaveVideo(photo, dir_name, Flags):
    if Flags['SavePhoto'] == True:
        SaveToFile.SaveVideoToFile('Video download is not supported', dir_name + photo.title.text + ".txt")
        print photo.title.text + ': video file download not supported'
