

PicasaUpload is a set of scripts to allow massive album uploads to Picasa webservice.
Apart from plain upload, it can automaticly set album properties and info, set photos summary and restore comments. 
Additional information (album properties,photo meta data) are fetched from EXIF or 
separate text files (types and content same as in albums download by PicasaDownload)

Limitations:
- video uploading is not supported yet
- not possible autmaticly set album's cover

Authentication:
  - Visit Google Developers Console: https://console.developers.google.com 
  - Create credidential under API -> Credidentials
  - Download JSON file
  - Specify JSON file in ClientSecret parameter
  - upon first attempt, follow on screan instructions.
  - authentication token is stored in user_credidentials.txt, if you which to connect to different Picasa account, remove this file beforehand 

Script:
AlbumsUploader.py - main uploader script

Hints:
- check -h for possible input parameters
- to reuse configuration parameters use config.txt
- input parameters overwrites those from config.txt
- you can use text file with paths to multiple albums for mass upload. Specify that file as AlbumListToUpload parameter in config.txt
- to only update metadata, remove photos from album directory leaving txt files with meta
