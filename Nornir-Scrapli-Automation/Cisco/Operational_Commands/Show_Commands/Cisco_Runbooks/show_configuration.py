from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="/home/jwilliams/Automation/Nornir-Scrapli-Automation/Cisco/Cisco_Inventory/config_file.yaml")

def write_configuration(task):
    start_config = task.run(task=send_command, command="show start")
    task.host['facts'] = start_config.scrapli_response.textfsm_parse_output()
    configuration = task.host['facts']
    rprint(configuration)
    

show_configuration = nr.run(task=write_configuration)


