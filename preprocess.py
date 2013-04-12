import json
import os

from pyproj import Proj
p = Proj(proj='merc',ellps='WGS84') # use kwargs

las = json.load(open('las.json'))

out = {}
for fname in os.listdir('las'):
    if not fname.endswith('.geojson'): continue
    try:
        j = json.load(open(os.path.join('las', fname)))
    except ValueError: continue
    if 'error' in j:
        continue
    c = j['coordinates']
    if j['type'] ==  'MultiPolygon': polygons = c
    else: polygons = [c]


    ons = las[fname[:-8]]['codes']['ons']
    out[ons] = []
    for polygon in polygons:
        out_poly = []
        for co in polygon[0]:
            x,y = p(*co)
            out_poly.append([x/100000, y/100000 - 65])
        out[ons].append(out_poly)
json.dump(out, open('out.json', 'w'))
