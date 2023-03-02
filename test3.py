#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Peter
#
# Created:     29-11-2014
# Copyright:   (c) Peter 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib.request



def main():
    print("Hi Peter")
    GetAktier()


def GetAktier():
    print("GetAktier")
    f = urllib.request.urlopen('http://www.svt.se/svttext/tv/pages/203.html')
    print(f.read(2000))

main()
