#!/usr/bin python3

import subprocess
import optparse
import re
import time

def red(text):
    print(f"\033[31m{text}\033[0m")

def green(text):
    print(f"\033[32m{text}\033[0m")


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC address")
    parser.add_option("-m", "--mac", dest="mac", help="New MAC address to be Changed")

    (options, arguments) = parser.parse_args()

    if not options.interface :
        parser.error(red("[+] please specify an interface use --help for more info"))
    if not options.mac :
        parser.error(red("[+] please specify an Mac Address use --help for more info"))
    else :
        return options


def mac_changer (interface,mac) :
    print(f"[+] changing mac address to interface \033[32m{interface}\033[0m  as : \033[34m{mac}\033[0m")
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", mac])
    subprocess.run(["ifconfig", interface, "up"])
    time.sleep(1)
    print(f"[+] Your MAC address is Changed to \033[32m{mac}\033[0m")
    time.sleep(.5)
    subprocess.run(["ifconfig", interface])

def check_result (options):
    ifconfig_result =subprocess.check_output(['ifconfig',options.interface])
    re_result = re.search(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", str(ifconfig_result))

    # re_result = re.search(f"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    current_mac = re_result.group(0)

    if current_mac == options.mac :
        print(f"\033[0m[+] MAC address changed Succesfully to \033[32m{str(options.mac)}")
    else:
        red("[+] MAC address change Failed")

options = get_arguments()
mac_changer (options.interface,options.mac)
check_result (options)