#!/usr/bin/python3

import json

def main():

    with open("datacenter.json", "r") as datacenter:
        datacenterstr = datacenter.read()

        datacenterdict = json.loads(datacenterstr) # gives a dict

        print(datacenterdict["row1"])

        with open("datacenter.json", "r") as datacenter:
            datacentershort = json.load(datacenter) # loads file directly, forms a dict
        print(type(datacentershort)) # Will show this is a dict



main()
