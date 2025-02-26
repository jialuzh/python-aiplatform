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


from google.cloud.aiplatform_v1beta1.types import encryption_spec as gca_encryption_spec
from google.cloud.aiplatform_v1beta1.types import job_state
from google.protobuf import struct_pb2 as struct  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore
from google.rpc import status_pb2 as status  # type: ignore
from google.type import money_pb2 as money  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1",
    manifest={
        "DataLabelingJob",
        "ActiveLearningConfig",
        "SampleConfig",
        "TrainingConfig",
    },
)


class DataLabelingJob(proto.Message):
    r"""DataLabelingJob is used to trigger a human labeling job on
    unlabeled data from the following Dataset:

    Attributes:
        name (str):
            Output only. Resource name of the
            DataLabelingJob.
        display_name (str):
            Required. The user-defined name of the
            DataLabelingJob. The name can be up to 128
            characters long and can be consist of any UTF-8
            characters.
            Display name of a DataLabelingJob.
        datasets (Sequence[str]):
            Required. Dataset resource names. Right now we only support
            labeling from a single Dataset. Format:
            ``projects/{project}/locations/{location}/datasets/{dataset}``
        annotation_labels (Sequence[google.cloud.aiplatform_v1beta1.types.DataLabelingJob.AnnotationLabelsEntry]):
            Labels to assign to annotations generated by
            this DataLabelingJob.
            Label keys and values can be no longer than 64
            characters (Unicode codepoints), can only
            contain lowercase letters, numeric characters,
            underscores and dashes. International characters
            are allowed. See https://goo.gl/xmQnxf for more
            information and examples of labels. System
            reserved label keys are prefixed with
            "aiplatform.googleapis.com/" and are immutable.
        labeler_count (int):
            Required. Number of labelers to work on each
            DataItem.
        instruction_uri (str):
            Required. The Google Cloud Storage location
            of the instruction pdf. This pdf is shared with
            labelers, and provides detailed description on
            how to label DataItems in Datasets.
        inputs_schema_uri (str):
            Required. Points to a YAML file stored on
            Google Cloud Storage describing the config for a
            specific type of DataLabelingJob. The schema
            files that can be used here are found in the
            https://storage.googleapis.com/google-cloud-
            aiplatform bucket in the
            /schema/datalabelingjob/inputs/ folder.
        inputs (google.protobuf.struct_pb2.Value):
            Required. Input config parameters for the
            DataLabelingJob.
        state (google.cloud.aiplatform_v1beta1.types.JobState):
            Output only. The detailed state of the job.
        labeling_progress (int):
            Output only. Current labeling job progress percentage scaled
            in interval [0, 100], indicating the percentage of DataItems
            that has been finished.
        current_spend (google.type.money_pb2.Money):
            Output only. Estimated cost(in US dollars)
            that the DataLabelingJob has incurred to date.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this
            DataLabelingJob was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this
            DataLabelingJob was updated most recently.
        error (google.rpc.status_pb2.Status):
            Output only. DataLabelingJob errors. It is only populated
            when job's state is ``JOB_STATE_FAILED`` or
            ``JOB_STATE_CANCELLED``.
        labels (Sequence[google.cloud.aiplatform_v1beta1.types.DataLabelingJob.LabelsEntry]):
            The labels with user-defined metadata to organize your
            DataLabelingJobs.

            Label keys and values can be no longer than 64 characters
            (Unicode codepoints), can only contain lowercase letters,
            numeric characters, underscores and dashes. International
            characters are allowed.

            See https://goo.gl/xmQnxf for more information and examples
            of labels. System reserved label keys are prefixed with
            "aiplatform.googleapis.com/" and are immutable. Following
            system labels exist for each DataLabelingJob:

            -  "aiplatform.googleapis.com/schema": output only, its
               value is the
               ``inputs_schema``'s
               title.
        specialist_pools (Sequence[str]):
            The SpecialistPools' resource names
            associated with this job.
        encryption_spec (google.cloud.aiplatform_v1beta1.types.EncryptionSpec):
            Customer-managed encryption key spec for a
            DataLabelingJob. If set, this DataLabelingJob
            will be secured by this key.
            Note: Annotations created in the DataLabelingJob
            are associated with the EncryptionSpec of the
            Dataset they are exported to.
        active_learning_config (google.cloud.aiplatform_v1beta1.types.ActiveLearningConfig):
            Parameters that configure the active learning
            pipeline. Active learning will label the data
            incrementally via several iterations. For every
            iteration, it will select a batch of data based
            on the sampling strategy.
    """

    name = proto.Field(proto.STRING, number=1)

    display_name = proto.Field(proto.STRING, number=2)

    datasets = proto.RepeatedField(proto.STRING, number=3)

    annotation_labels = proto.MapField(proto.STRING, proto.STRING, number=12)

    labeler_count = proto.Field(proto.INT32, number=4)

    instruction_uri = proto.Field(proto.STRING, number=5)

    inputs_schema_uri = proto.Field(proto.STRING, number=6)

    inputs = proto.Field(proto.MESSAGE, number=7, message=struct.Value,)

    state = proto.Field(proto.ENUM, number=8, enum=job_state.JobState,)

    labeling_progress = proto.Field(proto.INT32, number=13)

    current_spend = proto.Field(proto.MESSAGE, number=14, message=money.Money,)

    create_time = proto.Field(proto.MESSAGE, number=9, message=timestamp.Timestamp,)

    update_time = proto.Field(proto.MESSAGE, number=10, message=timestamp.Timestamp,)

    error = proto.Field(proto.MESSAGE, number=22, message=status.Status,)

    labels = proto.MapField(proto.STRING, proto.STRING, number=11)

    specialist_pools = proto.RepeatedField(proto.STRING, number=16)

    encryption_spec = proto.Field(
        proto.MESSAGE, number=20, message=gca_encryption_spec.EncryptionSpec,
    )

    active_learning_config = proto.Field(
        proto.MESSAGE, number=21, message="ActiveLearningConfig",
    )


