from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import os.path
from os import makedirs
from datetime import date
from rich import print as rprint 

nr = InitNornir(config_file="/home/jwilliams/Automation/Nornir-Scrapli-Automation/Cisco/Cisco_Inventory/config_file.yaml")

def write_to_file(task):
   start_config = task.run(task=send_command, command="show start")
   
   path = f"/home/jwilliams/Automation/Nornir-Scrapli-Automation/Cisco/Configuration_Backup/{date.today()}"
   file_name = f"{task.host}_configuration"
   absolute_name = os.path.join(path, file_name)
   path_check = os.makedirs(path, exist_ok=True)

   with open(absolute_name, mode='w') as config_file:
       config_file.write(start_config)

show_result = nr.run(task=write_to_file)
print_result(show_result)