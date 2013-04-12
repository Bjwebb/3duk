import json, subprocess
import os

for k,v in json.load(open('las.json')).items():
    #print v['codes']['ons']
    if os.path.isfile('las/{0}.geojson'.format(v['id'])):
        print 'Skipping'
        continue
    subprocess.call('sleep 1s; curl "http://mapit.mysociety.org/area/{0}.geojson?simplify_tolerance=0.01" > las/{0}.geojson'.format(v['id']), shell=True)

