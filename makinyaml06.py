#!/usr/bin/python3

import yaml

def main():
    hitchhikers = [{"name":"zaphod beetlebrox","species":"betelgeusian"},{"name":"author dent","species":"human"}]

    mystr =  yaml.dump(hitchhikers)
       
    print(mystr)

main()
