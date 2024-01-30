# CorePy

This Python script is designed to gather essential system information and convert it into a JSON format. It utilizes various modules to retrieve details about the operating system, network configuration, and hardware specifications.

## Prerequisites

CorePy uses the following modules:

- `platform`
- `socket`
- `re`
- `uuid`
- `json`
- `psutil`
- `logging`

## Usage

1. Open a terminal or command prompt
2. Navigate to the directory containing the script
3. Run the script using the command: `python corepy.py`

## System Information Collected

CorePy gathers the following system information:

- **Platform**: Operating system name
- **Platform Release**: Release version of the operating system
- **Platform Version**: Version information of the operating system
- **Architecture**: Machine architecture (e.g., 'x86_64')
- **Hostname**: Hostname of the machine
- **IP Address**: IP address of the machine
- **MAC Address**: MAC address of the machine
- **Processor**: Processor information
- **RAM**: Total RAM in gigabytes (GB)

## Output

CorePy outputs the system information in JSON format, making it easy to integrate into other applications or store for future reference.

Note: If any exceptions occur during the process of gathering system information, they will be logged using the `logging` module.

Feel free to modify the script to suit your specific requirements or integrate it into other projects.
