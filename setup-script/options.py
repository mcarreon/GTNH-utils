from dataclasses import dataclass
from pathlib import Path


@dataclass
class Options:
    server_workdir: str
    client_workdir: str

    should_patch_configs: bool
    should_apply_journeymap_unlimited: bool
    should_disable_rwg: bool
    should_install_mods: bool
    should_install_shaders: bool
    should_install_resource_packs: bool


    def get_workdir(self, target):
        match target:
            case "server":
                workdir = self.server_workdir
            case "client":
                workdir = self.client_workdir
            case _:
                return Path()

        return Path(workdir)

    def get_mod_path(self, target):
        match target:
            case "server":
                workdir = self.server_workdir
            case "client":
                workdir = self.client_workdir
            case _:
                return Path()

        return Path(workdir).joinpath('mods')

    def get_shaders_dest(self):
        return Path(self.client_workdir).joinpath('shaders')

    def get_resourcepacks_dest(self):
        return Path(self.client_workdir).joinpath('resourcepacks')

def get_options():
    server_workdir = input("Enter base directory of GTNH server installation: ")
    client_workdir = input("Enter base directory of GTNH client installation: ")

    should_patch_configs = get_boolean_input("Should the script patch configs (y/n): ")
    should_apply_journeymap_unlimited = get_boolean_input("Should the script apply journeymap unlimited (y/n): ")
    should_disable_rwg = get_boolean_input("Should the script disable RWG (y/n): ")
    should_install_mods = get_boolean_input("Should the script install utility mods (y/n): ")
    should_install_shaders = get_boolean_input("Should the script install shaders (y/n): ")
    should_install_resource_packs = get_boolean_input("Should the script install resource packs (y/n): ")


    options = Options(
        server_workdir,
        client_workdir,
        should_patch_configs,
        should_apply_journeymap_unlimited,
        should_disable_rwg,
        should_install_mods,
        should_install_shaders,
        should_install_resource_packs
    )

    return options

def get_boolean_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print('Please enter either y or n')
