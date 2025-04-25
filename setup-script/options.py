from dataclasses import dataclass


@dataclass
class Options:
    server_workdir: str
    client_workdir: str

    should_patch_configs: bool
    should_install_mods: bool
    should_install_shaders: bool
    should_install_resource_packs: bool
    should_apply_journeymap_unlimited: bool

    def get_workdir(self, target):
        match target:
            case "server":
                return self.server_workdir
            case "client":
                return self.client_workdir
            case _:
                return ""

def get_options():
    server_workdir = input("Enter base directory of GTNH server installation: ")
    client_workdir = input("Enter base directory of GTNH client installation: ")

    should_patch_configs = get_boolean_input("Should the script patch configs (y/n): ")
    should_install_mods = get_boolean_input("Should the script install utility mods (y/n): ")
    should_install_shaders = get_boolean_input("Should the script install shaders (y/n): ")
    should_install_resource_packs = get_boolean_input("Should the script install resource packs (y/n): ")
    should_apply_journeymap_unlimited = get_boolean_input("Should the script apply journeymap unlimited (y/n): ")

    options = Options(
        server_workdir,
        client_workdir,
        should_patch_configs,
        should_install_mods,
        should_install_shaders,
        should_install_resource_packs,
        should_apply_journeymap_unlimited
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
