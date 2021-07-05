import src.controllers.file_access as file_access
import src.controllers.file as file
import src.controllers.ldap as ldap
import src.controllers.mongo as mongo
import src.controllers.mysql as mysql
import src.controllers.rce as rce
import src.controllers.rci as rci
import src.controllers.rxss as rxss
import src.controllers.ssrf as ssrf
import src.controllers.xpath as xpath

handlers = [
    file_access,
    file,
    ldap,
    mongo,
    mysql,
    rce,
    rci,
    rxss,
    ssrf,
    xpath,
]

handler_dic={}

for module in handlers:
    handler_dic[module.handler_name]=module.handler