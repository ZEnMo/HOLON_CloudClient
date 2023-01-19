
from cloudclient.datamodel.actors import *
from cloudclient.datamodel.contracts import *

class Contract_Energysupplier_default(Contract):
    type=ContractTypeEnum.fixed
    contract_scope=ContractScopeEnum.energysupplier

class Contract_Energysupplier_variable(Contract):
    type=ContractTypeEnum.variable
    contract_scope=ContractScopeEnum.energysupplier

class Contract_Gridoperator_nodal(Contract):
    type=ContractTypeEnum.nodalpricing
    contract_scope=ContractScopeEnum.gridoperator

class Contract_NonfirmATO_night(Contract):
    type=ContractTypeEnum.nonfirmato
    contract_scope=ContractScopeEnum.gridoperator
    nfATO_capacity_kW=5000.0
    nfATO_starttime_h=16.0
    nfATO_endtime_h=7.0

class Contract_Holon_default(Contract):
    type=ContractTypeEnum.fixed
    contract_scope=ContractScopeEnum.energysupplier

class Contract_holon_nodal(Contract):
    type=ContractTypeEnum.nodalpricing
    contract_scope=ContractScopeEnum.gridoperator



