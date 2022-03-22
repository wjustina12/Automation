from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="/home/jwilliams/Nornir-Scrapli-Automation/Cisco/Cisco_Inventory/config_file.yaml")

def show_version(task):
    version = task.run(task=send_command, command="show version")

version = nr.run(task=show_version)

print_result(version)