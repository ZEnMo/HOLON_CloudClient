from cloudclient.datamodel.actors import *
from cloudclient.datamodel.contracts import *


class Contract_Energysupplier_default(Contract):
    contractType = ContractTypeEnum.delivery
    deliveryContractType = DeliveryContractTypeEnum.fixed
    contractScope = "sup1"
    energyCarrier = EnergyCarrierEnum.electricity
    deliveryPrice_eurpkWh = 0.15
    feedinPrice_eurpkWh = 0.15


class Contract_Energysupplier_variable(Contract):
    contractType = ContractTypeEnum.delivery
    deliveryContractType = DeliveryContractTypeEnum.variable
    contractScope = "sup1"
    energyCarrier = EnergyCarrierEnum.electricity
    deliveryPrice_eurpkWh = 0.0
    feedinPrice_eurpkWh = 0.0


# class Contract_Gridoperator_nodal(Contract):
#     type=ContractTypeEnum.nodalpricing
#     contract_scope=ContractScopeEnum.gridoperator

# class Contract_NonfirmATO_night(Contract):
#     type=ContractTypeEnum.nonfirmato
#     contract_scope=ContractScopeEnum.gridoperator
#     nfATO_capacity_kW=5000.0
#     nfATO_starttime_h=16.0
#     nfATO_endtime_h=7.0

# class Contract_Holon_default(Contract):
#     type=ContractTypeEnum.fixed
#     contract_scope=ContractScopeEnum.energysupplier

# class Contract_holon_nodal(Contract):
#     type=ContractTypeEnum.nodalpricing
#     contract_scope=ContractScopeEnum.gridoperator
