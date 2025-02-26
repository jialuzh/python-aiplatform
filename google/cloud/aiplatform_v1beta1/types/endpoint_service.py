# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.cloud.aiplatform_v1beta1.types import endpoint as gca_endpoint
from google.cloud.aiplatform_v1beta1.types import operation
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1",
    manifest={
        "CreateEndpointRequest",
        "CreateEndpointOperationMetadata",
        "GetEndpointRequest",
        "ListEndpointsRequest",
        "ListEndpointsResponse",
        "UpdateEndpointRequest",
        "DeleteEndpointRequest",
        "DeployModelRequest",
        "DeployModelResponse",
        "DeployModelOperationMetadata",
        "UndeployModelRequest",
        "UndeployModelResponse",
        "UndeployModelOperationMetadata",
    },
)


class CreateEndpointRequest(proto.Message):
    r"""Request message for
    ``EndpointService.CreateEndpoint``.

    Attributes:
        parent (str):
            Required. The resource name of the Location to create the
            Endpoint in. Format:
            ``projects/{project}/locations/{location}``
        endpoint (google.cloud.aiplatform_v1beta1.types.Endpoint):
            Required. The Endpoint to create.
    """

    parent = proto.Field(proto.STRING, number=1)

    endpoint = proto.Field(proto.MESSAGE, number=2, message=gca_endpoint.Endpoint,)


class CreateEndpointOperationMetadata(proto.Message):
    r"""Runtime operation information for
    ``EndpointService.CreateEndpoint``.

    Attributes:
        generic_metadata (google.cloud.aiplatform_v1beta1.types.GenericOperationMetadata):
            The operation generic information.
    """

    generic_metadata = proto.Field(
        proto.MESSAGE, number=1, message=operation.GenericOperationMetadata,
    )


class GetEndpointRequest(proto.Message):
    r"""Request message for
    ``EndpointService.GetEndpoint``

    Attributes:
        name (str):
            Required. The name of the Endpoint resource. Format:
            ``projects/{project}/locations/{location}/endpoints/{endpoint}``
    """

    name = proto.Field(proto.STRING, number=1)


class ListEndpointsRequest(proto.Message):
    r"""Request message for
    ``EndpointService.ListEndpoints``.

    Attributes:
        parent (str):
            Required. The resource name of the Location from which to
            list the Endpoints. Format:
            ``projects/{project}/locations/{location}``
        filter (str):
            Optional. An expression for filtering the results of the
            request. For field names both snake_case and camelCase are
            supported.

            -  ``endpoint`` supports = and !=. ``endpoint`` represents
               the Endpoint ID, i.e. the last segment of the Endpoint's
               [resource
               name][google.cloud.aiplatform.v1beta1.Endpoint.name].
            -  ``display_name`` supports = and, !=
            -  ``labels`` supports general map functions that is:

               -  ``labels.key=value`` - key:value equality
               -  \`labels.key:\* or labels:key - key existence
               -  A key including a space must be quoted.
                  ``labels."a key"``.

            Some examples:

            -  ``endpoint=1``
            -  ``displayName="myDisplayName"``
            -  ``labels.myKey="myValue"``
        page_size (int):
            Optional. The standard list page size.
        page_token (str):
            Optional. The standard list page token. Typically obtained
            via
            ``ListEndpointsResponse.next_page_token``
            of the previous
            ``EndpointService.ListEndpoints``
            call.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Mask specifying which fields to
            read.
    """

    parent = proto.Field(proto.STRING, number=1)

    filter = proto.Field(proto.STRING, number=2)

    page_size = proto.Field(proto.INT32, number=3)

    page_token = proto.Field(proto.STRING, number=4)

    read_mask = proto.Field(proto.MESSAGE, number=5, message=field_mask.FieldMask,)


