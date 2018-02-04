#!/usr/bin/env python
"""
macmru.parsers.plists module

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

import plistlib
from time import gmtime, strftime

from macmru.bundleddependency import ccl_bplist


def ParseLSSharedFileListPlist(MRUFile, opts):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)
        print "Max number of recent items in this plist:: " + str(plist["RecentDocuments"]["MaxAmount"])
        print "[MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
        for n, item in enumerate(plist["RecentDocuments"]["CustomListItems"]):
            print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"
            blob = item["Bookmark"]
            csv_blob_data = opts.process_blob(blob)
            if opts.csv_output and csv_blob_data:
                # do something with csv data
                pass
    except:
        print "Cannot open file: " + MRUFile


def ParseRecentItemsPlist(MRUFile, opts):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)
        try:
            print "Recent Applications (Max number of recent items in this key: " + str(
                plist["RecentApplications"]["MaxAmount"]) + ")"
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n, item in enumerate(plist["RecentApplications"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"

                blob = item["Bookmark"]
                csv_blob_data = opts.process_blob(blob)
                if opts.csv_output and csv_blob_data:
                    # do something with csv data
                    pass
        except:
            print "No Recent Applications"

        try:
            print "Recent Documents (Max number of recent items in this key: " + str(
                plist["RecentDocuments"]["MaxAmount"]) + ")"
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n, item in enumerate(plist["RecentDocuments"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"

                blob = item["Bookmark"]
                csv_blob_data = opts.process_blob(blob)
                if opts.csv_output and csv_blob_data:
                    # do something with csv data
                    pass
        except:
            print "No Recent Documents"

        try:
            print "Recent Servers (Max number of recent items in this key: " + str(
                plist["RecentServers"]["MaxAmount"]) + ")"
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n, item in enumerate(plist["RecentServers"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"

                blob = item["Bookmark"]
                csv_blob_data = opts.process_blob(blob)
                if opts.csv_output and csv_blob_data:
                    # do something with csv data
                    pass
        except:
            print 'No Recent Servers'

        try:
            print "Recent Hosts (Max number of recent items in this key: " + str(plist["Hosts"]["MaxAmount"]) + ")"
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n, item in enumerate(plist["Hosts"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'" + " - URL: " + item["URL"] + "'"
        except:
            print "No Recent Hosts"

        try:
            print "Recent Applications (Legacy) (Max number of recent items in this key: " + str(
                plist["pythonApplications"]["MaxAmount"]) + ")"
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n, item in enumerate(plist["Applications"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"
                blob = item["Alias"]
                csv_blob_data = opts.process_blob(blob)
                if opts.csv_output and csv_blob_data:
                    # do something with csv data
                    pass

        except:
            print "No Recent Applications (Legacy)"

        try:
            print "Recent Documents (Legacy) (Max number of recent items in this key: " + str(
                plist["Documents"]["MaxAmount"]) + ")"
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n, item in enumerate(plist["Documents"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"
                blob = item["Alias"]
                csv_blob_data = opts.process_blob(blob)
                if opts.csv_output and csv_blob_data:
                    # do something with csv data
                    pass
        except:
            print "No Recent Documents (Legacy)"

        try:
            print "Recent Servers (Legacy) (Max number of recent items in this key: " + str(
                plist["Servers"]["MaxAmount"]) + ")"
            print "MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
            for n, item in enumerate(plist["Servers"]["CustomListItems"]):
                print "    [Item Number: " + str(n) + "] '" + item["Name"] + "'"
                blob = item["Alias"]
                csv_blob_data = opts.process_blob(blob)
                if opts.csv_output and csv_blob_data:
                    # do something with csv data
                    pass
        except:
            print 'No Recent Servers (Legacy)'
    except:
        print "Cannot open file: " + MRUFile


def ParseFinderPlist(MRUFile, opts):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)

        print "Parsing FXRecentFolders Key"
        print "[MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"
        try:
            for n, item in enumerate(plist["FXRecentFolders"]):
                print "    [Item Number: " + str(n) + "] '" + item["name"] + "'"

                try:
                    blob = item["file-bookmark"]
                    csv_blob_data = opts.process_blob(blob)
                    if opts.csv_output and csv_blob_data:
                        # do something with csv data
                        pass
                except:
                    pass

                try:
                    blob = item["file-data"]["_CFURLAliasData"]
                    csv_blob_data = opts.process_blob(blob)
                    if opts.csv_output and csv_blob_data:
                        # do something with csv data
                        pass
                except:
                    pass
        except:
            pass

        print "\nParsing FXDesktopVolumePositions Key"
        print "Item number has no bearing upon time of usage."
        try:
            for n, item in enumerate(plist["FXDesktopVolumePositions"]):
                item_split = item.split('_0x')
                item_timestamp = "0x" + item_split[1]
                if float.fromhex(item_timestamp) > 0:
                    volume_creation = gmtime(int(float.fromhex(item_timestamp) + 978307200))
                    volume_creation_ts = strftime("%m-%d-%Y %H:%M:%S", volume_creation)
                    print "    [Item Number: " + str(
                        n) + "] Volume Created: " + volume_creation_ts + "  Volume Name: '" + item_split[
                              0] + "'\tOriginal Key: '" + item + "'"
                else:
                    print "    [Item Number: " + str(n) + "] Volume Created: None\t\t   Volume Name: '" + item_split[
                        0] + "'\tOriginal Key: '" + item + "'"
        except:
            pass

    except:
        print "Cannot open file: " + MRUFile


def ParseSidebarlistsPlist(MRUFile, opts):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)

        print "Parsing 'systemitems' Key (Only --blob_hex works)"
        print "Item number has no bearing upon time of usage."
        try:
            for n, item in enumerate(plist["systemitems"]['VolumesList']):
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
                    # todo -- why were first two commented out?
                    # BLOBParser_raw(blob)
                    # BLOBParser_human(blob)
                    # BLOB_hex(blob)  # todo -- I commented this out, refactor if only this is needed
                except:
                    pass
        except:
            pass

        print "Parsing 'favorites' Key (Only --blob_hex works)"
        print "Item number has no bearing upon time of usage."
        try:
            for n, item in enumerate(plist["favorites"]['VolumesList']):
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
                    # todo -- why were first two commented out?
                    # BLOBParser_raw(blob)
                    # BLOBParser_human(blob)
                    # BLOB_hex(blob)  # todo -- I commented this out, refactor if only this is needed
                except:
                    pass
        except:
            pass
    except:
        print "Cannot open file: " + MRUFile


def ParseMSOffice2016Plist(MRUFile, opts):
    try:
        plistfile = plistlib.readPlist(MRUFile)
        for n, item in enumerate(plistfile):
            print "    [Item: " + item + "]"
            try:
                print "        UUID: " + plistfile[item]["kUUIDKey"]
            except:
                print "        UUID: No 'kUUIDKey' Key"

            bookmarkdata = plistfile[item]["kBookmarkDataKey"]
            for attr, blob in bookmarkdata.__dict__.iteritems():
                csv_blob_data = opts.process_blob(blob)
                if opts.csv_output and csv_blob_data:
                    # do something with csv data
                    pass
    except:
        print "Cannot open file: " + MRUFile


def ParseMSOffice2011Plist(MRUFile, opts):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)

        print "[MRUs are listed from Newest to Oldest (ie: Item 0 - Item 9)]"

        def FunkyMSTime(raw_accessdate):
            global accessdate  # todo -- validate if needs to be declared outside this scope to be valid
            thebytes = raw_accessdate.encode("hex")[4:12]
            macosts = int("".join(reversed([thebytes[i:i + 2] for i in range(0, len(thebytes), 2)])), 16)
            epochtime = gmtime(macosts - 2082844800)
            accessdate = strftime("%m-%d-%Y %H:%M:%S", epochtime)
    except:
        print "Cannot open file: " + MRUFile

    try:
        print "Microsoft Word MRUs: (Use --blob_parse_human or --blob_parse_raw for file paths in BLOBs.)"
        try:
            for n, item in enumerate(plist["14\File MRU\MSWD"]):
                raw_accessdate = item["Access Date"]
                FunkyMSTime(raw_accessdate)

                print "    [Item Number: " + str(n) + "] - Access Date (UTC): " + accessdate + ""

                blob = item["File Alias"]
                csv_blob_data = opts.process_blob(blob)
                if opts.csv_output and csv_blob_data:
                    # do something with csv data
                    pass
        except:
            print "    No key for 14\File MRU\MSWD"
    except:
        pass

    try:
        print "Microsoft Excel MRUs: (Use --blob_parse_human or --blob_parse_raw for file paths in BLOBs.)"
        try:
            for n, item in enumerate(plist["14\File MRU\XCEL"]):
                raw_accessdate = item["Access Date"]
                FunkyMSTime(raw_accessdate)

                print "    [Item Number: " + str(n) + "] - Access Date (UTC): " + accessdate + ""

                blob = item["File Alias"]
                csv_blob_data = opts.process_blob(blob)
                if opts.csv_output and csv_blob_data:
                    # do something with csv data
                    pass
        except:
            print "    No key for 14\File MRU\XCEL"
    except:
        pass

    try:
        print "Microsoft Powerpoint MRUs: (Use --blob_parse_human or --blob_parse_raw for file paths in BLOBs.)"
        try:
            for n, item in enumerate(plist["14\File MRU\PPT3"]):
                raw_accessdate = item["Access Date"]
                FunkyMSTime(raw_accessdate)

                print "    [Item Number: " + str(n) + "] - Access Date (UTC): " + accessdate + ""

                blob = item["File Alias"]
                csv_blob_data = opts.process_blob(blob)
                if opts.csv_output and csv_blob_data:
                    # do something with csv data
                    pass
        except:
            print "    No key for 14\File MRU\PPT3"
    except:
        pass
