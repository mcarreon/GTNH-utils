from dataclasses import dataclass
import json
from pathlib import Path

config_path = './configs/config.json'

@dataclass
class Config:
    patch_path: str
    mod_path: str
    journeymap_unlimited_path: str

    journeymap_server_file: str
    journeymap_client_file: str

    def get_server_journeymap_path(self, server_workdir):
        return Path(server_workdir).joinpath('mods').joinpath(self.journeymap_server_file)

    def get_client_journeymap_path(self, client_workdir):
        return Path(client_workdir).joinpath('mods').joinpath(self.journeymap_client_file)

def get_config():
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return Config(**data)