class ListEndpointsResponse(proto.Message):
    r"""Response message for
    ``EndpointService.ListEndpoints``.

    Attributes:
        endpoints (Sequence[google.cloud.aiplatform_v1beta1.types.Endpoint]):
            List of Endpoints in the requested page.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            ``ListEndpointsRequest.page_token``
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    endpoints = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gca_endpoint.Endpoint,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class UpdateEndpointRequest(proto.Message):
    r"""Request message for
    ``EndpointService.UpdateEndpoint``.

    Attributes:
        endpoint (google.cloud.aiplatform_v1beta1.types.Endpoint):
            Required. The Endpoint which replaces the
            resource on the server.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. See
            `FieldMask <https://tinyurl.com/protobufs/google.protobuf#fieldmask>`__.
    """

    endpoint = proto.Field(proto.MESSAGE, number=1, message=gca_endpoint.Endpoint,)

    update_mask = proto.Field(proto.MESSAGE, number=2, message=field_mask.FieldMask,)


class DeleteEndpointRequest(proto.Message):
    r"""Request message for
    ``EndpointService.DeleteEndpoint``.

    Attributes:
        name (str):
            Required. The name of the Endpoint resource to be deleted.
            Format:
            ``projects/{project}/locations/{location}/endpoints/{endpoint}``
    """

    name = proto.Field(proto.STRING, number=1)


class DeployModelRequest(proto.Message):
    r"""Request message for
    ``EndpointService.DeployModel``.

    Attributes:
        endpoint (str):
            Required. The name of the Endpoint resource into which to
            deploy a Model. Format:
            ``projects/{project}/locations/{location}/endpoints/{endpoint}``
        deployed_model (google.cloud.aiplatform_v1beta1.types.DeployedModel):
            Required. The DeployedModel to be created within the
            Endpoint. Note that
            ``Endpoint.traffic_split``
            must be updated for the DeployedModel to start receiving
            traffic, either as part of this call, or via
            ``EndpointService.UpdateEndpoint``.
        traffic_split (Sequence[google.cloud.aiplatform_v1beta1.types.DeployModelRequest.TrafficSplitEntry]):
            A map from a DeployedModel's ID to the percentage of this
            Endpoint's traffic that should be forwarded to that
            DeployedModel.

            If this field is non-empty, then the Endpoint's
            ``traffic_split``
            will be overwritten with it. To refer to the ID of the just
            being deployed Model, a "0" should be used, and the actual
            ID of the new DeployedModel will be filled in its place by
            this method. The traffic percentage values must add up to
            100.

            If this field is empty, then the Endpoint's
            ``traffic_split``
            is not updated.
    """

    endpoint = proto.Field(proto.STRING, number=1)

    deployed_model = proto.Field(
        proto.MESSAGE, number=2, message=gca_endpoint.DeployedModel,
    )

    traffic_split = proto.MapField(proto.STRING, proto.INT32, number=3)


class DeployModelResponse(proto.Message):
    r"""Response message for
    ``EndpointService.DeployModel``.

    Attributes:
        deployed_model (google.cloud.aiplatform_v1beta1.types.DeployedModel):
            The DeployedModel that had been deployed in
            the Endpoint.
    """

    deployed_model = proto.Field(
        proto.MESSAGE, number=1, message=gca_endpoint.DeployedModel,
    )


class DeployModelOperationMetadata(proto.Message):
    r"""Runtime operation information for
    ``EndpointService.DeployModel``.

    Attributes:
        generic_metadata (google.cloud.aiplatform_v1beta1.types.GenericOperationMetadata):
            The operation generic information.
    """

    generic_metadata = proto.Field(
        proto.MESSAGE, number=1, message=operation.GenericOperationMetadata,
    )


class UndeployModelRequest(proto.Message):
    r"""Request message for
    ``EndpointService.UndeployModel``.

    Attributes:
        endpoint (str):
            Required. The name of the Endpoint resource from which to
            undeploy a Model. Format:
            ``projects/{project}/locations/{location}/endpoints/{endpoint}``
        deployed_model_id (str):
            Required. The ID of the DeployedModel to be
            undeployed from the Endpoint.
        traffic_split (Sequence[google.cloud.aiplatform_v1beta1.types.UndeployModelRequest.TrafficSplitEntry]):
            If this field is provided, then the Endpoint's
            ``traffic_split``
            will be overwritten with it. If last DeployedModel is being
            undeployed from the Endpoint, the [Endpoint.traffic_split]
            will always end up empty when this call returns. A
            DeployedModel will be successfully undeployed only if it
            doesn't have any traffic assigned to it when this method
            executes, or if this field unassigns any traffic to it.
    """

    endpoint = proto.Field(proto.STRING, number=1)

    deployed_model_id = proto.Field(proto.STRING, number=2)

    traffic_split = proto.MapField(proto.STRING, proto.INT32, number=3)


class UndeployModelResponse(proto.Message):
    r"""Response message for
    ``EndpointService.UndeployModel``.
    """


class UndeployModelOperationMetadata(proto.Message):
    r"""Runtime operation information for
    ``EndpointService.UndeployModel``.

    Attributes:
        generic_metadata (google.cloud.aiplatform_v1beta1.types.GenericOperationMetadata):
            The operation generic information.
    """

    generic_metadata = proto.Field(
        proto.MESSAGE, number=1, message=operation.GenericOperationMetadata,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
