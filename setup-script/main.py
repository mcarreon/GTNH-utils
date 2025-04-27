from options import *
from patch import *
from mods import *
from journeymap import *
from config import *
from shaders import *
from resource_packs import *
from rwg import *


config = get_config()
# options = get_options()

options = Options("./test/server", "./test/client", False, False, True, False, False, False)

# patch configs
if options.should_patch_configs:
    print_color(f'###### starting config patching ######', 'green')
    apply_patches(options, config.patch_path)

# apply journeymap_unlimited fix
if options.should_apply_journeymap_unlimited:
    print_color(f'###### applying journeymap unlimited ######', 'green')
    apply_journeymap_unlimited_fix(config, options)

# apply rwg disabling fix
if options.should_disable_rwg:
    print_color(f'###### starting rwg disabling ######', 'green')
    disable_rwg(config, options)

# migrate mods
if options.should_install_mods:
    print_color(f'###### starting mod migration ######', 'green')
    migrate_mods(options, config.mod_path)

# migrate shaders
if options.should_install_shaders:
    print_color(f'###### starting shader migration ######', 'green')
    migrate_shaders(config, options)

# migrate resource packs
if options.should_install_resource_packs:
    print_color(f'###### starting resource pack migration ######', 'green')
    migrate_resourcepacks(config, options)