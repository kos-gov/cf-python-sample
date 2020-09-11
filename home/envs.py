import os
import json


def got_apps_env():
    if os.getenv('VCAP_APPLICATION') != None:
        apps = os.getenv('VCAP_APPLICATION', None)
    else:
        f = open('jcap_app.json', 'r')
        apps = str(f.read())
        f.close()

    return apps


def gto_svcs_env():
    if os.getenv('VCAP_SERVICES') != None:
        svcs = os.getenv('VCAP_SERVICES', None)
    else:
        f = open('jcap_services.json', 'r')
        svcs = str(f.read())
        f.close()

    return svcs


def get_apps():
    cfapps = got_apps_env()

    # loaded json contains a dictionary, not a string
    parsed_json = json.loads(cfapps)

    if 'VCAP_APPLICATION' in parsed_json:
        s = json.dumps(parsed_json['VCAP_APPLICATION'])
        # print("VCAP_APPLICATION ==> ", s)
        parsed_json = json.loads(s)

    cfapps = {}

    if 'application_name' in parsed_json:
        cfapps['application_name'] = parsed_json['application_name']

    if 'instance_index' in parsed_json:
        cfapps['instance_index'] = parsed_json['instance_index']
    else:
        cfapps['instance_index'] = "0"

    if 'limits' in parsed_json:
        cfapps['mem'] = parsed_json['limits']['mem']
        cfapps['disk'] = parsed_json['limits']['disk']

    if 'space_name' in parsed_json:
        cfapps['space_name'] = parsed_json['space_name']

    if 'uris' in parsed_json:
        cfapps['application_uris'] = ', '.join(parsed_json['uris'])

    # for key, value in cfapps.items():
    #    print("cfapps ==> ", key, ":", value)

    return cfapps


def get_svcs():
    cfsvcs = gto_svcs_env()

    # loaded json contains a dictionary, not a string
    parsed_json = json.loads(cfsvcs)

    if 'VCAP_SERVICES' in parsed_json:
        s = json.dumps(parsed_json['VCAP_SERVICES'])
        print("VCAP_SERVICES ==> ", s)
        parsed_json = json.loads(s)

    cfsvcs = {}

    svc_name = next(iter(parsed_json), "")

    if svc_name:
        cfsvcs['cfservicename'] = svc_name

        if svc_name in parsed_json:
            s = json.dumps(parsed_json[svc_name])
            s = s[1:]
            s = s[:-1]
            #    print("VCAP_SERVICES ==> ", s)
            parsed_json = json.loads(s)

            if 'name' in parsed_json:
                cfsvcs['name'] = parsed_json['name']

            if 'plan' in parsed_json:
                cfsvcs['plan'] = parsed_json['plan']

            # for key, value in cfsvcs.items():
            #    print("cfsvcs ==> ", key, ":", value)

    return cfsvcs
