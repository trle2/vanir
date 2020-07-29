from episerver.vanir.options_parser import OptionsParser

option_parser = OptionsParser()
args = option_parser.parse()
args.func(args)

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