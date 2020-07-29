import subprocess

class AddResourceCommand:
    def execute(self, args):
        print('Run "terraform init"')
        template_location = f"templates/{args.type}/{args.template}"
        terraform_init = subprocess.run(['terraform', 'init', template_location], stdout = subprocess.PIPE, universal_newlines=True)
        print(terraform_init.stdout)
        
        print('Run "terraform plan"')
        terraform_run = subprocess.run(['terraform', 'plan', f"-var-file={args.resource_values}", template_location], stdout = subprocess.PIPE, universal_newlines=True)
        print(terraform_run.stdout)

        print('Run "terraform apply"')
        terraform_apply = subprocess.run(['terraform', 'apply', '-auto-approve', f"-var-file={args.resource_values}", template_location], stdout = subprocess.PIPE, universal_newlines=True)
        print(terraform_apply.stdout)