class ActiveLearningConfig(proto.Message):
    r"""Parameters that configure the active learning pipeline.
    Active learning will  label the data incrementally by several
    iterations. For every iteration, it  will select a batch of data
    based on the sampling strategy.

    Attributes:
        max_data_item_count (int):
            Max number of human labeled DataItems.
        max_data_item_percentage (int):
            Max percent of total DataItems for human
            labeling.
        sample_config (google.cloud.aiplatform_v1beta1.types.SampleConfig):
            Active learning data sampling config. For
            every active learning labeling iteration, it
            will select a batch of data based on the
            sampling strategy.
        training_config (google.cloud.aiplatform_v1beta1.types.TrainingConfig):
            CMLE training config. For every active
            learning labeling iteration, system will train a
            machine learning model on CMLE. The trained
            model will be used by data sampling algorithm to
            select DataItems.
    """

    max_data_item_count = proto.Field(
        proto.INT64, number=1, oneof="human_labeling_budget"
    )

    max_data_item_percentage = proto.Field(
        proto.INT32, number=2, oneof="human_labeling_budget"
    )

    sample_config = proto.Field(proto.MESSAGE, number=3, message="SampleConfig",)

    training_config = proto.Field(proto.MESSAGE, number=4, message="TrainingConfig",)


class SampleConfig(proto.Message):
    r"""Active learning data sampling config. For every active
    learning labeling iteration, it will select a batch of data
    based on the sampling strategy.

    Attributes:
        initial_batch_sample_percentage (int):
            The percentage of data needed to be labeled
            in the first batch.
        following_batch_sample_percentage (int):
            The percentage of data needed to be labeled
            in each following batch (except the first
            batch).
        sample_strategy (google.cloud.aiplatform_v1beta1.types.SampleConfig.SampleStrategy):
            Field to choose sampling strategy. Sampling
            strategy will decide which data should be
            selected for human labeling in every batch.
    """

    class SampleStrategy(proto.Enum):
        r"""Sample strategy decides which subset of DataItems should be
        selected for human labeling in every batch.
        """
        SAMPLE_STRATEGY_UNSPECIFIED = 0
        UNCERTAINTY = 1

    initial_batch_sample_percentage = proto.Field(
        proto.INT32, number=1, oneof="initial_batch_sample_size"
    )

    following_batch_sample_percentage = proto.Field(
        proto.INT32, number=3, oneof="following_batch_sample_size"
    )

    sample_strategy = proto.Field(proto.ENUM, number=5, enum=SampleStrategy,)


class TrainingConfig(proto.Message):
    r"""CMLE training config. For every active learning labeling
    iteration, system will train a machine learning model on CMLE.
    The trained model will be used by data sampling algorithm to
    select DataItems.

    Attributes:
        timeout_training_milli_hours (int):
            The timeout hours for the CMLE training job,
            expressed in milli hours i.e. 1,000 value in
            this field means 1 hour.
    """

    timeout_training_milli_hours = proto.Field(proto.INT64, number=1)


__all__ = tuple(sorted(__protobuf__.manifest))
