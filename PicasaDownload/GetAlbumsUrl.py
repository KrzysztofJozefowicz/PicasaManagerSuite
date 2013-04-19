'''
Created on 23-03-2013

@author: j00zef.git@gmail.com
'''
import argparse
#import gdata.photos.service
import gdata


def GetAllAlbumsUrl(PicasaUser, PicasaAlbumsVisability, Username, Password):
    gd_client = gdata.photos.service.PhotosService()
    gd_client.email = Username
    gd_client.password = Password
    gd_client.source = 'PMS - Picasa Downloader'
    gd_client.ProgrammaticLogin()
    albums = gd_client.GetUserFeed(user=PicasaUser)

    AlbumList = []
    for album in albums.entry:
        if PicasaAlbumsVisability == album.access.text:
            AlbumList.append(album.link[1].href)

        if PicasaAlbumsVisability == 'all':
            AlbumList.append(album.link[1].href)

    return AlbumList


def SaveAllAlbumsUrl(AlbumList, PicasaAlbumsUrlFile):
    file = open(PicasaAlbumsUrlFile, 'wb')
    for i in AlbumList:
        file.write(i + '\r\n')
    file.close()


def SaveAllAlbumUsrlToFile(PicasaUser, PicasaAlbumsVisability, PicasaAlbumsUrlFile):
    SaveAllAlbumsUrl(GetAllAlbumsUrl(PicasaUser, PicasaAlbumsVisability, Username, Password), PicasaAlbumsUrlFile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-usr", "--Username", dest="Username", help="Sets google username to authenticate in gdata service.")
    parser.add_argument("-pwd", "--Password", dest="Password", help="Sets google user's password to authenticate in gdata service.")
    parser.add_argument("-pu", "--PicasaUser", dest="PicasaUser", help="Sets Picasa usersname to get album query.")
    parser.add_argument("-af", "--PicasaAlbumsUrlFile", dest="PicasaAlbumsUrlFile", help="Specify file with album urls to download.")
    parser.add_argument("-vi", "--PicasaAlbumsVisability", dest="PicasaAlbumsVisability", help="Specify which albums to download, when used with .")
    args = parser.parse_args()

    PicasaUser = args.PicasaUser
    PicasaAlbumsVisability = args.PicasaAlbumsVisability
    PicasaAlbumsUrlFile = args.PicasaAlbumsUrlFile
    Username = args.Username
    Password = args.Password

    gd_client = gdata.photos.service.PhotosService()
    gd_client.email = Username
    gd_client.password = Password
    gd_client.source = 'exampleCo-exampleApp-1'
    gd_client.ProgrammaticLogin()

    SaveAllAlbumUsrlToFile(PicasaUser, PicasaAlbumsVisability, PicasaAlbumsUrlFile)
    