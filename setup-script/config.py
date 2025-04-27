from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import List

config_path = './configs/config.json'

@dataclass
class Change:
    base: str
    override: str

@dataclass
class Patch:
    filepath: str
    changes: List[Change] = field(default_factory=list)

@dataclass
class RWG:
    patch: Patch
    rwg_file: str

@dataclass
class Config:
    patch_path: str
    mod_path: str
    shaders_path: str
    resourcepacks_path: str

    journeymap_unlimited_path: str
    journeymap_server_file: str
    journeymap_client_file: str

    rwg: RWG

    def get_server_journeymap_path(self, server_workdir):
        return Path(server_workdir).joinpath('mods').joinpath(self.journeymap_server_file)

    def get_client_journeymap_path(self, client_workdir):
        return Path(client_workdir).joinpath('mods').joinpath(self.journeymap_client_file)

    def get_server_rwg_path(self, client_workdir):
        return Path(client_workdir).joinpath('mods').joinpath(self.rwg.rwg_file)

def get_config():
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)

        # build Change objects
        patch_data = data["rwg"]["patch"]
        changes = [Change(**chg) for chg in patch_data["changes"]]

        # build Patch
        patch = Patch(
            filepath=patch_data["filepath"],
            changes=changes
        )

        # build RWG
        rwg = RWG(
            patch=patch,
            rwg_file=data["rwg"]["rwg_file"]
        )

        # build Config, passing the rwg instance
        return Config(
            patch_path=data["patch_path"],
            mod_path=data["mod_path"],
            shaders_path=data["shaders_path"],
            resourcepacks_path=data["resourcepacks_path"],
            journeymap_unlimited_path=data["journeymap_unlimited_path"],
            journeymap_server_file=data["journeymap_server_file"],
            journeymap_client_file=data["journeymap_client_file"],
            rwg=rwg
        )