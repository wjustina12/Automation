from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint 

nr = InitNornir(config_file="/home/jwilliams/Automation/Nornir-Scrapli-Automation/Cisco/Cisco_Inventory/config_file.yaml")

def show_ip_interface_brief(task):
    interface_object = task.run(task=send_command, command="show ip interface brief")
    task.host['facts'] = interface_object.scrapli_response.genie_parse_output()
    interfaces = task.host['facts']
    rprint(interfaces)

interface_response = nr.run(task=show_ip_interface_brief)