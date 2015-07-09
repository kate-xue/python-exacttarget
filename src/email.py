import etapi
import os
import glob

if __name__ == '__main__':
    et = etapi.ExactTargetAPI('kate_jba', 'kate@jba2015', 'https://webservice.s6.exacttarget.com/etframework.wsdl')
    et.init_client()
    # MID
    et.set_client_id(6370050)

    et_namespace = 'welcome'
    # Folder ID
    et_folder = 28424
    segment = 'list'
    lookup_folder = 'welcome/*.html'

    # et.get_contents('2014-10/mods', et_folder)

    for filepath in glob.glob(lookup_folder):
        et.create_contents(et_namespace, segment, filepath, et_folder)