PicasaUpload is a set of scripts to allow massive album uploads to Picasa webservice.
Apart from plain upload, it can automaticly set album properties and info, set photos summary and restore comments. Additional information (album properties,photo meta data) are fetched from EXIF or separate text files (types and content same as in albums download by PicasaDownload)

Limitations:
- video uploading is not supported (Python GoogleAPI does not support it)
- not possible autmaticly set album's cover


Script:
AlbumsUploader.py - main uploader script

Hints:
- check -h for possible input parameters
- to reuse configuration parameters use config.txt
- input parameters overwrites those from config.txt
- check help how to mass upload albums using file with urls or directory path, specified in AlbumListToUpload parameter

