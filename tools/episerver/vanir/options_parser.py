import json
import argparse
from episerver.vanir.environment.add import AddEnvironmentCommand
from episerver.vanir.environment.delete import DeleteEnvironmentCommand
from episerver.vanir.resource.add import AddResourceCommand
from episerver.vanir.resource.delete import DeleteResourceCommand

class OptionsParser:
    def __init__(self):
            self.add_environment_command = AddEnvironmentCommand()
            self.delete_environment_command = DeleteEnvironmentCommand()
            self.add_resource_command = AddResourceCommand()
            self.delete_resource_command = DeleteResourceCommand()
    
    def parse(self):
        # parse args
        parser = argparse.ArgumentParser(description='Resource management CLI.')
        subparsers = parser.add_subparsers()

        # profile
        profile_parser = subparsers.add_parser('profile', help='Profile management.')
        profile_subparsers = profile_parser.add_subparsers()
        
        # add profile
        add_profile_parser = profile_subparsers.add_parser('add', help='Add new profile.')
        add_profile_parser.add_argument('-n', '--name', required=True, help='Name of the profile.')
        
        # delete profile
        add_profile_parser = profile_subparsers.add_parser('delete', help='Delete the profile.')
        add_profile_parser.add_argument('-n', '--name', required=True, help='Name of the profile.')
        
        # add profile
        add_profile_parser = profile_subparsers.add_parser('resources', help='List resources of the profile.')
        add_profile_parser.add_argument('-n', '--name', required=True, help='Name of the profile.')
        
        # resource
        resource_parser = subparsers.add_parser('resource', help='Resource management')
        resource_subparsers = resource_parser.add_subparsers()

        # add resource
        add_resource_parser = resource_subparsers.add_parser('add', help='Add new resource for environment.')
        add_resource_parser.add_argument('-t', '--type', required=True, choices=['individual', 'composite'], help='The type of the resource.')
        add_resource_parser.add_argument('-e', '--environment', required=True, help='The environment that hold the resource.')
        add_resource_parser.add_argument('-l', '--template', required=True, help='The template of the resource.')
        add_resource_parser.add_argument('-v', '--resource-values', help='The value file for resource template.')
        add_resource_parser.set_defaults(func=self.add_resource_command.execute)
        
        #delete resoure
        delete_resource_parser = resource_subparsers.add_parser('delete', help='Delete a resource on an environment.')
        delete_resource_parser.add_argument('-t', '--type', required=True, choices=['individual', 'composite'], help='The type of the resource.')
        delete_resource_parser.add_argument('-l', '--template', required=True, help='The template of the resource.')
        delete_resource_parser.set_defaults(func=self.delete_resource_command.execute)
        
        #environment
        environment_parser = subparsers.add_parser('environment', help='Environment management')
        environment_subparsers = environment_parser.add_subparsers()

        # add environment
        add_environment_parser = environment_subparsers.add_parser('add', help='Add new environment.')
        add_environment_parser.add_argument('-n', '--name', required=True, help='An environment that hold all related resources. Currently map to a resource group.')
        add_environment_parser.add_argument('-l', '--location', required=True, help='Location on the environment.')
        add_environment_parser.add_argument('-p', '--profile', required=True, help='Name of the profile that own the environment.')
        add_environment_parser.set_defaults(func=self.add_environment_command.execute)

        #delete environment
        delete_environment_parser = environment_subparsers.add_parser('delete', help='Delete an environment.')
        delete_environment_parser.add_argument('-n', '--name', required=True, help='An environment that hold all related resources. Currently map to a resource group.')
        delete_environment_parser.add_argument('-p', '--profile', required=True, help='Name of the profile that own the environment.')
        delete_environment_parser.set_defaults(func=self.delete_environment_command.execute)

        args = parser.parse_args()
        return args