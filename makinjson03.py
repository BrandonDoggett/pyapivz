#!/usr/bin/python3

import json

def main():
    hitchhikers = [{"name":"zaphod beetlebrox","species":"betelgeusian"},{"name":"author dent","species":"human"}]

    with open("galaxyguide.json", "w") as zfile:
        json.dump(hitchhikers, zfile)


main()
