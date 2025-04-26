from options import *
from patch import *
from mods import *
from journeymap import *
from config import *

config = get_config()
# options = get_options()

options = Options("./test/server", "./test/client", False, True, False, False, False, False)

# patch configs
if options.should_patch_configs:
    print_color(f'###### starting config patching ######', 'green')
    apply_patches(options, config.patch_path)

# apply journeymap_unlimited fix
if options.should_apply_journeymap_unlimited:
    print_color(f'###### applying journeymap unlimited ######', 'green')
    apply_journeymap_unlimited_fix(config, options)

# apply rwg disabling fix

# migrate mods
if options.should_install_mods:
    print_color(f'###### starting mod migration ######', 'green')
    migrate_mods(options, config.mod_path)

# migrate shaders

# migrate resource packs
