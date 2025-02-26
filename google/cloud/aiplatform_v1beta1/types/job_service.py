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


from google.cloud.aiplatform_v1beta1.types import (
    batch_prediction_job as gca_batch_prediction_job,
)
from google.cloud.aiplatform_v1beta1.types import custom_job as gca_custom_job
from google.cloud.aiplatform_v1beta1.types import (
    data_labeling_job as gca_data_labeling_job,
)
from google.cloud.aiplatform_v1beta1.types import (
    hyperparameter_tuning_job as gca_hyperparameter_tuning_job,
)
from google.protobuf import field_mask_pb2 as field_mask  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1",
    manifest={
        "CreateCustomJobRequest",
        "GetCustomJobRequest",
        "ListCustomJobsRequest",
        "ListCustomJobsResponse",
        "DeleteCustomJobRequest",
        "CancelCustomJobRequest",
        "CreateDataLabelingJobRequest",
        "GetDataLabelingJobRequest",
        "ListDataLabelingJobsRequest",
        "ListDataLabelingJobsResponse",
        "DeleteDataLabelingJobRequest",
        "CancelDataLabelingJobRequest",
        "CreateHyperparameterTuningJobRequest",
        "GetHyperparameterTuningJobRequest",
        "ListHyperparameterTuningJobsRequest",
        "ListHyperparameterTuningJobsResponse",
        "DeleteHyperparameterTuningJobRequest",
        "CancelHyperparameterTuningJobRequest",
        "CreateBatchPredictionJobRequest",
        "GetBatchPredictionJobRequest",
        "ListBatchPredictionJobsRequest",
        "ListBatchPredictionJobsResponse",
        "DeleteBatchPredictionJobRequest",
        "CancelBatchPredictionJobRequest",
    },
)


class CreateCustomJobRequest(proto.Message):
    r"""Request message for
    ``JobService.CreateCustomJob``.

    Attributes:
        parent (str):
            Required. The resource name of the Location to create the
            CustomJob in. Format:
            ``projects/{project}/locations/{location}``
        custom_job (google.cloud.aiplatform_v1beta1.types.CustomJob):
            Required. The CustomJob to create.
    """

    parent = proto.Field(proto.STRING, number=1)

    custom_job = proto.Field(proto.MESSAGE, number=2, message=gca_custom_job.CustomJob,)


class GetCustomJobRequest(proto.Message):
    r"""Request message for
    ``JobService.GetCustomJob``.

    Attributes:
        name (str):
            Required. The name of the CustomJob resource. Format:
            ``projects/{project}/locations/{location}/customJobs/{custom_job}``
    """

    name = proto.Field(proto.STRING, number=1)


class ListCustomJobsRequest(proto.Message):
    r"""Request message for
    ``JobService.ListCustomJobs``.

    Attributes:
        parent (str):
            Required. The resource name of the Location to list the
            CustomJobs from. Format:
            ``projects/{project}/locations/{location}``
        filter (str):
            The standard list filter.

            Supported fields:

            -  ``display_name`` supports = and !=.

            -  ``state`` supports = and !=.

            Some examples of using the filter are:

            -  ``state="JOB_STATE_SUCCEEDED" AND display_name="my_job"``

            -  ``state="JOB_STATE_RUNNING" OR display_name="my_job"``

            -  ``NOT display_name="my_job"``

            -  ``state="JOB_STATE_FAILED"``
        page_size (int):
            The standard list page size.
        page_token (str):
            The standard list page token. Typically obtained via
            ``ListCustomJobsResponse.next_page_token``
            of the previous
            ``JobService.ListCustomJobs``
            call.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask specifying which fields to read.
    """

    parent = proto.Field(proto.STRING, number=1)

    filter = proto.Field(proto.STRING, number=2)

    page_size = proto.Field(proto.INT32, number=3)

    page_token = proto.Field(proto.STRING, number=4)

    read_mask = proto.Field(proto.MESSAGE, number=5, message=field_mask.FieldMask,)


