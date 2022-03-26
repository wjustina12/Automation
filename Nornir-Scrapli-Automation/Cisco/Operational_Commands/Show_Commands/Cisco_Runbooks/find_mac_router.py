from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint 

nr = InitNornir(config_file="Inventory/config.yaml")

rprint("[bold green]Hello! Welcome to MAC hunter, your tool to find a MAC address with the associated IP address![/bold green]")
ip_lookup = input("What's the IP address?\n").strip()

def get_mac(task):
    global mac_dictionary
    mac_dictionary = {}

    arp_object = task.run(task=send_command, command="show ip arp")
    task.host["facts"] = arp_object.scrapli_response.genie_parse_output()
    arp = task.host["facts"]["interfaces"]
    
    for key,interfaces in arp.items():
        ip_interfaces = interfaces['ipv4']['neighbors']
        
        for key,value in ip_interfaces.items():
            ip_address = value['ip']
            mac_address = value["link_layer_address"]

            if ip_address != mac_dictionary.keys():
                mac_dictionary[ip_address] = mac_address
            elif ip_address == mac_dictionary.keys():
                pass


    
def return_mac():
    mac_dictionary2 = mac_dictionary
    if ip_lookup in mac_dictionary2.keys():
        rprint(f"The IP address [bold green]{ip_lookup}[/bold green] has the mac address of [bold green]{mac_dictionary2[ip_lookup]}[/bold green]")
    elif ip_lookup not in mac_dictionary2.keys():
        print(f"The IP {ip_lookup} doesn't have a MAC address associated with it. Is the IP address correct?")

mac_result = nr.run(task=get_mac)
return_mac()


