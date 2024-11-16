# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PaymentResponse",
    "_Links",
    "_LinksSelf",
    "Data",
    "DataAdditionalInformation",
    "DataDiscount",
    "DataLoyaltyInformation",
    "DataLoyaltyInformationConsumedAmount",
    "DataLoyaltyInformationGeneratedAmount",
    "DataLoyaltyInformationNewBalance",
    "DataMetaData",
    "DataNewBalance",
    "DataTransactionFee",
]


class _LinksSelf(BaseModel):
    href: Optional[str] = None
    """Hyperlink to access the financial payment."""


class _Links(BaseModel):
    self: Optional[_LinksSelf] = None


class DataAdditionalInformation(BaseModel):
    description: str
    """Description of additional information item."""

    name: str
    """Name of additional information item."""


class DataDiscount(BaseModel):
    amount: float
    """Amount of money"""

    units: str
    """Currency"""


class DataLoyaltyInformationConsumedAmount(BaseModel):
    amount: float
    """Amount of money"""

    units: str
    """Currency"""


class DataLoyaltyInformationGeneratedAmount(BaseModel):
    amount: float
    """Amount of money"""

    units: str
    """Currency"""


class DataLoyaltyInformationNewBalance(BaseModel):
    amount: float
    """Amount of money"""

    units: str
    """Currency"""


class DataLoyaltyInformation(BaseModel):
    consumed_amount: Optional[DataLoyaltyInformationConsumedAmount] = FieldInfo(alias="consumedAmount", default=None)
    """Representation of monetary value."""

    generated_amount: Optional[DataLoyaltyInformationGeneratedAmount] = FieldInfo(alias="generatedAmount", default=None)
    """Representation of monetary value."""

    new_balance: Optional[DataLoyaltyInformationNewBalance] = FieldInfo(alias="newBalance", default=None)
    """Representation of monetary value."""


class DataMetaData(BaseModel):
    description: str
    """Description of additional information item."""

    name: str
    """Name of additional information item."""


class DataNewBalance(BaseModel):
    amount: float
    """Amount of money"""

    units: str
    """Currency"""


class DataTransactionFee(BaseModel):
    amount: float
    """Amount of money"""

    units: str
    """Currency"""


class Data(BaseModel):
    additional_information: Optional[DataAdditionalInformation] = FieldInfo(alias="additionalInformation", default=None)
    """Additional information relating to the payment transaction."""

    approval_id: Optional[str] = FieldInfo(alias="approvalId", default=None)
    """
    Unique identifier in the client for the payment in case it is needed to
    correlate. Generated by back-end system. This can be blank if the payment has
    previously been pre-approved.
    """

    correlator_id: Optional[str] = FieldInfo(alias="correlatorId", default=None)
    """
    Unique identifier in the client for the payment in case it is needed to
    correlate.
    """

    discount: Optional[DataDiscount] = None
    """Representation of monetary value."""

    external_code: Optional[str] = FieldInfo(alias="externalCode", default=None)
    """This is the external reference code.

    This can be the bank institution code for the NIMBS payments usecases
    """

    loyalty_information: Optional[DataLoyaltyInformation] = FieldInfo(alias="loyaltyInformation", default=None)
    """Contains all the loyalty balances associated with a customer."""

    meta_data: Optional[List[DataMetaData]] = FieldInfo(alias="metaData", default=None)
    """An array of additional information related to the payment"""

    new_balance: Optional[DataNewBalance] = FieldInfo(alias="newBalance", default=None)
    """Representation of monetary value."""

    payer_note: Optional[str] = FieldInfo(alias="payerNote", default=None)
    """A descriptive note for sender transaction history."""

    status: Optional[str] = None
    """Status of the payment method."""

    status_date: Optional[str] = FieldInfo(alias="statusDate", default=None)
    """Time the status of the payment changed."""

    transaction_fee: Optional[DataTransactionFee] = FieldInfo(alias="transactionFee", default=None)
    """Representation of monetary value."""


class PaymentResponse(BaseModel):
    api_links: Optional[_Links] = FieldInfo(alias="_links", default=None)
    """Relevant links to the financial payment."""

    data: Optional[Data] = None

    fulfillment_status: Optional[Literal["Succesful", "Failed"]] = FieldInfo(alias="fulfillmentStatus", default=None)
    """A description of the transaction fulfillment status."""

    provider_transaction_id: Optional[str] = FieldInfo(alias="providerTransactionId", default=None)
    """ID of the payment, generated by back-end system.

    This can be blank if the payment has previously been pre-approved.
    """

    sequence_no: Optional[str] = FieldInfo(alias="sequenceNo", default=None)
    """A unique id for tracing all requests"""

    status_code: Optional[str] = FieldInfo(alias="statusCode", default=None)
    """
    This is the MADAPI Canonical Error Code (it is 4 characters long and it is not
    the HTTP Status Code which is 3 characters long). Back-end system errors are
    mapped to specific canonical error codes which are returned. 0000 is for a
    success. More information on these mappings can be found on the MADAPI
    Confluence Page 'Response Codes'
    """

    status_message: Optional[str] = FieldInfo(alias="statusMessage", default=None)
    """A description of the transaction status."""

    support_message: Optional[str] = FieldInfo(alias="supportMessage", default=None)
    """A description used for error handling"""