class ListCustomJobsResponse(proto.Message):
    r"""Response message for
    ``JobService.ListCustomJobs``

    Attributes:
        custom_jobs (Sequence[google.cloud.aiplatform_v1beta1.types.CustomJob]):
            List of CustomJobs in the requested page.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            ``ListCustomJobsRequest.page_token``
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    custom_jobs = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gca_custom_job.CustomJob,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class DeleteCustomJobRequest(proto.Message):
    r"""Request message for
    ``JobService.DeleteCustomJob``.

    Attributes:
        name (str):
            Required. The name of the CustomJob resource to be deleted.
            Format:
            ``projects/{project}/locations/{location}/customJobs/{custom_job}``
    """

    name = proto.Field(proto.STRING, number=1)


class CancelCustomJobRequest(proto.Message):
    r"""Request message for
    ``JobService.CancelCustomJob``.

    Attributes:
        name (str):
            Required. The name of the CustomJob to cancel. Format:
            ``projects/{project}/locations/{location}/customJobs/{custom_job}``
    """

    name = proto.Field(proto.STRING, number=1)


class CreateDataLabelingJobRequest(proto.Message):
    r"""Request message for
    [DataLabelingJobService.CreateDataLabelingJob][].

    Attributes:
        parent (str):
            Required. The parent of the DataLabelingJob. Format:
            ``projects/{project}/locations/{location}``
        data_labeling_job (google.cloud.aiplatform_v1beta1.types.DataLabelingJob):
            Required. The DataLabelingJob to create.
    """

    parent = proto.Field(proto.STRING, number=1)

    data_labeling_job = proto.Field(
        proto.MESSAGE, number=2, message=gca_data_labeling_job.DataLabelingJob,
    )


class GetDataLabelingJobRequest(proto.Message):
    r"""Request message for [DataLabelingJobService.GetDataLabelingJob][].

    Attributes:
        name (str):
            Required. The name of the DataLabelingJob. Format:
            ``projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}``
    """

    name = proto.Field(proto.STRING, number=1)


class ListDataLabelingJobsRequest(proto.Message):
    r"""Request message for [DataLabelingJobService.ListDataLabelingJobs][].

    Attributes:
        parent (str):
            Required. The parent of the DataLabelingJob. Format:
            ``projects/{project}/locations/{location}``
        filter (str):
            The standard list filter.

            Supported fields:

            -  ``display_name`` supports = and !=.

            -  ``state`` supports = and !=.

            Some examples of using the filter are:

            -  ``state="JOB_STATE_SUCCEEDED" AND display_name="my_job"``

            -  ``state="JOB_STATE_RUNNING" OR display_name="my_job"``

            -  ``NOT display_name="my_job"``

            -  ``state="JOB_STATE_FAILED"``
        page_size (int):
            The standard list page size.
        page_token (str):
            The standard list page token.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask specifying which fields to read. FieldMask represents a
            set of symbolic field paths. For example, the mask can be
            ``paths: "name"``. The "name" here is a field in
            DataLabelingJob. If this field is not set, all fields of the
            DataLabelingJob are returned.
        order_by (str):
            A comma-separated list of fields to order by, sorted in
            ascending order by default. Use ``desc`` after a field name
            for descending.
    """

    parent = proto.Field(proto.STRING, number=1)

    filter = proto.Field(proto.STRING, number=2)

    page_size = proto.Field(proto.INT32, number=3)

    page_token = proto.Field(proto.STRING, number=4)

    read_mask = proto.Field(proto.MESSAGE, number=5, message=field_mask.FieldMask,)

    order_by = proto.Field(proto.STRING, number=6)


class ListDataLabelingJobsResponse(proto.Message):
    r"""Response message for
    ``JobService.ListDataLabelingJobs``.

    Attributes:
        data_labeling_jobs (Sequence[google.cloud.aiplatform_v1beta1.types.DataLabelingJob]):
            A list of DataLabelingJobs that matches the
            specified filter in the request.
        next_page_token (str):
            The standard List next-page token.
    """

    @property
    def raw_page(self):
        return self

    data_labeling_jobs = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gca_data_labeling_job.DataLabelingJob,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class DeleteDataLabelingJobRequest(proto.Message):
    r"""Request message for
    ``JobService.DeleteDataLabelingJob``.

    Attributes:
        name (str):
            Required. The name of the DataLabelingJob to be deleted.
            Format:
            ``projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}``
    """

    name = proto.Field(proto.STRING, number=1)


class CancelDataLabelingJobRequest(proto.Message):
    r"""Request message for
    [DataLabelingJobService.CancelDataLabelingJob][].

    Attributes:
        name (str):
            Required. The name of the DataLabelingJob. Format:
            ``projects/{project}/locations/{location}/dataLabelingJobs/{data_labeling_job}``
    """

    name = proto.Field(proto.STRING, number=1)


class CreateHyperparameterTuningJobRequest(proto.Message):
    r"""Request message for
    ``JobService.CreateHyperparameterTuningJob``.

    Attributes:
        parent (str):
            Required. The resource name of the Location to create the
            HyperparameterTuningJob in. Format:
            ``projects/{project}/locations/{location}``
        hyperparameter_tuning_job (google.cloud.aiplatform_v1beta1.types.HyperparameterTuningJob):
            Required. The HyperparameterTuningJob to
            create.
    """

    parent = proto.Field(proto.STRING, number=1)

    hyperparameter_tuning_job = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gca_hyperparameter_tuning_job.HyperparameterTuningJob,
    )


class GetHyperparameterTuningJobRequest(proto.Message):
    r"""Request message for
    ``JobService.GetHyperparameterTuningJob``.

    Attributes:
        name (str):
            Required. The name of the HyperparameterTuningJob resource.
            Format:
            ``projects/{project}/locations/{location}/hyperparameterTuningJobs/{hyperparameter_tuning_job}``
    """

    name = proto.Field(proto.STRING, number=1)


class ListHyperparameterTuningJobsRequest(proto.Message):
    r"""Request message for
    ``JobService.ListHyperparameterTuningJobs``.

    Attributes:
        parent (str):
            Required. The resource name of the Location to list the
            HyperparameterTuningJobs from. Format:
            ``projects/{project}/locations/{location}``
        filter (str):
            The standard list filter.

            Supported fields:

            -  ``display_name`` supports = and !=.

            -  ``state`` supports = and !=.

            Some examples of using the filter are:

            -  ``state="JOB_STATE_SUCCEEDED" AND display_name="my_job"``

            -  ``state="JOB_STATE_RUNNING" OR display_name="my_job"``

            -  ``NOT display_name="my_job"``

            -  ``state="JOB_STATE_FAILED"``
        page_size (int):
            The standard list page size.
        page_token (str):
            The standard list page token. Typically obtained via
            ``ListHyperparameterTuningJobsResponse.next_page_token``
            of the previous
            ``JobService.ListHyperparameterTuningJobs``
            call.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask specifying which fields to read.
    """

    parent = proto.Field(proto.STRING, number=1)

    filter = proto.Field(proto.STRING, number=2)

    page_size = proto.Field(proto.INT32, number=3)

    page_token = proto.Field(proto.STRING, number=4)

    read_mask = proto.Field(proto.MESSAGE, number=5, message=field_mask.FieldMask,)


class ListHyperparameterTuningJobsResponse(proto.Message):
    r"""Response message for
    ``JobService.ListHyperparameterTuningJobs``

    Attributes:
        hyperparameter_tuning_jobs (Sequence[google.cloud.aiplatform_v1beta1.types.HyperparameterTuningJob]):
            List of HyperparameterTuningJobs in the requested page.
            ``HyperparameterTuningJob.trials``
            of the jobs will be not be returned.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            ``ListHyperparameterTuningJobsRequest.page_token``
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    hyperparameter_tuning_jobs = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gca_hyperparameter_tuning_job.HyperparameterTuningJob,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class DeleteHyperparameterTuningJobRequest(proto.Message):
    r"""Request message for
    ``JobService.DeleteHyperparameterTuningJob``.

    Attributes:
        name (str):
            Required. The name of the HyperparameterTuningJob resource
            to be deleted. Format:
            ``projects/{project}/locations/{location}/hyperparameterTuningJobs/{hyperparameter_tuning_job}``
    """

    name = proto.Field(proto.STRING, number=1)


