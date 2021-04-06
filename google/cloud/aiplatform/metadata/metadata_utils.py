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
from typing import Optional

from google.cloud.aiplatform import utils, initializer


def full_resource_name(
    resource_id: str,
    resource_noun: str,
    metadata_store_id: Optional[str] = None,
    project: Optional[str] = None,
    location: Optional[str] = None,
) -> str:
    """
    Returns fully qualified resource name.

    Args:
        resource_id (str):
            Required. AI Platform (Unified) resource ID.
        resource_noun (str):
            A plural resource noun to validate the resource name against.
            For example, you would pass "datasets" to validate
            "projects/123/locations/us-central1/datasets/456".
        metadata_store_id (str):
            Optional metadata store to retrieve resource_noun from.
        project (str):
            Optional project to retrieve resource_noun from. If not set, project
            set in aiplatform.init will be used.
        location (str):
            Optional location to retrieve resource_noun from. If not set, location
            set in aiplatform.init will be used.

    Returns:
        resource_name (str):
            A fully-qualified AI Platform (Unified) resource name.

    Raises:
        ValueError:
            If resource name, resource ID or project ID not provided.
    """
    utils.validate_resource_noun(resource_noun)

    user_project = project or initializer.global_config.project
    user_location = location or initializer.global_config.location

    # Partial resource name (i.e. "12345") with known project and location
    if (
        utils.validate_project(user_project)
        and utils.validate_region(user_location)
        and utils.validate_id(resource_id)
    ):
        if metadata_store_id:
            resource_name = f"projects/{user_project}/locations/{user_location}/metadataStores/{metadata_store_id}/{resource_noun}/{resource_id}"
        else:
            resource_name = f"projects/{user_project}/locations/{user_location}/{resource_noun}/{resource_id}"
    # Invalid resource_name parameter
    else:
        raise ValueError(f"Please provide a valid {resource_noun[:-1]} ID")

    return resource_name
