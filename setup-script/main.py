import json

from options import *
from utils import *
from patch import *


# config_path = './configs/test_config.json'
config_path = './configs/patch_config.json'

options = Options("./test/server", "./test/client", True, True, True, True)

# options = get_options()

if options.should_patch_configs:
    apply_patches(options, config_path)
