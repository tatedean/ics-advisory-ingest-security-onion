import sys, requests, json
from advisorymod import advisorymod

status, t = advisorymod.getLatestAdvisories(5)
if(t.get('error')): sys.exit()

latest = t.get('data')

bulk = []

for adv in latest:
    advId = adv.get('ICS-CERT_Number')
    status, data = advisorymod.getAdvisoryById(advId)
    print(status)
    if(status != 200): continue
    bulk.append(data.get('data'))

with open('advisories/advisories.json', 'w') as f:
    f.write(json.dumps(bulk))