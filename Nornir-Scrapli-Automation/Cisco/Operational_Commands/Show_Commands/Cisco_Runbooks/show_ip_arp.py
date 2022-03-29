from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint 

nr = InitNornir(config_file="/home/jwilliams/Automation/Nornir-Scrapli-Automation/Cisco/Cisco_Inventory/config_file.yaml")

def show_arp(task):
    arp_object = task.run(task=send_command, command="show ip route")
    task.host['facts'] = arp_object.scrapli_response.genie_parse_output()
    arp = task.host['facts']
    rprint(arp)

arp_response = nr.run(task=show_arp)