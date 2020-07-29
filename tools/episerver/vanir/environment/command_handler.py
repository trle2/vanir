from episerver.vanir.environment.add import AddEnvironmentCommand
from episerver.vanir.environment.delete import DeleteEnvironmentCommand

class CommandHandler:
    def handle(self, env, command, location):
        delete_command = DeleteEnvironmentCommand(env)
        if command == "add":
            add_command = AddEnvironmentCommand(env, location)
            add_command.execute()
        elif command == "delete":
            add_command = DeleteEnvironmentCommand(env)
            add_command.execute()