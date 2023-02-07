# from cloudclient.datamodel.defaults import *

from cloudclient.datamodel.actors import *
from cloudclient.datamodel.contracts import *
from cloudclient.datamodel.defaults.contracts_defaults import *

class Energysupplier_default(Actor):
    amount: Optional[int]
    category = ActorTypeEnum.energysupplier
    id = ""
    parent_actor = "nat"
    contracts = []

class Gridoperator_default(Actor):
    amount: Optional[int]
    category = ActorTypeEnum.gridoperator
    id = ""
    parent_actor = "nat"
    contracts = []

class Energyholon_default(Actor):
    amount: Optional[int]
    category = ActorTypeEnum.energyholon
    id = ""
    parent_actor = ""
    contracts = [Contract_Holon_default()]


class Household_default(Actor):
    amount: Optional[int]
    category = ActorTypeEnum.connectionowner
    id = ""
    parent_actor = ""
    contracts = [Contract_Energysupplier_default()]

class Commercial_default(Actor):
    amount: Optional[int]
    type = SubTypeEnum.commercial
    category = ActorTypeEnum.connectionowner
    id = ""
    parent_actor = ""
    contracts = [Contract_Energysupplier_default()]

#     Actor(
#         category="ENERGYSUPPLIER",
#         id="sup1",
#         parent_actor="nat",
#     ),
#     Actor(
#         category="ENERGYHOLON",
#         id="hol1",
#         parent_actor="sup1",
#         contracts=[
#             Contract(type="NODALPRICING", contract_scope="GRIDOPERATOR"),
#             Contract(type="VARIABLE", contract_scope="ENERGYSUPPLIER"),
#             Contract(
#                 type="NONFIRMATO",
#                 contract_scope="GRIDOPERATOR",
#                 nfATO_capacity_kW=5000.0,
#                 nfATO_starttime_h=16.0,
#                 nfATO_endtime_h=7.0,
#             ),
#         ],
#     ),
#     Actor(
#         category="GRIDOPERATOR",
#         id="o1",
#         parent_actor="nat",
#     ),