class CancelHyperparameterTuningJobRequest(proto.Message):
    r"""Request message for
    ``JobService.CancelHyperparameterTuningJob``.

    Attributes:
        name (str):
            Required. The name of the HyperparameterTuningJob to cancel.
            Format:
            ``projects/{project}/locations/{location}/hyperparameterTuningJobs/{hyperparameter_tuning_job}``
    """

    name = proto.Field(proto.STRING, number=1)


class CreateBatchPredictionJobRequest(proto.Message):
    r"""Request message for
    ``JobService.CreateBatchPredictionJob``.

    Attributes:
        parent (str):
            Required. The resource name of the Location to create the
            BatchPredictionJob in. Format:
            ``projects/{project}/locations/{location}``
        batch_prediction_job (google.cloud.aiplatform_v1beta1.types.BatchPredictionJob):
            Required. The BatchPredictionJob to create.
    """

    parent = proto.Field(proto.STRING, number=1)

    batch_prediction_job = proto.Field(
        proto.MESSAGE, number=2, message=gca_batch_prediction_job.BatchPredictionJob,
    )


class GetBatchPredictionJobRequest(proto.Message):
    r"""Request message for
    ``JobService.GetBatchPredictionJob``.

    Attributes:
        name (str):
            Required. The name of the BatchPredictionJob resource.
            Format:
            ``projects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}``
    """

    name = proto.Field(proto.STRING, number=1)


