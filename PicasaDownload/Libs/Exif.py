'''
Created on 05-04-2013

@author: j00zef.git@gmail.com
'''
import pyexiv2
import math


def GpsDecToRational(GpsDec):
    degrees = math.trunc(GpsDec)
    minutes = math.trunc(abs(GpsDec) * 60) % 60
    seconds = abs(GpsDec) * 3600 % 60
    return (pyexiv2.Rational(degrees * 60 + minutes, 60), pyexiv2.Rational(seconds * 100, 6000), pyexiv2.Rational(0, 1))


def SaveGpsToExif(latitude, longitude, filename):
    metadata = pyexiv2.ImageMetadata(filename)
    metadata.read()
    metadata['Exif.GPSInfo.GPSLatitude'] = GpsDecToRational(latitude)
    metadata['Exif.GPSInfo.GPSLongitude'] = GpsDecToRational(longitude)
    metadata.write()


def SaveTitleToExif(ImageDescription, filename):
    metadata = pyexiv2.ImageMetadata(filename)
    metadata.read()
    metadata['Exif.Image.ImageDescription'] = ImageDescription
    metadata['Xmp.dc.description'] = ImageDescription
    metadata['Iptc.Application2.Caption'] = [ImageDescription]
    metadata.write()
