import subprocess

import argparse

from episerver.vanir.options import Options
from episerver.vanir.environment.command_handler import CommandHandler
from episerver.vanir.environment.resource import CommandHandler

# parse args
options = Options()
parser = argparse.ArgumentParser(description='Resource management CLI.')
parser.add_argument('module', choices=['enviroment', 'resource'])
args = parser.parse_args(namespace=options)
parser.add_argument('command', choices=['add', 'delete'])
parser.add_argument('-n', '--name', required=True, help='An environment that hold all related resources. Currently map to a resource group.')
parser.add_argument('-l', '--location', required=True, help='Location on the environment.')
parser.add_argument('-r', '--resource-type', required=True, help='The type of the resource. Accepts 2 values: resource/environment.')
parser.add_argument('-t', '--resource-template', required=True, help='The template of the resource.')
parser.add_argument('-v', '--resource-values', help='The value file for resource template.')

args = parser.parse_args(namespace=options)

if options.module == 'environment':
   command_handler = CommandHandler()
   command_handler.handle(options.name, options.command, options.location)
elif options.module == 'resource':
   resource = Resource()
   


# template_location = f"templates/{options.resource_type}/{options.resource_template}"

# # terraform
# print('Run "terraform init"')
# terraform_init = subprocess.run(['terraform', 'init', template_location], stdout = subprocess.PIPE, universal_newlines=True)
# print(terraform_init.stdout)

# print('Run "terraform plan"')
# terraform_run = subprocess.run(['terraform', 'plan', f"-var-file={options.resource_values}", template_location], stdout = subprocess.PIPE, universal_newlines=True)
# print(terraform_run.stdout)

# print('Run "terraform apply"')
# terraform_apply = subprocess.run(['terraform', 'apply', '-auto-approve', f"-var-file={options.resource_values}", template_location], stdout = subprocess.PIPE, universal_newlines=True)
# print(terraform_apply.stdout)