class ListBatchPredictionJobsRequest(proto.Message):
    r"""Request message for
    ``JobService.ListBatchPredictionJobs``.

    Attributes:
        parent (str):
            Required. The resource name of the Location to list the
            BatchPredictionJobs from. Format:
            ``projects/{project}/locations/{location}``
        filter (str):
            The standard list filter.

            Supported fields:

            -  ``display_name`` supports = and !=.

            -  ``state`` supports = and !=.

            -  ``model_display_name`` supports = and !=

            Some examples of using the filter are:

            -  ``state="JOB_STATE_SUCCEEDED" AND display_name="my_job"``

            -  ``state="JOB_STATE_RUNNING" OR display_name="my_job"``

            -  ``NOT display_name="my_job"``

            -  ``state="JOB_STATE_FAILED"``
        page_size (int):
            The standard list page size.
        page_token (str):
            The standard list page token. Typically obtained via
            ``ListBatchPredictionJobsResponse.next_page_token``
            of the previous
            ``JobService.ListBatchPredictionJobs``
            call.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask specifying which fields to read.
    """

    parent = proto.Field(proto.STRING, number=1)

    filter = proto.Field(proto.STRING, number=2)

    page_size = proto.Field(proto.INT32, number=3)

    page_token = proto.Field(proto.STRING, number=4)

    read_mask = proto.Field(proto.MESSAGE, number=5, message=field_mask.FieldMask,)


class ListBatchPredictionJobsResponse(proto.Message):
    r"""Response message for
    ``JobService.ListBatchPredictionJobs``

    Attributes:
        batch_prediction_jobs (Sequence[google.cloud.aiplatform_v1beta1.types.BatchPredictionJob]):
            List of BatchPredictionJobs in the requested
            page.
        next_page_token (str):
            A token to retrieve the next page of results. Pass to
            ``ListBatchPredictionJobsRequest.page_token``
            to obtain that page.
    """

    @property
    def raw_page(self):
        return self

    batch_prediction_jobs = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gca_batch_prediction_job.BatchPredictionJob,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class DeleteBatchPredictionJobRequest(proto.Message):
    r"""Request message for
    ``JobService.DeleteBatchPredictionJob``.

    Attributes:
        name (str):
            Required. The name of the BatchPredictionJob resource to be
            deleted. Format:
            ``projects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}``
    """

    name = proto.Field(proto.STRING, number=1)


class CancelBatchPredictionJobRequest(proto.Message):
    r"""Request message for
    ``JobService.CancelBatchPredictionJob``.

    Attributes:
        name (str):
            Required. The name of the BatchPredictionJob to cancel.
            Format:
            ``projects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}``
    """

    name = proto.Field(proto.STRING, number=1)


__all__ = tuple(sorted(__protobuf__.manifest))
