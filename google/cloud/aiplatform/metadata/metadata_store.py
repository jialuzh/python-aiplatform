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
import logging
from typing import Optional, Sequence, Tuple
from urllib.error import HTTPError

import proto
from google.auth import credentials as auth_credentials

from google.cloud.aiplatform import base, initializer
from google.cloud.aiplatform.metadata.metadata_utils import full_resource_name
from google.cloud.aiplatform_v1beta1.services.metadata_service.transports import grpc
from google.cloud.aiplatform_v1beta1.types import metadata_store as gca_metadata_store
from google.cloud.aiplatform_v1beta1.services.metadata_service import (
    client as metadata_service_client,
)


class MetadataStore(base.AiPlatformResourceNounWithFutureManager):
    """Managed metadataStore resource for AI Platform"""

    client_class = metadata_service_client.MetadataServiceClient
    _is_client_prediction_client = False
    _resource_noun = "metadataStores"
    _getter_method = "get_metadata_store"
    _delete_method = "delete_metadata_store"

    def __init__(
        self,
        metadata_store_resource_name: Optional[str] = None,
        metadata_store_id: Optional[str] = "default",
        project: Optional[str] = None,
        location: Optional[str] = None,
        credentials: Optional[auth_credentials.Credentials] = None,
    ):
        """Retrieves an existing MetadataStore given a MetadataStore name or ID.

        Args:
            metadata_store_resource_name (str):
                Optional. A fully-qualified MetadataStore resource name.
                Example: "projects/123/locations/us-central1/MetadataStore/default".
                If set, metadata_store_resource_name overrides metadata_store_id.
            metadata_store_id (str):
                Optional. A resource ID to generate full resource name together with
                project and location when they are initialized or passed.
                If not set, ID will be set to "default".
            project (str):
                Optional project to retrieve resource from. If not set, project
                set in aiplatform.init will be used.
            location (str):
                Optional location to retrieve resource from. If not set, location
                set in aiplatform.init will be used.
            credentials (auth_credentials.Credentials):
                Custom credentials to use to upload this model. Overrides
                credentials set in aiplatform.init.

        """

        super().__init__(
            project=project, location=location, credentials=credentials,
        )
        if metadata_store_resource_name:
            self._gca_resource = self._get_gca_resource(
                resource_name=metadata_store_resource_name
            )
        else:
            self._gca_resource = self._get_gca_resource(
                resource_name=full_resource_name(
                    resource_id=metadata_store_id, resource_noun=self._resource_noun
                )
            )

    def _get_gca_resource(
        self, resource_name: str, allow_str_id: Optional[bool] = False,
    ) -> proto.Message:
        """Returns GAPIC service representation of client class resource."""
        """
        Args:
            resource_name (str):
            Required. A fully-qualified resource name or ID.
            allow_str_id (bool):
            Optional. Whether resource ID can contain non-integer characters.
        """
        return getattr(self.api_client, self._getter_method)(name=resource_name)

    @classmethod
    def create(
        cls,
        metadata_store_id: str = "default",
        project: Optional[str] = None,
        location: Optional[str] = None,
        credentials: Optional[auth_credentials.Credentials] = None,
        request_metadata: Optional[Sequence[Tuple[str, str]]] = (),
        encryption_spec_key_name: Optional[str] = None,
        sync: bool = True,
    ) -> "MetadataStore":
        """Creates a new metadata_store.

        Args:
            metadata_store_id (str):
                The {metadatastore} portion of the resource name with
                the format:
                projects/{project}/locations/{location}/metadataStores/{metadatastore}
                If not provided, the MetadataStore's ID will be set to "default" to create a default MetadataStore.
            project (str):
                Project to upload this model to. Overrides project set in
                aiplatform.init.
            location (str):
                Location to upload this model to. Overrides location set in
                aiplatform.init.
            credentials (auth_credentials.Credentials):
                Custom credentials to use to upload this model. Overrides
                credentials set in aiplatform.init.
            request_metadata (Sequence[Tuple[str, str]]):
                Strings which should be sent along with the request as metadata.
            encryption_spec_key_name (Optional[str]):
                Optional. The Cloud KMS resource identifier of the customer
                managed encryption key used to protect the dataset. Has the
                form:
                ``projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key``.
                The key needs to be in the same region as where the compute
                resource is created.

                If set, this Dataset and all sub-resources of this Dataset will be secured by this key.

                Overrides encryption_spec_key_name set in aiplatform.init.
            sync (bool):
                Whether to execute this method synchronously. If False, this method
                will be executed in concurrent Future and any downstream object will
                be immediately returned and synced when the Future has completed.

        Returns:
            dataset (Dataset):
                Instantiated representation of the managed dataset resource.

        """
        api_client = cls._instantiate_client(location=location, credentials=credentials)
        gapic_metadata_store = gca_metadata_store.MetadataStore(
            encryption_spec=initializer.global_config.get_encryption_spec(
                encryption_spec_key_name=encryption_spec_key_name
            )
        )

        try:
            created_metadata_store = api_client.create_metadata_store(
                parent=initializer.global_config.common_location_path(
                    project=project, location=location
                ),
                metadata_store=gapic_metadata_store,
                metadata_store_id=metadata_store_id,
                metadata=request_metadata,
            ).result()
        except Exception as e:
            logging.error(f"Create MetadataStore caused error: {str(e)}")
            raise

        return cls(
            metadata_store_resource_name=created_metadata_store.name,
            project=project,
            location=location,
            credentials=credentials,
        )
