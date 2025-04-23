from input import *

serverWorkdir = input("Enter base directory of GTNH server installation: ")
clientWorkdir = input("Enter base directory of GTNH client installation: ")

shouldPatchConfigs = get_boolean_input("Should the script patch configs (y/n): ")
shouldInstallMods = get_boolean_input("Should the script install utility mods (y/n): ")
shouldInstallShaders = get_boolean_input("Should the script install shaders (y/n): ")
shouldInstallResourcePacks = get_boolean_input("Should the script install resource packs (y/n): ")


