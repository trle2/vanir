# Vanir

A tool that help developers manage Azure resources more effectively.

## Executable
You can find the latest build of the tool in [tools/executable](tools/executable) folder. I built it using [PyInstaller](https://www.pyinstaller.org/). Only linux executable for now.

## Prerequisites
- Environment variables: AZURE_SUBSCRIPTION_ID, AZURE_TENANT_ID, AZURE_CLIENT_ID, AZURE_CLIENT_SECRET

## Features
### Profile management

**This feature is not supported yet. I planned to implement in the next hack day.**
Idealy, each developer will have their own profile, which hold all of their own environments.

### Environment management

Environment can be used to hold all resources needed by an application or an environment of an application that can be created/destroyed with ease.

### Resource management

Individual Azure resources can be managed here.