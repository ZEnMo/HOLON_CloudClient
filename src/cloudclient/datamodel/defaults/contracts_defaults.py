from cloudclient.datamodel.actors import *
from cloudclient.datamodel.contracts import *


class Contract_Energysupplier_default(Contract):
    contractType = ContractTypeEnum.delivery
    deliveryContractType = DeliveryContractTypeEnum.fixed
    contractScope = ""
    energyCarrier = EnergyCarrierEnum.electricity
    deliveryPrice_eurpkWh = 0.15
    feedinPrice_eurpkWh = 0.15


class Contract_Energysupplier_variable(Contract):
    contractType = ContractTypeEnum.delivery
    deliveryContractType = DeliveryContractTypeEnum.variable
    contractScope = ""
    # contractScope = "sup1"
    energyCarrier = EnergyCarrierEnum.electricity
    deliveryPrice_eurpkWh = 0.0
    feedinPrice_eurpkWh = 0.0


class Contract_Connection_default(Contract):
    contractType = ContractTypeEnum.connection
    contractScope = ""
    # contractScope: str
    energyCarrier = EnergyCarrierEnum.electricity
    annualFee_eur = 100.0
    connectionContractType = ConnectionContractTypeEnum.default


class Contract_Transport_default(Contract):
    contractType = ContractTypeEnum.transport
    contractScope = ""
    # contractScope: str
    energyCarrier = EnergyCarrierEnum.electricity
    annualFee_eur = 100.0
    transportContractType = TransportContractTypeEnum.default


class Contract_Tax_default(Contract):
    contractType = ContractTypeEnum.tax
    contractScope = ""
    energyCarrier = EnergyCarrierEnum.electricity
    taxContractType = TaxContractTypeEnum.salderen
    taxDelivery_eurpkWh = 0.12
    taxFeedin_eurpkWh = 0.12
    proportionalTax_pct = 0.21
