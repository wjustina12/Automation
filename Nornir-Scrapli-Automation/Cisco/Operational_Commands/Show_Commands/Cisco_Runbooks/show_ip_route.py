from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint 

nr = InitNornir(config_file="/home/jwillliams/Automation/Nornir-Scrapli-Automation/Cisco/Cisco_Inventory/config_file.yaml")

def show_ip_route(task):
    route_object = task.run(task=send_command, command="show ip route")
    task.host["facts"] = route_object.scrapli_response.genie_parse_output()
    route = task.host["facts"]
    rprint(route)

route_result = nr.run(task=show_ip_route)