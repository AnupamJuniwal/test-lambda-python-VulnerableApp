import xml.etree.ElementTree as ET
import lxml.etree
import io

USERS_XML = """<?xml version="1.0" encoding="utf-8"?><users><user id="0"><username>admin</username><name>admin</name><surname>admin</surname><password>7en8aiDoh!</password></user><user id="1"><username>dricci</username><name>dian</name><surname>ricci</surname><password>12345</password></user><user id="2"><username>amason</username><name>anthony</name><surname>mason</surname><password>gandalf</password></user><user id="3"><username>svargas</username><name>sandra</name><surname>vargas</surname><password>phest1945</password></user></users>"""


handler_name = 'ssrf'

def handler(args):
    type, q = args
    switcher = {
        'xml': xpath_xml,
        'lxml': xpath_lxml
    }
    data = switcher[type](q, args)
    return data

def xpath_xml(payload, _args):
    tree = ET.parse('employees.xml')
    root = tree.getroot()
    query = ".//employee/[firstName='%s']" % payload
    print("XPATH query executing : {}".format(query))
    elmts = root.findall(query)  # Noncompliant
    res = []
    print("Data found: ")
    for x in elmts:
        xmlstr = ET.tostring(x, encoding='utf8', method='xml')
        print("entry : {}".format(xmlstr))
        res.append(xmlstr)
    return res

def xpath_lxml(payload, _args):
    query = ".//user[name/text()='%s']" % payload
    print("XPATH query executing : {}".format(query))
    elmts = lxml.etree.parse(io.BytesIO(USERS_XML.encode())).xpath(query)
    res = []
    print("Data found: ")
    for x in elmts:
        xmlstr = lxml.etree.tostring(x)
        print("entry : {}".format(xmlstr))
        res.append(xmlstr)
    return res
