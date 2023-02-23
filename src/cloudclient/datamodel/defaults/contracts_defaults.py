from cloudclient.datamodel.actors import *
from cloudclient.datamodel.contracts import *


class Contract_Energysupplier_default(DeliveryContract):
    contractType = ContractTypeEnum.delivery
    deliveryContractType = DeliveryContractTypeEnum.fixed
    contractScope = ""
    energyCarrier = EnergyCarrierEnum.electricity
    deliveryPrice_eurpkWh = 0.15
    feedinPrice_eurpkWh = 0.15
    annualFee_eur = 100.0


class Contract_Energysupplier_variable(DeliveryContract):
    contractType = ContractTypeEnum.delivery
    deliveryContractType = DeliveryContractTypeEnum.variable
    contractScope = ""
    # contractScope = "sup1"
    energyCarrier = EnergyCarrierEnum.electricity
    deliveryPrice_eurpkWh = 0.0
    feedinPrice_eurpkWh = 0.0
    annualFee_eur = 100.0


class Contract_Connection_default(ConnectionContract):
    contractType = ContractTypeEnum.connection
    contractScope = ""
    # contractScope: str
    energyCarrier = EnergyCarrierEnum.electricity
    annualFee_eur = 100.0
    connectionContractType = ConnectionContractTypeEnum.default


class Contract_Transport_default(TransportContract):
    contractType = ContractTypeEnum.transport
    contractScope = ""
    # contractScope: str
    energyCarrier = EnergyCarrierEnum.electricity
    annualFee_eur = 100.0
    transportContractType = TransportContractTypeEnum.default


class Contract_Tax_default(TaxContract):
    contractType = ContractTypeEnum.tax
    contractScope = ""
    energyCarrier = EnergyCarrierEnum.electricity
    taxContractType = TaxContractTypeEnum.salderen
    taxDelivery_eurpkWh = 0.12
    taxFeedin_eurpkWh = 0.12
    proportionalTax_pct = 0.21
    annualFee_eur = 100.0
