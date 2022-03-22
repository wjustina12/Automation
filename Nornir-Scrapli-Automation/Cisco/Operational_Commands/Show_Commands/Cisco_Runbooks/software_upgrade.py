from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="/home/jwilliams/Nornir-Scrapli-Automation/Cisco/Cisco_Inventory/config_file.yaml")

def show_version(task):
    version_object = task.run(task=send_command, command="show version")
    task.host["facts"] = version_object.scrapli_response.textfsm_parse_output()
    version = task.host["facts"]
    rprint(version)

version_response = nr.run(task=show_version)
