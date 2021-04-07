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

from google.cloud.aiplatform import metadata


class MetadataConfig:
    """Stores states for Metadata Service."""

    def __init__(
        self, experiment: Optional[str] = None, run: Optional[str] = None,
    ):
        self._experiment = experiment
        self._run = run
        self._experiment_context = (None,)
        self._run_execution = (None,)
        self._metrics_artifact = (None,)

    def init(self):
        print(f"setup metadata config: {self._experiment} and {self._run}.")

        metadata.MetadataStore.create()

        # TODO: update schema_title to system type.
        self._experiment_context = metadata.Context.create(
            context_id=self._experiment, schema_title="test.Experiment"
        )
