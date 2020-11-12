# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_create_hyperparameter_tuning_job_sample]
from google.cloud import aiplatform


def run_sample():
    # TODO(dev): replace these variables to run the code
    display_name = "YOUR-DISPLAY-NAME"
    container_image_uri = "YOUR-CONTAINER-IMAGE-URI"
    project = "YOUR-PROJECT"
    create_hyperparameter_tuning_job_sample(display_name, container_image_uri, project)


def create_hyperparameter_tuning_job_sample(
    display_name: str, container_image_uri: str, project: str
):
    client_options = {"api_endpoint": "us-central1-aiplatform.googleapis.com"}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.JobServiceClient(client_options=client_options)
    location = "us-central1"
    parent = "projects/{project}/locations/{location}".format(
        project=project, location=location
    )
    hyperparameter_tuning_job = {
        "display_name": display_name,
        "max_trial_count": 2,
        "parallel_trial_count": 1,
        "max_failed_trial_count": 1,
        "study_spec": {
            "metrics": [
                {
                    "metric_id": "accuracy",
                    "goal": aiplatform.gapic.StudySpec.MetricSpec.GoalType.MAXIMIZE,
                }
            ],
            "parameters": [
                {
                    # Learning rate.
                    "parameter_id": "lr",
                    "double_value_spec": {"min_value": 0.001, "max_value": 0.1},
                },
            ],
        },
        "trial_job_spec": {
            "worker_pool_specs": [
                {
                    "machine_spec": {
                        "machine_type": "n1-standard-4",
                        "accelerator_type": aiplatform.gapic.AcceleratorType.NVIDIA_TESLA_K80,
                        "accelerator_count": 1,
                    },
                    "replica_count": 1,
                    "container_spec": {
                        "image_uri": container_image_uri,
                        "command": [],
                        "args": [],
                    },
                }
            ]
        },
    }
    response = client.create_hyperparameter_tuning_job(
        parent=parent, hyperparameter_tuning_job=hyperparameter_tuning_job
    )
    print("response")
    print(" name:", response.name)
    print(" display_name:", response.display_name)
    print(" max_trial_count:", response.max_trial_count)
    print(" parallel_trial_count:", response.parallel_trial_count)
    print(" max_failed_trial_count:", response.max_failed_trial_count)
    print(" state:", response.state)
    print(" start_time:", response.start_time)
    print(" end_time:", response.end_time)
    print(" labels:", response.labels)
    study_spec = response.study_spec
    trial_job_spec = response.trial_job_spec
    trials = response.trials
    error = response.error


# [END aiplatform_create_hyperparameter_tuning_job_sample]