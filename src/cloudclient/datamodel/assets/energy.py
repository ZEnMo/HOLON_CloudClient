from pydantic import BaseModel, Extra

from enum import Enum


class EnergyAsset(BaseModel, extra=Extra.forbid):
    pass


# class DefaultEnergyAsset(EnergyAsset):
#     name: str


class AmbientTempTypeEnum(str, Enum):
    air = "AIR"
    ground = "GROUND"
    water = "WATER"
