'''
Created on 22-03-2013

@author: j00zef.git@gmail.com
'''
import argparse
import sys
sys.path.append('Libs/')
import SaveToFile
import InitSetup
import SaveContent
import Utils

Flags = {}
Flags = InitSetup.SetFlags(InitSetup.ReadConfigFile('config.txt'),  InitSetup.ArgumentParsing(argparse.ArgumentParser()))


Utils.SetProxy(Flags)


gd_client = Utils.Autorize(Flags)

Utils.CreateWorkingDirectory(Flags)

AlbumList = Utils.GetAlbumList(Flags)
albums = Utils.GetFeed(gd_client.GetUserFeed(user=Flags['PicasaUser']))

if len(albums.entry) == 0:
    print "There are no albums to download or PicasaUser " + Flags['PicasaUser'] + " is not known."

albumCounter=1
for AlbumUrl in AlbumList:

    for album in albums.entry:
        # compare by album name derived from url - splits album name from url, split output from ?string with
        if Utils.GetProperUrlPart(album.link[1].href) == AlbumUrl:
            albumid = album.gphoto_id.text

            if Flags['ConvertToAscii'] == True or Flags['ConvertToAscii'] == 'Names':
                album.title.text = Utils.ConvertToAscii(album.title.text)

            dir_name = Utils.CrateAlbumDirectory(Utils.RemoveForbiddenCharsFromName(album.title.text), Flags)

            print "#####"
            print "Processing: " + album.title.text
            print "Album "+str(albumCounter)+" / "+str(len(AlbumList))
            print "#####"

            SaveToFile.SaveAlbumInfoToFile(album,  dir_name, Flags)
            SaveToFile.SaveAlbumThumbToFile(album, dir_name, Flags)

            photos = Utils.GetFeed(gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s?imgmax = d' % (Flags['PicasaUser'], albumid)))  # fetch photo list from given albumID
            FileCounter = 1  # counter used also for preserving file ordering from album

            for photo in photos.entry:

                photo.title.text = Utils.RemoveForbiddenCharsFromName(photo.title.text)

                if len(photo.media.content) > 1 and photo.media.content[1].medium == 'video':

                    SaveContent.SaveVideo(photo, dir_name, Flags)
                    SaveContent.SaveVideoTitle(photo, dir_name, Flags)

                    comments = Utils.GetFeed(gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s/photoid/%s?kind = comment' % (Flags['PicasaUser'], albumid, photo.gphoto_id.text)))
                    SaveContent.SaveCommentsToFile(photo, dir_name, comments, Flags)

                else:

                    Utils.KeepFileOrder(FileCounter, photo, Flags)
                    SaveContent.SavePhoto(photo, dir_name, Flags)
                    SaveContent.SavePhotoTitle(photo, dir_name, Flags)
                    SaveContent.SavePhotoGps(photo, dir_name, Flags)

                    comments = Utils.GetFeed(gd_client.GetFeed('/data/feed/api/user/%s/albumid/%s/photoid/%s?kind = comment' % (Flags['PicasaUser'], albumid, photo.gphoto_id.text)))
                    SaveContent.SaveCommentsToFile(photo, dir_name, comments, Flags)

                    FileCounter += 1

            break

print "Done!"
