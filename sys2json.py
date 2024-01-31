import platform  ## module to get informations about the system's platform
import socket  ## module for network-related functions
import re  ## module for regular expressions
import uuid  ## module to generate and manipulate UUIDs and obtain the MAC address
import json  ## module for JSON serialization and deserialization
import psutil  ## module to access system details and process utilities
import logging  ## module for logging exception messages
import fade ## module to add faded color effect on ascii art title displayed when running the script
from colorama import Fore ## module to add color to "System Information in JSON format" print statement for better readability
from rich.console import Console ## importing the console class from the rich module for enhanced console output
from rich.table import Table ## importing the Table class from the rich module for creating and formatting tables in the console

def get_system_info():
    ## creating a dictionary to store system information
    info = {
        'platform': platform.system(),  ## operating system name 
        'platform-release': platform.release(),  ## release version of the operating system
        'platform-version': platform.version(),  ## version information of the operating system
        'architecture': platform.machine(),  ## machine architecture (e.g., 'x86_64')
        'hostname': socket.gethostname(),  ## hostname of the machine
        'ip-address': socket.gethostbyname(socket.gethostname()),  ## IP address of the machine
        'mac-address': ':'.join(re.findall('..', '%012x' % uuid.getnode())),  ## MAC address of the machine
        'processor': platform.processor(),  ## processor information
        'ram': f"{round(psutil.virtual_memory().total / (1024.0**3))}GB"  ## total RAM in gigabytes (GB)
    }
    return info

## function to iterate over the key-value pairs in the info dictionary and print each key-value pair in table format
def print_system_info(info):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("System", style="dim", width=20)
    table.add_column("Information")

    for key, value in info.items():
        table.add_row(key, str(value))

    console = Console()
    console.print(table)

## function to attempt to get system information using get_system_info() and convert the result to JSON format
def system_info_to_json():
    try:
        info = get_system_info() ## get system information
        return json.dumps(info, indent=4) ## convert the information to JSON format
    except Exception as e:
        logging.exception(e) ## log any exceptions that occur during the process

## fancy ascii art title + colors
title = '''
    _____              _____    ___  _____  _____  _   _ 
    /  ___|            / __  \  |_  |/  ___||  _  || \ | |
    \ `--.  _   _  ___ `' / /'    | |\ `--. | | | ||  \| |
    `--. \| | | |/ __|  / /      | | `--. \| | | || . ` |
    /\__/ /| |_| |\__ \./ /___/\__/ //\__/ /\ \_/ /| |\  |
    \____/  \__, ||___/\_____/\____/ \____/  \___/ \_| \_/
            __/ |                                        
            |___/              
'''

faded_text = fade.greenblue(title)
print(faded_text)

## get and print system information
system_info = get_system_info()
print_system_info(system_info)

## print system information in JSON format
json_info = Fore.LIGHTGREEN_EX + system_info_to_json()
print(f"\nSystem Information in JSON format:\n{json_info}")