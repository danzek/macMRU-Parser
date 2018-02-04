#!/usr/bin/env python
"""
Copyright (c) 2017, Station X Labs, LLC
All rights reserved.

Contributions adding CSV output by Dan O'Day <d@4n68r.com>

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Station X Labs, LLC nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL STATION X LABS, LLC BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import argparse
import fnmatch
import os
import plistlib
import sys
import uuid
from argparse import RawTextHelpFormatter
from time import gmtime, strftime

from mac_alias import Alias
from mac_alias import Bookmark

from macmru.bundleddependency import ccl_bplist
from macmru import __version__ as ver, _hrule_width


def BLOBParser_human(blob):
    # As described in:
    # http://mac-alias.readthedocs.io/en/latest/bookmark_fmt.html
    # http://mac-alias.readthedocs.io/en/latest/alias_fmt.html
    if args.blob_parse_human == True:
        print '-' * _hrule_width
        print "Human Readable Parsed BLOB:"
        try:
            b = Bookmark.from_bytes(blob)
            print "\tBookmark BLOB: Volume Name [0x2010]: \t\t" + b.get(0x2010,default=None)
            print "\tBookmark BLOB: Volume Path [0x2002]: \t\t" + str(b.get(0x2002,default=None))
            print "\tBookmark BLOB: Volume Flags [0x2020]: \t\t" + str(b.get(0x2020,default=None))
            print "\tBookmark BLOB: Volume is Root FS [0x2030]: \t" + str(b.get(0x2030,default=None))
            print "\tBookmark BLOB: Volume UUID [0x2011]: \t\t" + str(b.get(0x2011,default=None))
            print "\tBookmark BLOB: Volume Size [0x2012]: \t\t" + str(b.get(0x2012,default=None))
            print "\tBookmark BLOB: Volume Creation Date [0x2013]: \t" + str(b.get(0x2013,default=None))
            print "\tBookmark BLOB: Volume URL [0x2005]: \t\t" + str(b.get(0x2005,default=None))
            print "\tBookmark BLOB: Volume Bookmark [0x2040]: \t" + str(b.get(0x2040,default=None))
            print "\tBookmark BLOB: Volume Mount Point [0x2050]: \t" + str(b.get(0x2050,default=None))
            print "\tBookmark BLOB: Security Extension [0xf080]: \t" + str(b.get(0xf080,default=None))
            print "\tBookmark BLOB: Security Extension [0xf081]: \t" + str(b.get(0xf081,default=None))
            print ""
            print "\tBookmark BLOB: Target Path [0x1004]: \t\t" + str(b.get(0x1004,default=None))
            print "\tBookmark BLOB: Target CNID Path [0x1005]: \t" + str(b.get(0x1005,default=None))
            print "\tBookmark BLOB: Containing Folder Index [0xc001]:" + str(b.get(0xc001,default=None))
            print "\tBookmark BLOB: Target Creation Date [0x1040]: \t" + str(b.get(0x1040,default=None))
            print "\tBookmark BLOB: Target Flags [0x1010]: \t\t" + str(b.get(0x1010,default=None))
            print "\tBookmark BLOB: Target Filename [0x1020]: \t" + str(b.get(0x1020,default=None))
            print ""
            print "\tBookmark BLOB: Creator Username [0xc011]: \t" + str(b.get(0xc011,default=None))
            print "\tBookmark BLOB: Creator UID [0xc012]: \t\t" + str(b.get(0xc012,default=None)) 
            print ""
            
            print "\tBookmark BLOB: Unknown [0x1003]: \t\t" + str(b.get(0x1003,default=None))
            print "\tBookmark BLOB: Unknown [0x1054]: \t\t" + str(b.get(0x1054,default=None))
            print "\tBookmark BLOB: Unknown [0x1055]: \t\t" + str(b.get(0x1055,default=None))
            print "\tBookmark BLOB: Unknown [0x1056]: \t\t" + str(b.get(0x1056,default=None))
            print "\tBookmark BLOB: Unknown [0x1101]: \t\t" + str(b.get(0x1101,default=None))
            print "\tBookmark BLOB: Unknown [0x1102]: \t\t" + str(b.get(0x1102,default=None))
            print "\tBookmark BLOB: TOC Path [0x2000]: \t\t" + str(b.get(0x2000,default=None))
            print "\tBookmark BLOB: Unknown [0x2070]: \t\t" + str(b.get(0x2070,default=None))
            
            print "\tBookmark BLOB: File Reference Flag [0xd001]: \t" + str(b.get(0xd001,default=None))
            print "\tBookmark BLOB: Creation Options [0xd010]: \t" + str(b.get(0xd010,default=None))
            print "\tBookmark BLOB: URL Length Array [0xe003]: \t" + str(b.get(0xe003,default=None))
            print "\tBookmark BLOB: Localized Name (?) [0xf017]: \t" + str(b.get(0xf017,default=None))
            print "\tBookmark BLOB: Unknown [0xf022]: \t\t" + str(b.get(0xf022,default=None))

            if b.get(0xf020,default=None):

                icon_uuid = uuid.uuid4()
                print icon_uuid
                
                filename = "ICNS_file_" + str(icon_uuid) + ".icns"

                saveICNS = open(filename,'w')
                saveICNS.write(b.get(0xf020,default=None).bytes)
                saveICNS.close()

                print "\tBookmark BLOB: ICNS (Icon) File [0xf020]: \tICNS File Saved in: " + filename

        except:
            pass

        try:
            a = Alias.from_bytes(blob)
            print "\tAlias BLOB: Alias Version: \t\t" + str(a.version)
            print "\tAlias BLOB: Target Filename: \t\t" + a.target.filename
            print "\tAlias BLOB: Target File CNID: \t\t" + str(a.target.cnid)
            print "\tAlias BLOB: Target Carbon Path: \t" + a.target.carbon_path
            print "\tAlias BLOB: Target POSIX Path: \t\t" + a.target.posix_path
            print "\tAlias BLOB: Target Creation Date: \t" + str(a.target.creation_date)
            print "\tAlias BLOB: Target Creator Code: \t" + a.target.creator_code
            print "\tAlias BLOB: Target Type Code: \t\t" + a.target.type_code
            print "\tAlias BLOB: Target Folder Name: \t" + a.target.folder_name
            print "\tAlias BLOB: Target Folder CNID: \t" + str(a.target.folder_cnid)
            if a.target.kind == 0:
                print "\tAlias BLOB: Target Kind: \t\tFile" 
            elif a.target.kind == 1:
                print "\tAlias BLOB: Target Kind: \t\tFolder" 
            print ""
            print "\tAlias BLOB: Levels From: \t\t" + str(a.target.levels_from)
            print "\tAlias BLOB: Levels To: \t\t\t" + str(a.target.levels_to)
            print "\tAlias BLOB: User Home Prefix Length: \t" + str(a.target.user_home_prefix_len)
            print ""
            print "\tAlias BLOB: Volume Name: \t\t" + a.volume.name
            print "\tAlias BLOB: Volume Creation Date: \t" + str(a.volume.creation_date)
            print "\tAlias BLOB: Volume Filesystem Type: \t" + a.volume.fs_type
            print "\tAlias BLOB: Volume Disk Type: \t\t" + str(a.volume.disk_type)
            print "\tAlias BLOB: Volume Attribute Flags: \t" + str(a.volume.attribute_flags)
            print "\tAlias BLOB: Volume Filesystem ID: \t" + str(a.volume.fs_id)
            print ""
            print "\tAlias BLOB: Volume AppleShare Information: \t" + a.volume.appleshare_info
            print "\tAlias BLOB: Volume Driver Name: \t" + str(a.volume.driver_name)
            print "\tAlias BLOB: Volume POSIX Path: \t" + str(a.volume.posix_path)
            print "\tAlias BLOB: Volume Disk Image Alias: \t" + a.volume.disk_image_alias
            print "\tAlias BLOB: Volume Creation Date: \t" + str(a.volume.creation_date)
            print "\tAlias BLOB: Volume Dialup Information: \t" + str(a.volume.dialup_info)
            print "\tAlias BLOB: Volume Network Mount Information: \t" + str(a.volume.network_mount_info)
            print ""
            print "\tAlias BLOB: Extra: \t" + str(a.extra)
            print "\tAlias BLOB: App Info: \t" + str(a.appinfo)
            print "\tAlias BLOB: Apple Share Info - Server: \t" + str(a.AppleShareInfo.server)
            print "\tAlias BLOB: Apple Share Info - User: \t" + str(a.AppleShareInfo.user)
            print "\tAlias BLOB: Apple Share Info - Zone \t" + str(a.AppleShareInfo.zone)
        except:
            pass
        print '-' * _hrule_width


def ParseSFL(MRUFile):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)
        plist_objects = ccl_bplist.deserialise_NsKeyedArchiver(plist, parse_whole_structure=True)

        try:
            if plist_objects["root"]["NS.objects"][1]["NS.keys"][0] == "com.apple.LSSharedFileList.MaxAmount":
                numberOfItems = plist_objects["root"]["NS.objects"][1]["NS.objects"][0]
                print "Max number of recent items in this plist: " + str(numberOfItems)
        except:
            pass

        if plist_objects["root"]["NS.keys"][2] == "items":
            items = plist_objects["root"]["NS.objects"][2]["NS.objects"] 
            for n,item in enumerate(items):
                try:
                    name = item["name"]
                except:
                    name = "No 'name' Key"

                print"    [Item Number: " + str(n) +  " | Order: " + str(item["order"]) + "] Name:'" + name + "' (URL:'" + item["URL"]['NS.relative'] + "')"
                
                #UNCOMMENT FOR UNIQUE IDENTIFIER HEXDUMP
                #print '-' * _hrule_width
                #print "Hexdump of Unique Identifier: "
                #print hexdump.hexdump(item["uniqueIdentifier"]["NS.uuidbytes"])
                #print '-' * _hrule_width
                if "LSSharedFileList.RecentHosts" not in MRUFile:
                    blob = item["bookmark"]
                    BLOBParser_raw(blob)
                    BLOBParser_human(blob) 
                    BLOB_hex(blob)
    except:
        print "Cannot open file: " + MRUFile
 
def ParseSFL2(MRUFile):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)
        plist_objects = ccl_bplist.deserialise_NsKeyedArchiver(plist, parse_whole_structure=True)

        try:
            if plist_objects["root"]["NS.objects"][1]["NS.keys"][0] == "com.apple.LSSharedFileList.MaxAmount":
                numberOfItems = plist_objects["root"]["NS.objects"][1]["NS.objects"][0]
                print "Max number of recent items in this plist: " + str(numberOfItems)
        except:
            pass

        if plist_objects["root"]["NS.keys"][0] == "items":
            items = plist_objects["root"]["NS.objects"][0]["NS.objects"] 

            for n,item in enumerate(items):
                attribute_keys = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.keys"]
                attribute_values = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.objects"]
                attributes = dict(zip(attribute_keys,attribute_values))
                try:
                    uuid = attributes["uuid"]
                except:
                    uuid = "No 'UUID' Attribute"
                
                try:
                    visability = str(attributes["visibility"])
                except:
                    visability = "No 'Visability' Attribute"

                try:
                    name = attributes["Name"]
                except:
                    name = "No 'Name' Attribute (Use BLOB parser for name)"

                print "    [Item Number: " + str(n) +  " | (UUID:'" + uuid + "') | Visibility: " + visability + "] Name:'" + name + "'"

                #Unknown "CustomItemProperties" - Only seen blank, uncomment to see details.
                #print attributes["CustomItemProperties"]
                if "LSSharedFileList.RecentHosts" not in MRUFile:
                    blob = attributes["Bookmark"]
                    BLOBParser_raw(blob)
                    BLOBParser_human(blob) 
                    BLOB_hex(blob)
    except:
        print "Cannot open file: " + MRUFile

def ParseSFL2_FavoriteVolumes(MRUFile):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)
        plist_objects = ccl_bplist.deserialise_NsKeyedArchiver(plist, parse_whole_structure=True)

        print "Item number has no bearing upon time of usage."
        print "Plist Properties:"
        if plist_objects["root"]["NS.keys"][1] == "properties":

            properties_keys = plist_objects["root"]["NS.objects"][1]["NS.keys"]
            properties_values = plist_objects["root"]["NS.objects"][1]["NS.objects"]
            properties = dict(zip(properties_keys,properties_values))
            for key in properties:
                print  "    " + key + ": " + str(properties[key])

        if plist_objects["root"]["NS.keys"][0] == "items":
            items = plist_objects["root"]["NS.objects"][0]["NS.objects"] 

            for n,item in enumerate(items):
                attribute_keys = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.keys"]
                attribute_values = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.objects"]
                attributes = dict(zip(attribute_keys,attribute_values))
                try:
                    uuid = attributes["uuid"]
                except:
                    uuid = "No 'UUID' Attribute"
                
                try:
                    visibility = str(attributes["visibility"])
                except:
                    visibility = "No 'Visability' Attribute"

                try:
                    name = attributes["Name"]
                except:
                    name = "No 'Name' Attribute (Use BLOB parser for name)"

                print "\n    [Item Number: " + str(n) +  " | (UUID:'" + uuid + "') | Visibility: " + visibility + "] Name: '" + name + "'"

                if attributes["CustomItemProperties"]:
                    CIP_keys = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.objects"][1]["NS.keys"]
                    CIP_values = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.objects"][1]["NS.objects"]
                    CIP_attributes = dict(zip(CIP_keys,CIP_values))
                    print "\tCustomItemProperties:"
                    for key in CIP_attributes:
                        print  "\t  " + key + ": " + str(CIP_attributes[key])

                if "LSSharedFileList.RecentHosts" not in MRUFile:
                    blob = attributes["Bookmark"]
                    BLOBParser_raw(blob)
                    BLOBParser_human(blob) 
                    BLOB_hex(blob)
    except:
        print "Cannot open file: " + MRUFile

def ParseLSSharedFileListPlist(MRUFile):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)
        print "Max number of recent items in this plist:: " + str(plist["RecentDocuments"]["MaxAmount"])
        print "[MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
        for n,item in enumerate(plist["RecentDocuments"]["CustomListItems"]):
            print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"
            blob = item["Bookmark"]
            BLOBParser_raw(blob)
            BLOBParser_human(blob) 
            BLOB_hex(blob)
    except:
        print "Cannot open file: " + MRUFile

def ParseRecentItemsPlist(MRUFile):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)
        try:
            print "Recent Applications (Max number of recent items in this key: " + str(plist["RecentApplications"]["MaxAmount"]) + ")"
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n,item in enumerate(plist["RecentApplications"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"
 
                blob = item["Bookmark"]
                BLOBParser_raw(blob)
                BLOBParser_human(blob) 
                BLOB_hex(blob)        
        except:
            print "No Recent Applications"
            
        try:
            print "Recent Documents (Max number of recent items in this key: " + str(plist["RecentDocuments"]["MaxAmount"]) + ")"
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n,item in enumerate(plist["RecentDocuments"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"

                blob = item["Bookmark"]
                BLOBParser_raw(blob)
                BLOBParser_human(blob) 
                BLOB_hex(blob)
        except:
            print "No Recent Documents"
        
        try:
            print "Recent Servers (Max number of recent items in this key: " + str(plist["RecentServers"]["MaxAmount"]) + ")"   
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n,item in enumerate(plist["RecentServers"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"

                blob = item["Bookmark"]
                BLOBParser_raw(blob)
                BLOBParser_human(blob) 
                BLOB_hex(blob)
        except:
            print 'No Recent Servers'

        try:    
            print "Recent Hosts (Max number of recent items in this key: " + str(plist["Hosts"]["MaxAmount"]) + ")"   
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n,item in enumerate(plist["Hosts"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'" + " - URL: " + item["URL"] + "'"
        except:
            print "No Recent Hosts"

        try:
            print "Recent Applications (Legacy) (Max number of recent items in this key: " + str(plist["pythonApplications"]["MaxAmount"]) + ")"
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n,item in enumerate(plist["Applications"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"
                blob = item["Alias"]
                BLOBParser_raw(blob)
                BLOBParser_human(blob) 
                BLOB_hex(blob)

        except:
            print "No Recent Applications (Legacy)"
            
        try:
            print "Recent Documents (Legacy) (Max number of recent items in this key: " + str(plist["Documents"]["MaxAmount"]) + ")"
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n,item in enumerate(plist["Documents"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"
                blob = item["Alias"]
                BLOBParser_raw(blob)
                BLOBParser_human(blob) 
                BLOB_hex(blob)
        except:
            print "No Recent Documents (Legacy)"
        
        try:
            print "Recent Servers (Legacy) (Max number of recent items in this key: " + str(plist["Servers"]["MaxAmount"]) + ")"   
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n,item in enumerate(plist["Servers"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"
                blob = item["Alias"]
                BLOBParser_raw(blob)
                BLOBParser_human(blob) 
                BLOB_hex(blob)
        except:
            print 'No Recent Servers (Legacy)'
    except:
        print "Cannot open file: " + MRUFile

def ParseFinderPlist(MRUFile):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)

        print "Parsing FXRecentFolders Key"
        print "[MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
        try:
            for n,item in enumerate(plist["FXRecentFolders"]):
                print "    [Item Number: " + str(n) + "] '" + item["name"] + "'"

                try:
                    blob = item["file-bookmark"]
                    BLOBParser_raw(blob)
                    BLOBParser_human(blob) 
                    BLOB_hex(blob)
                except:
                    pass

                try:
                    blob = item["file-data"]["_CFURLAliasData"]
                    BLOBParser_raw(blob)
                    BLOBParser_human(blob) 
                    BLOB_hex(blob)
                except:
                    pass
        except:
            pass

        print "\nParsing FXDesktopVolumePositions Key"
        print "Item number has no bearing upon time of usage."
        try:
            for n,item in enumerate(plist["FXDesktopVolumePositions"]):
                item_split = item.split('_0x')
                item_timestamp = "0x" + item_split[1]
                if float.fromhex(item_timestamp) > 0:
                    volume_creation = gmtime(int(float.fromhex(item_timestamp) + 978307200))
                    volume_creation_ts = strftime("%m-%d-%Y %H:%M:%S", volume_creation) 
                    print "    [Item Number: " + str(n) + "] Volume Created: " + volume_creation_ts+ "  Volume Name: '" + item_split[0] + "'\tOriginal Key: '" + item + "'"
                else:
                    print "    [Item Number: " + str(n) + "] Volume Created: None\t\t   Volume Name: '" + item_split[0] + "'\tOriginal Key: '" + item + "'"
        except:
            pass

    except:
        print "Cannot open file: " + MRUFile

def ParseSidebarlistsPlist(MRUFile):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)

        print "Parsing 'systemitems' Key (Only --blob_hex works)"
        print "Item number has no bearing upon time of usage."
        try:
            for n,item in enumerate(plist["systemitems"]['VolumesList']):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "' EntryType: " + str(item['EntryType'])

                try:
                    print "\tSpecialID: " + str(item['SpecialID'])
                except:
                    pass

                try:
                    print "\tVisibility: " + str(item['Visibility'])
                except:
                    pass

                try:
                    print "\tFlags: " + str(item['Flags'])
                except:
                    pass

                try:
                    blob = plist["systemitems"]['VolumesList'][n]['Alias']
                    #BLOBParser_raw(blob)
                    #BLOBParser_human(blob) 
                    BLOB_hex(blob)
                except:
                    pass
        except:
           pass

        print "Parsing 'favorites' Key (Only --blob_hex works)"
        print "Item number has no bearing upon time of usage."
        try:
            for n,item in enumerate(plist["favorites"]['VolumesList']):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "' EntryType: " + str(item['EntryType'])

                try:
                    print "\tSpecialID: " + str(item['SpecialID'])
                except:
                    pass

                try:
                    print "\tVisibility: " + str(item['Visibility'])
                except:
                    pass

                try:
                    print "\tFlags: " + str(item['Flags'])
                except:
                    pass

                try:
                    blob = plist["systemitems"]['VolumesList'][n]['Alias']
                    #BLOBParser_raw(blob)
                    #BLOBParser_human(blob) 
                    BLOB_hex(blob)
                except:
                    pass
        except:
           pass
    except:
       print "Cannot open file: " + MRUFile

def ParseMSOffice2016Plist(MRUFile):
    try:
        plistfile = plistlib.readPlist(MRUFile)
        for n,item in enumerate(plistfile):
            print "    [Item: " + item + "]"
            try:
                print "        UUID: " + plistfile[item]["kUUIDKey"]
            except:
                print "        UUID: No 'kUUIDKey' Key"

            bookmarkdata = plistfile[item]["kBookmarkDataKey"]
            for attr, blob in bookmarkdata.__dict__.iteritems():
                BLOBParser_raw(blob)
                BLOBParser_human(blob) 
                BLOB_hex(blob)
    except:
        print "Cannot open file: " + MRUFile

def ParseMSOffice2011Plist(MRUFile):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)

        print "[MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"

        def FunkyMSTime(raw_accessdate):
            global accessdate
            thebytes = raw_accessdate.encode("hex")[4:12]
            macosts =  int("".join(reversed([thebytes[i:i+2] for i in range(0, len(thebytes), 2)])),16)
            epochtime = gmtime(macosts - 2082844800)
            accessdate = strftime("%m-%d-%Y %H:%M:%S", epochtime)
    except:
        print "Cannot open file: " + MRUFile

    try:
        print "Microsoft Word MRUs: (Use --blob_parse_human or --blob_parse_raw for file paths in BLOBs.)"
        try:
            for n,item in enumerate(plist["14\File MRU\MSWD"]):

                raw_accessdate = item["Access Date"]
                FunkyMSTime(raw_accessdate)

                print "    [Item Number: " + str(n) + "] - Access Date (UTC): " + accessdate + ""

                blob = item["File Alias"]
                BLOBParser_raw(blob)
                BLOBParser_human(blob) 
                BLOB_hex(blob)
        except:
            print "    No key for 14\File MRU\MSWD"
    except:
        pass

    try:                   
        print "Microsoft Excel MRUs: (Use --blob_parse_human or --blob_parse_raw for file paths in BLOBs.)"
        try:
            for n,item in enumerate(plist["14\File MRU\XCEL"]):

                raw_accessdate = item["Access Date"]
                FunkyMSTime(raw_accessdate)

                print "    [Item Number: " + str(n) + "] - Access Date (UTC): " + accessdate + ""
                
                blob = item["File Alias"]
                BLOBParser_raw(blob)
                BLOBParser_human(blob) 
                BLOB_hex(blob) 
        except:
            print "    No key for 14\File MRU\XCEL"
    except:
        pass

    try:
        print "Microsoft Powerpoint MRUs: (Use --blob_parse_human or --blob_parse_raw for file paths in BLOBs.)"
        try:
            for n,item in enumerate(plist["14\File MRU\PPT3"]):

                raw_accessdate = item["Access Date"]
                FunkyMSTime(raw_accessdate)

                print "    [Item Number: " + str(n) + "] - Access Date (UTC): " + accessdate + ""

                blob = item["File Alias"]
                BLOBParser_raw(blob)
                BLOBParser_human(blob) 
                BLOB_hex(blob) 
        except:
            print "    No key for 14\File MRU\PPT3"
    except:
        pass   

def SpotlightShortcuts(MRUFile):
    try:
        plistfile = plistlib.readPlist(MRUFile)
        print "[Spotlight Shortcuts are shown with a UTC timestamp]"
        for n,item in enumerate(plistfile):
            print "    [Shortcut: '" + item + "']"
            try:
                print "        Display Name: \t\t" + plistfile[item]["DISPLAY_NAME"]
            except:
                print "        Display Name: No 'DISPLAY_NAME' Key"
            
            try:
                print "        Last Used Timestamp: \t" + str(plistfile[item]["LAST_USED"])
            except:
                print "        Last Used Timestamp: No 'LAST_USED' Key"
            
            try:
                print "        URL: \t\t\t" + plistfile[item]["URL"]
            except:
                print "        URL: No 'URL' Key"      
    except:
        print "Cannot open file: " + MRUFile


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='\
    Parse the Mac MRU (Most Recently Used) Plist Files \
    \n\n\tMac MRU File Locations: \
    \n\t- /Users/<username>/Library/Preferences/<bundle_id>.LSSharedFileList.plist\
    \n\t- /Users/<username>/Library/Preferences/com.apple.finder.plist\
    \n\t- [10.10-] /Users/<username>/Library/Preferences/com.apple.recentitems.plist\
    \n\t- [10.11+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.ApplicationRecentDocuments/<bundle_id>.sfl\
    \n\t- [10.11+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/RecentApplications.sfl\
    \n\t- [10.11+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/RecentDocuments.sfl\
    \n\t- [10.11+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/RecentServers.sfl\
    \n\t- [10.11+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/RecentHosts.sfl\
    \n\t- [10.13+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.ApplicationRecentDocuments/<bundle_id>.sfl2\
    \n\t- [10.13+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.RecentApplications.sfl2\
    \n\t- [10.13+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.RecentDocuments.sfl2\
    \n\t- [10.13+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.RecentServers.sfl2\
    \n\t- [10.13+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.RecentHosts.sfl2\
    \n\t- MS Office 2011 - /Users/<username>/Library/Preferences/com.microsoft.office.plist\
    \n\t- MS Office 2016 - /Users/<username>/Library/Containers/com.microsoft.<app>/Data/Library/Preferences/com.microsoft.<app>.securebookmarks.plist \
    \n\t- Spotlight Shortcuts - /Users/<username>/Library/Application Support/com.apple.spotlight.Shortcuts \
    \n\t- [10.12-]/Users/<username>/Library/Preferences/com.apple.sidebarlists.plist \
    \n\t- [10.13+] /Users/<username>/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.FavoriteVolumes.sfl2\ \
    \n \
    \n\tAuthor:     Sarah Edwards | @iamevltwin | mac4n6.com | oompa@csh.rit.edu \
    \n\tCSV Output: Dan O\'Day     | @4n68r      | 4n68r.com  | d@4n68r.com'
        , prog='macmru.py'
        , formatter_class=RawTextHelpFormatter)
    parser.add_argument("--csv", help="Create CSV output to file provided as parameter")
    parser.add_argument('--blob_hex', action='store_true', help="Include hex dump of Bookmark BLOBs in standard output (can very verbose!)")
    parser.add_argument('--blob_parse_human', action='store_true', help="Parse the BLOB data in human readable format (can very verbose!)")
    parser.add_argument('--blob_parse_raw', action='store_true', help="Parse the BLOB data in raw format (can very verbose!)")
    parser.add_argument('MRU_DIR')
    args = parser.parse_args()

    MRUDirectory = args.MRU_DIR

    print "###### MacMRU Parser v{0} ######".format(ver)

    # validate MRU directory
    if not MRUDirectory or MRUDirectory is None or not os.path.exists(MRUDirectory):
        print "Invalid file path (path provided does not exist)"
        sys.exit(1)

    csv_output = False
    csv_path = None
    if args.csv and args.csv is not None and len(args.csv.strip()) > 0:
        csv_output = True
        csv_path = args.csv

    for root, dirs, filenames in os.walk(MRUDirectory):
        for f in filenames:
            MRUFile = os.path.join(root, f)
            print "Parsing: " + MRUFile

            if os.path.isfile(MRUFile):
                if f.endswith(".sfl") and not fnmatch.fnmatch(f,'*Favorite*.sfl') and not fnmatch.fnmatch(f,'*Project*.sfl') and not fnmatch.fnmatch(f,'*iCloudItems*.sfl'):
                    ParseSFL(MRUFile)
                elif f.endswith(".sfl2") and not fnmatch.fnmatch(f,'*Favorite*.sfl2') and not fnmatch.fnmatch(f,'*Project*.sfl2') and not fnmatch.fnmatch(f,'*iCloudItems*.sfl2'):
                    ParseSFL2(MRUFile)
                elif f.endswith("FavoriteVolumes.sfl2"):
                    ParseSFL2_FavoriteVolumes(MRUFile)
                elif f.endswith(".LSSharedFileList.plist"):
                    ParseLSSharedFileListPlist(MRUFile)
                elif f == "com.apple.finder.plist":
                    ParseFinderPlist(MRUFile)
                elif f == "com.apple.sidebarlists.plist":
                    ParseSidebarlistsPlist(MRUFile)
                elif f == "com.apple.recentitems.plist":
                    ParseRecentItemsPlist(MRUFile)
                elif f.endswith(".securebookmarks.plist"):
                    ParseMSOffice2016Plist(MRUFile)
                elif f == "com.microsoft.office.plist":
                    ParseMSOffice2011Plist(MRUFile)
                elif f == "com.apple.spotlight.Shortcuts":
                    SpotlightShortcuts(MRUFile)
                else:
                    print "Invalid MRU file"
            else:
                print "ERROR: Bad file name or path: {0}".format(MRUFile)

            print '=' * _hrule_width
