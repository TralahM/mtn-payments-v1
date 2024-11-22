# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrderResponse", "_Links", "_LinksSelf", "Data"]


class _LinksSelf(BaseModel):
    href: Optional[str] = None
    """Hyperlink to access the payment link generation endpoint."""


class _Links(BaseModel):
    self: Optional[_LinksSelf] = None


class Data(BaseModel):
    order_redirect_url: Optional[str] = FieldInfo(alias="orderRedirectUrl", default=None)
    """This will have the encrypted url that will be route to pay portal on click."""

    provider_transaction_id: Optional[str] = FieldInfo(alias="providerTransactionId", default=None)
    """ID of the payment, generated by back-end system.

    This can be blank if the payment has previously been pre-approved.
    """


class OrderResponse(BaseModel):
    api_links: Optional[_Links] = FieldInfo(alias="_links", default=None)

    data: Optional[Data] = None

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
    """Message of the transaction. Either Success or Failure."""

    transaction_id: Optional[str] = FieldInfo(alias="transactionId", default=None)
    """Unique identifier for every request to the backend. Mapped from input request."""