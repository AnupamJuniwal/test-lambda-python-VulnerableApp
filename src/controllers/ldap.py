# import ldap
from ldap3 import Server, Connection
from ldap3.core.exceptions import LDAPSocketOpenError

handler_name = 'ldap'

def handler(args):
    type, uid = args
    switcher = {
        # 'ldap': ldap_ldap,
        'ldap3': ldap_ldap3
    }
    data = switcher[type](uid, args)
    return data

# def ldap_ldap(uid, _args):
#     try:
#         conn = ldap.initialize("ldap://127.0.0.1:8090/")
#         conn.simple_bind("bob", "secret")
#         treebase = "dc=example,dc=org"
#         attrs = ["sn", "objectclass"]
#         filter = "(|(uid={}))".format(uid)
#         print("filter query: {}".format(filter))
#         ldap_result_id = conn.search(base=treebase, scope=ldap.SCOPE_SUBTREE, filterstr=filter, attrlist=attrs)
#         result_set = []
#         while 1:
#             result_type, result_data = conn.result(ldap_result_id, 0)
#             if (result_data == []):
#                 break
#             else:
#                 ## here you don't have to append to a list
#                 ## you could do whatever you want with the individual entry
#                 ## The appending to list is just for illustration.
#                 if result_type == ldap.RES_SEARCH_ENTRY:
#                     result_set.append(result_data)
#         print("result : {}".format(result_set))
#         return result_set
#     except ldap.SERVER_DOWN as e:
#         print("Excpetion in ldap_ldap : {}".format(e))
#         return "Please check if LDAP server is running or not, try running server using command 'python3 ldap_server.py'"

def ldap_ldap3(uid, _args):
    try:
        server = Server('127.0.0.1:8090')
        conn = Connection(server, user="bob", password='secret')
        conn.bind()
        treebase = "dc=example,dc=org"
        attrs = ["sn", "objectclass"]
        filter = "(|(uid={}))".format(uid)
        print("filter query: {}".format(filter))
        conn.search(treebase, filter, attributes=attrs)
        print(conn.entries)
        return conn.entries
    except LDAPSocketOpenError as e:
        print("Excpetion in ldap_ldap3 : {}".format(e))
        return "Please check if LDAP server is running or not, try running server using command 'python3 ldap_server.py'"
