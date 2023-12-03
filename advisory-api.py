import sys, json
from advisorymod import advisorymod

# status, t = advisorymod.getLatestAdvisories(5)
# if(t.get('error')): sys.exit()

config = {}
mappings = {}
with open('config.json', 'r') as f:
    config = json.load(f)
with open('advisory-mappings.json', 'r') as f:
    mappings = json.load(f)

advisorymod.putMappings(config, mappings)


# latest = t.get('data')

# bulk = []

# for adv in latest:
#     advId = adv.get('ICS-CERT_Number')
#     status, data = advisorymod.getAdvisoryById(advId)
#     print(status)
#     if(status != 200): continue
#     bulk.append(data.get('data'))

# with open('advisories/advisories.json', 'w') as f:
#     f.write(json.dumps(bulk))