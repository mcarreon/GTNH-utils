from options import *
from patch import *
from mods import *

# config_path = './configs/test_config.json'
config_path = './configs/patch_config.json'
mod_path = './mods-to-install'


options = Options("./test/server", "./test/client", False, True, True, True, True)

# options = get_options()

# patch configs
if options.should_patch_configs:
    print_color(f'###### starting config patching ######', 'green')
    apply_patches(options, config_path)

# migrate mods
if options.should_install_mods:
    print_color(f'###### starting mod migration ######', 'green')
    migrate_mods(options, mod_path)
