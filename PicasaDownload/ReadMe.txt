PicasaDownload is a set of console scipts which allows to download content from Picasa webservice.
Apart from downloading photos, it can also be used to save limited types of metadata like photo summary,comments,gps coordinates stored to EXIF or separate text file. 
Album information and setting can be also stored.


Limitations:
- video download not yet supported (cannot be done via Python GoogleAPI)
- album photocover can only be saved as cropped photo

Scripts:
PicasaDownloader.py - script to download Picasa content, albums list can be specified as per url or as file with full urls. Each line should consist one album. 

GetAlbumsUrl.py - script to get links of albums from selected Picasa account. List can be done manually py creating file with urls to albums - one url per line.



Hints:
- check config.txt for parameters to fill in. It is easier this way than in CLI
- check -h for possible input parameters
- to reuse configuration parameters use config.txt
- input parameters overwrites those from config.txt
- download content will be stored in place pointed at "WorkingDirectory", directory named as album
- in case of non-english characters there is an option to do convertion to ASCII range. Might be helpful when local filesystem has problems with creating directory with unsupported characters
- multiple albums download can be achived by using list of urls generated by GetAlbumsUrl.py
- in case of using non OS compatible charactes in Picasa (eg. national special letter in filenames and albums,comments and photo and album summary) ConvertToAscii can set to standardise character set. Still it is possible to hold orginal character set for further usage (eg. Picasa upload). Anyway it is best to store them in EXIF.
