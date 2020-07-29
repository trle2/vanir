import subprocess

class DeleteResourceCommand:
    def execute(self, args):
        print('Run "terraform init"')
        template_location = f"templates/{args.type}/{args.template}"
        terraform_init = subprocess.run(['terraform', 'init', template_location], stdout = subprocess.PIPE, universal_newlines=True)
        print(terraform_init.stdout)
        
        print('Run "terraform plan -destroy"')
        terraform_run = subprocess.run(['terraform', 'plan', '-destroy', template_location], stdout = subprocess.PIPE, universal_newlines=True)
        print(terraform_run.stdout)

        print('Run "terraform destroy"')
        terraform_apply = subprocess.run(['terraform', 'destroy', '-auto-approve', template_location], stdout = subprocess.PIPE, universal_newlines=True)
        print(terraform_apply.stdout)