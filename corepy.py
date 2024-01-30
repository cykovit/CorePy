import platform  ## module to get informations about the system's platform
import socket  ## module for network-related functions
import re  ## module for regular expressions
import uuid  ## module to generate and manipulate UUIDs and obtain the MAC address
import json  ## module for JSON serialization and deserialization
import psutil  ## module to access system details and process utilities
import logging  ## module for logging exception messages

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

## function to convert system information to JSON format
def system_info_to_json():
    try:
        info = get_system_info()  ## get system information
        return json.dumps(info)  ## convert the information to JSON format
    except Exception as e:
        logging.exception(e)  ## log any exceptions that occur during the process

print(system_info_to_json())