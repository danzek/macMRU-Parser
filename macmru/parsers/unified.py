#!/usr/bin/env python
"""
macmru.parsers.unified module

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

from macmru.bundleddependency import ccl_bplist


def ParseSFL(MRUFile, opts):
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
            for n, item in enumerate(items):
                try:
                    name = item["name"]
                except:
                    name = "No 'name' Key"

                print"    [Item Number: " + str(n) + " | Order: " + str(
                    item["order"]) + "] Name:'" + name + "' (URL:'" + item["URL"]['NS.relative'] + "')"

                # UNCOMMENT FOR UNIQUE IDENTIFIER HEXDUMP
                # print '-' * _hrule_width
                # print "Hexdump of Unique Identifier: "
                # print hexdump.hexdump(item["uniqueIdentifier"]["NS.uuidbytes"])
                # print '-' * _hrule_width
                if "LSSharedFileList.RecentHosts" not in MRUFile:
                    blob = item["bookmark"]
                    csv_blob_data = opts.process_blob(blob)
                    if opts.csv_output and csv_blob_data:
                        # do something with csv data
                        pass
    except:
        print "Cannot open file: " + MRUFile


def ParseSFL2(MRUFile, opts):
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

            for n, item in enumerate(items):
                attribute_keys = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.keys"]
                attribute_values = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.objects"]
                attributes = dict(zip(attribute_keys, attribute_values))
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

                print "    [Item Number: " + str(
                    n) + " | (UUID:'" + uuid + "') | Visibility: " + visibility + "] Name:'" + name + "'"

                # Unknown "CustomItemProperties" - Only seen blank, uncomment to see details.
                # print attributes["CustomItemProperties"]
                if "LSSharedFileList.RecentHosts" not in MRUFile:
                    blob = attributes["Bookmark"]
                    csv_blob_data = opts.process_blob(blob)
                    if opts.csv_output and csv_blob_data:
                        # do something with csv data
                        pass
    except:
        print "Cannot open file: " + MRUFile


def ParseSFL2_FavoriteVolumes(MRUFile, opts):
    try:
        plistfile = open(MRUFile, "rb")
        plist = ccl_bplist.load(plistfile)
        plist_objects = ccl_bplist.deserialise_NsKeyedArchiver(plist, parse_whole_structure=True)

        print "Item number has no bearing upon time of usage."
        print "Plist Properties:"
        if plist_objects["root"]["NS.keys"][1] == "properties":

            properties_keys = plist_objects["root"]["NS.objects"][1]["NS.keys"]
            properties_values = plist_objects["root"]["NS.objects"][1]["NS.objects"]
            properties = dict(zip(properties_keys, properties_values))
            for key in properties:
                print  "    " + key + ": " + str(properties[key])

        if plist_objects["root"]["NS.keys"][0] == "items":
            items = plist_objects["root"]["NS.objects"][0]["NS.objects"]

            for n, item in enumerate(items):
                attribute_keys = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.keys"]
                attribute_values = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.objects"]
                attributes = dict(zip(attribute_keys, attribute_values))
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

                print "\n    [Item Number: " + str(
                    n) + " | (UUID:'" + uuid + "') | Visibility: " + visibility + "] Name: '" + name + "'"

                if attributes["CustomItemProperties"]:
                    CIP_keys = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.objects"][1]["NS.keys"]
                    CIP_values = plist_objects["root"]["NS.objects"][0]["NS.objects"][n]["NS.objects"][1]["NS.objects"]
                    CIP_attributes = dict(zip(CIP_keys, CIP_values))
                    print "\tCustomItemProperties:"
                    for key in CIP_attributes:
                        print  "\t  " + key + ": " + str(CIP_attributes[key])

                if "LSSharedFileList.RecentHosts" not in MRUFile:
                    blob = attributes["Bookmark"]
                    csv_blob_data = opts.process_blob(blob)
                    if opts.csv_output and csv_blob_data:
                        # do something with csv data
                        pass
    except:
        print "Cannot open file: " + MRUFile
