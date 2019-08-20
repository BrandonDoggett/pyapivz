#!/usr/bin/python3

import yaml

def main():
    hitchhikers = [{"name":"zaphod beetlebrox","species":"betelgeusian"},{"name":"author dent","species":"human"}]

    with open("zfile.yml", "w") as zfile:
        yaml.dump(hitchhikers, zfile)
       


main()
