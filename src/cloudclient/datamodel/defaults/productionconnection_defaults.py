from cloudclient.datamodel.defaults import (
    production_defaults
)

from cloudclient.datamodel.gridconnections import *
from cloudclient.datamodel.defaults import *

class ResidualHeatProducer(ProductionGridConnection):
    amount: Optional[int]
    owner_actor = ""
    id = ""
    capacity_kw = 1000.0
    parent_electric = ""
    parent_heat = ""
    category = ProductionCategoryEnum.residualheat
    type = "RESIDUALHEATHT"
    assets = [ ResidualHeat_HT ]
    
  