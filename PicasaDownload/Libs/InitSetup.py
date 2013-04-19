'''
Created on 23-03-2013
@author: j00zef.git@gmail.com
'''

#import argparse
import os
import ast


def SetFlags(Settings, Arguments):

    Flags = {'KeepFileOrder': True,
    'SavePhoto': True,
    'SaveTitleToExif': True,
    'SaveTitleToFile': False,
    'SaveGPSToExif': True,
    'SaveGPSToFile': False,
    'SaveCommentsToFile': True,
    'SaveAlbumInfoToFile': True,
    'SaveAlbumThumbToFile': True,
    'PicasaAlbumsVisability': 'all',
    'WorkingDirectory': 'albums',
    'Username': None,
    'Password': None,
    'PicasaUser': None,
    'PicasaAlbumsUrlFile': None,
    'AlbumUrl': None,
    'Proxy': None,
    'ConvertToAscii': False}

    for i in Settings:
        for j in Flags:
            if i == j and Settings[i] != None:
                Flags[i] = Settings[i]

    for i in Arguments:
        for j in Flags:
            if i == j and Arguments[i] != None:
                Flags[i] = Arguments[i]

    if Flags['PicasaUser'] == None:
        Flags['PicasaUser'] = Flags['Username']

    if Flags['Username'] == None or Flags['Password'] == None:
        print "Username or Password variables not set!"
        exit()

    return (Flags)


def ArgumentParsing(parser):

    parser.add_argument("-dir", "--WorkingDirectory", dest="WorkingDirectory", help="Sets working directory where albums will be downloaded,if not specified current directory will be used.Relative or absolute path")

    parser.add_argument("-usr", "--Username", dest="Username", help="Sets google username to authenticate in gdata service.")
    parser.add_argument("-psw", "--Password", dest="Password", help="Sets google user's password to authenticate in gdata service.")

    parser.add_argument("-pu", "--PicasaUser", dest="PicasaUser", help="Sets Picasa username to download albums.If not specified, Username will be used.")

    parser.add_argument("-au", "--AlbumUrl", dest="AlbumUrl", help="Direct link of album url to be downloaded.")
    parser.add_argument("-af", "--PicasaAlbumsUrlFile", dest="PicasaAlbumsUrlFile", help="File with album urls from one user to download.")

    parser.add_argument("-vi", "--PicasaAlbumsVisability", dest="PicasaAlbumsVisability", choices=["all", "public", "protected", "private"], help="Specify which albums to download,usable only if you are the owner of Picasa albums,otherwise Public will be used. Default = All")

    parser.add_argument("-order", "--KeepFileOrder", dest="KeepFileOrder", choices=["True", "False"], help="Sets whether photo filenames will preserve order same as in album, done by adding counter prefix to filename. Default = True ")

    parser.add_argument("-sp", "--SavePhoto", dest="SavePhoto", choices=["True", "False"], help="Sets whether to save a photos from albums. Default = True")

    parser.add_argument("-te", "--SaveTitleToExif", dest="SaveTitleToExif", choices=["True", "False"], help="Sets whether save photo title as file's exif.Default = True")
    parser.add_argument("-tf", "--SaveTitleToFile", dest="SaveTitleToFile", choices=["True", "False"], help="Sets whether save photo title as textfile. Default = False")

    parser.add_argument("-ge", "--SaveGPSToExif", dest="SaveGPSToExif", choices=["True", "False"], help="Sets whether save gps data as file's exif. Default = True")
    parser.add_argument("-gf", "--SaveGPSToFile", dest="SaveGPSToFile", choices=["True", "False"], help="Sets whether save gps data as textfile. Default = False")

    parser.add_argument("-cf", "--SaveCommentsToFile", dest="SaveCommentsToFile", choices=["True", "False"], help="Sets whether save comments as textfile. Default = True")

    parser.add_argument("-aif", "--SaveAlbumInfoToFile", dest="SaveAlbumInfoToFile", choices=["True", "False"], help="Sets whether save album info to file. Default = True")
    parser.add_argument("-atf", "--SaveAlbumThumbToFile", dest="SaveAlbumThumbToFile", choices=["True", "False"], help="Sets whether save album thumbnail. Default = True")
    parser.add_argument("-pr", "--Proxy", dest="Proxy", help="Sets proxy if needed, format server:port.")
    parser.add_argument("-ca", "--ConvertToAscii", dest="ConvertToAscii", choices=["True", "False", "Names", "Text"], help="Convert all special/locacl letters to ASCII equivalent - this includes album name,filename,title and comments descriptions. Default = True ")

    args = parser.parse_args()
    arguments = {}

    for property, value in vars(args). iteritems():
        arguments[property] = value

    return(ConvertToBool(arguments))


def ReadConfigFile(filename):
    settings = {}
    if os.path.isfile(filename):
        lines = [line.strip() for line in open(filename)]
        for i in lines:
            i = i.replace("'", '')
            i = i.replace('"', '')
            i = ''.join(i.split())
            if len(i.split("=")[1]) == 0:
                settings[i.split("=")[0]] = None
            else:
                settings[i.split("=")[0]] = i.split("=")[1]

        if settings['PicasaAlbumsVisability'] != None:
            settings['PicasaAlbumsVisability'] = settings['PicasaAlbumsVisability'].lower()

        if settings['PicasaAlbumsVisability'] != 'public' and settings['PicasaAlbumsVisability'] != 'private' and settings['PicasaAlbumsVisability'] != 'protected' and settings['PicasaAlbumsVisability'] != 'all':
            settings['PicasaAlbumsVisability'] = 'all'

        if settings['ConvertToAscii'] != None:
            settings['ConvertToAscii'] = settings['ConvertToAscii'].capitalize()
            if settings['ConvertToAscii'] != 'True' and settings['ConvertToAscii'] != 'False' and settings['ConvertToAscii'] != 'Names'and settings['ConvertToAscii'] != 'Text':
                settings['ConvertToAscii'] = None

        return(ConvertToBool(settings))


def ConvertToBool(Flags):
    for items in ['KeepFileOrder', 'SavePhoto', 'SaveTitleToExif', 'SaveTitleToFile', 'SaveGPSToExif', 'SaveGPSToFile', 'SaveCommentsToFile', 'SaveAlbumInfoToFile', 'SaveAlbumThumbToFile']:
        try:
            Flags[items] = ast.literal_eval(Flags[items].capitalize())
        except:
            Flags[items] = None
    return(Flags)
