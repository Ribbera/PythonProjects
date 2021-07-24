import subprocess 
import optparse
import re

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface", dest = "interface", help="Interface para cambiar MAC")
    parser.add_option("-m","--mac", dest = "new_mac", help="Nueva direccion MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Porfavor indicar un interfaz, usa --help para mas informacion")
    elif not options.new_mac:
        parser.error("[-] Porfavor indicar un Direccion MAC, usa --help para mas informacion")
    return options

def change_mac(interface,new_mac):
    print("[+] Cambiando MAC Address for " + options.interface + " to " + options.new_mac)


    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_addres_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_addres_search_result:
        return mac_addres_search_result.group(0)

    else:
        print("[-] No pudimos leer la direccion MAC")

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface,options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] Direccion MAC cambio a " + current_mac)
else:
    print("[-] Direccion Mac no Cambio")
