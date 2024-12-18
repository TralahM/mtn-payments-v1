# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from mtn_payments_v1 import MtnPaymentsV1, AsyncMtnPaymentsV1
from mtn_payments_v1.types.payments import PaymentHistoryResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: MtnPaymentsV1) -> None:
        history = client.payments.history.list(
            id="c5f80cb8-dc8b-11ea-87d0-0242ac130003",
        )
        assert_matches_type(PaymentHistoryResponse, history, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: MtnPaymentsV1) -> None:
        history = client.payments.history.list(
            id="c5f80cb8-dc8b-11ea-87d0-0242ac130003",
            end_date="endDate",
            id_type="MSISDN",
            node_id="nodeId",
            page_number=0,
            page_size=0,
            query_type="queryType",
            registration_channel="registrationChannel",
            request_type="MOMO",
            segment="subscriber",
            start_date="startDate",
            start_time="startTime",
            status="status",
            target_system="CPG",
            trace_id="traceId",
            transaction_id="6f0bece6-7df3-4da4-af02-5e7f16e5e6fc",
            x_authorization="X-Authorization",
        )
        assert_matches_type(PaymentHistoryResponse, history, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: MtnPaymentsV1) -> None:
        response = client.payments.history.with_raw_response.list(
            id="c5f80cb8-dc8b-11ea-87d0-0242ac130003",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(PaymentHistoryResponse, history, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: MtnPaymentsV1) -> None:
        with client.payments.history.with_streaming_response.list(
            id="c5f80cb8-dc8b-11ea-87d0-0242ac130003",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(PaymentHistoryResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: MtnPaymentsV1) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.history.with_raw_response.list(
                id="",
            )


class TestAsyncHistory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncMtnPaymentsV1) -> None:
        history = await async_client.payments.history.list(
            id="c5f80cb8-dc8b-11ea-87d0-0242ac130003",
        )
        assert_matches_type(PaymentHistoryResponse, history, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMtnPaymentsV1) -> None:
        history = await async_client.payments.history.list(
            id="c5f80cb8-dc8b-11ea-87d0-0242ac130003",
            end_date="endDate",
            id_type="MSISDN",
            node_id="nodeId",
            page_number=0,
            page_size=0,
            query_type="queryType",
            registration_channel="registrationChannel",
            request_type="MOMO",
            segment="subscriber",
            start_date="startDate",
            start_time="startTime",
            status="status",
            target_system="CPG",
            trace_id="traceId",
            transaction_id="6f0bece6-7df3-4da4-af02-5e7f16e5e6fc",
            x_authorization="X-Authorization",
        )
        assert_matches_type(PaymentHistoryResponse, history, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMtnPaymentsV1) -> None:
        response = await async_client.payments.history.with_raw_response.list(
            id="c5f80cb8-dc8b-11ea-87d0-0242ac130003",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(PaymentHistoryResponse, history, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMtnPaymentsV1) -> None:
        async with async_client.payments.history.with_streaming_response.list(
            id="c5f80cb8-dc8b-11ea-87d0-0242ac130003",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(PaymentHistoryResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncMtnPaymentsV1) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.history.with_raw_response.list(
                id="",
            )
