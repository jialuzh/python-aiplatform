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


from google.cloud.aiplatform_v1beta1.types import deployed_model_ref
from google.cloud.aiplatform_v1beta1.types import encryption_spec as gca_encryption_spec
from google.cloud.aiplatform_v1beta1.types import env_var
from google.cloud.aiplatform_v1beta1.types import explanation
from google.protobuf import struct_pb2 as struct  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1",
    manifest={"Model", "PredictSchemata", "ModelContainerSpec", "Port",},
)


class Model(proto.Message):
    r"""A trained machine learning Model.

    Attributes:
        name (str):
            The resource name of the Model.
        display_name (str):
            Required. The display name of the Model.
            The name can be up to 128 characters long and
            can be consist of any UTF-8 characters.
        description (str):
            The description of the Model.
        predict_schemata (google.cloud.aiplatform_v1beta1.types.PredictSchemata):
            The schemata that describe formats of the Model's
            predictions and explanations as given and returned via
            ``PredictionService.Predict``
            and
            ``PredictionService.Explain``.
        metadata_schema_uri (str):
            Immutable. Points to a YAML file stored on Google Cloud
            Storage describing additional information about the Model,
            that is specific to it. Unset if the Model does not have any
            additional information. The schema is defined as an OpenAPI
            3.0.2 `Schema
            Object <https://tinyurl.com/y538mdwt#schema-object>`__.
            AutoML Models always have this field populated by AI
            Platform, if no additional metadata is needed, this field is
            set to an empty string. Note: The URI given on output will
            be immutable and probably different, including the URI
            scheme, than the one given on input. The output URI will
            point to a location where the user only has a read access.
        metadata (google.protobuf.struct_pb2.Value):
            Immutable. An additional information about the Model; the
            schema of the metadata can be found in
            ``metadata_schema``.
            Unset if the Model does not have any additional information.
        supported_export_formats (Sequence[google.cloud.aiplatform_v1beta1.types.Model.ExportFormat]):
            Output only. The formats in which this Model
            may be exported. If empty, this Model is not
            available for export.
        training_pipeline (str):
            Output only. The resource name of the
            TrainingPipeline that uploaded this Model, if
            any.
        container_spec (google.cloud.aiplatform_v1beta1.types.ModelContainerSpec):
            Input only. The specification of the container that is to be
            used when deploying this Model. The specification is
            ingested upon
            ``ModelService.UploadModel``,
            and all binaries it contains are copied and stored
            internally by AI Platform. Not present for AutoML Models.
        artifact_uri (str):
            Immutable. The path to the directory
            containing the Model artifact and any of its
            supporting files. Not present for AutoML Models.
        supported_deployment_resources_types (Sequence[google.cloud.aiplatform_v1beta1.types.Model.DeploymentResourcesType]):
            Output only. When this Model is deployed, its prediction
            resources are described by the ``prediction_resources``
            field of the
            ``Endpoint.deployed_models``
            object. Because not all Models support all resource
            configuration types, the configuration types this Model
            supports are listed here. If no configuration types are
            listed, the Model cannot be deployed to an
            ``Endpoint`` and
            does not support online predictions
            (``PredictionService.Predict``
            or
            ``PredictionService.Explain``).
            Such a Model can serve predictions by using a
            ``BatchPredictionJob``,
            if it has at least one entry each in
            ``supported_input_storage_formats``
            and
            ``supported_output_storage_formats``.
        supported_input_storage_formats (Sequence[str]):
            Output only. The formats this Model supports in
            ``BatchPredictionJob.input_config``.
            If
            ``PredictSchemata.instance_schema_uri``
            exists, the instances should be given as per that schema.

            The possible formats are:

            -  ``jsonl`` The JSON Lines format, where each instance is a
               single line. Uses
               ``GcsSource``.

            -  ``csv`` The CSV format, where each instance is a single
               comma-separated line. The first line in the file is the
               header, containing comma-separated field names. Uses
               ``GcsSource``.

            -  ``tf-record`` The TFRecord format, where each instance is
               a single record in tfrecord syntax. Uses
               ``GcsSource``.

            -  ``tf-record-gzip`` Similar to ``tf-record``, but the file
               is gzipped. Uses
               ``GcsSource``.

            -  ``bigquery`` Each instance is a single row in BigQuery.
               Uses
               ``BigQuerySource``.

            -  ``file-list`` Each line of the file is the location of an
               instance to process, uses ``gcs_source`` field of the
               ``InputConfig``
               object.

            If this Model doesn't support any of these formats it means
            it cannot be used with a
            ``BatchPredictionJob``.
            However, if it has
            ``supported_deployment_resources_types``,
            it could serve online predictions by using
            ``PredictionService.Predict``
            or
            ``PredictionService.Explain``.
        supported_output_storage_formats (Sequence[str]):
            Output only. The formats this Model supports in
            ``BatchPredictionJob.output_config``.
            If both
            ``PredictSchemata.instance_schema_uri``
            and
            ``PredictSchemata.prediction_schema_uri``
            exist, the predictions are returned together with their
            instances. In other words, the prediction has the original
            instance data first, followed by the actual prediction
            content (as per the schema).

            The possible formats are:

            -  ``jsonl`` The JSON Lines format, where each prediction is
               a single line. Uses
               ``GcsDestination``.

            -  ``csv`` The CSV format, where each prediction is a single
               comma-separated line. The first line in the file is the
               header, containing comma-separated field names. Uses
               ``GcsDestination``.

            -  ``bigquery`` Each prediction is a single row in a
               BigQuery table, uses
               ``BigQueryDestination``
               .

            If this Model doesn't support any of these formats it means
            it cannot be used with a
            ``BatchPredictionJob``.
            However, if it has
            ``supported_deployment_resources_types``,
            it could serve online predictions by using
            ``PredictionService.Predict``
            or
            ``PredictionService.Explain``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this Model was
            uploaded into AI Platform.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this Model was
            most recently updated.
        deployed_models (Sequence[google.cloud.aiplatform_v1beta1.types.DeployedModelRef]):
            Output only. The pointers to DeployedModels
            created from this Model. Note that Model could
            have been deployed to Endpoints in different
            Locations.
        explanation_spec (google.cloud.aiplatform_v1beta1.types.ExplanationSpec):
            The default explanation specification for this Model.

            The Model can be used for [requesting
            explanation][PredictionService.Explain] after being
            ``deployed``
            if it is populated. The Model can be used for [batch
            explanation][BatchPredictionJob.generate_explanation] if it
            is populated.

            All fields of the explanation_spec can be overridden by
            ``explanation_spec``
            of
            ``DeployModelRequest.deployed_model``,
            or
            ``explanation_spec``
            of
            ``BatchPredictionJob``.

            If the default explanation specification is not set for this
            Model, this Model can still be used for [requesting
            explanation][PredictionService.Explain] by setting
            ``explanation_spec``
            of
            ``DeployModelRequest.deployed_model``
            and for [batch
            explanation][BatchPredictionJob.generate_explanation] by
            setting
            ``explanation_spec``
            of
            ``BatchPredictionJob``.
        etag (str):
            Used to perform consistent read-modify-write
            updates. If not set, a blind "overwrite" update
            happens.
        labels (Sequence[google.cloud.aiplatform_v1beta1.types.Model.LabelsEntry]):
            The labels with user-defined metadata to
            organize your Models.
            Label keys and values can be no longer than 64
            characters (Unicode codepoints), can only
            contain lowercase letters, numeric characters,
            underscores and dashes. International characters
            are allowed.
            See https://goo.gl/xmQnxf for more information
            and examples of labels.
        encryption_spec (google.cloud.aiplatform_v1beta1.types.EncryptionSpec):
            Customer-managed encryption key spec for a
            Model. If set, this Model and all sub-resources
            of this Model will be secured by this key.
    """

    class DeploymentResourcesType(proto.Enum):
        r"""Identifies a type of Model's prediction resources."""
        DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED = 0
        DEDICATED_RESOURCES = 1
        AUTOMATIC_RESOURCES = 2

    class ExportFormat(proto.Message):
        r"""Represents export format supported by the Model.
        All formats export to Google Cloud Storage.

        Attributes:
            id (str):
                Output only. The ID of the export format. The possible
                format IDs are:

                -  ``tflite`` Used for Android mobile devices.

                -  ``edgetpu-tflite`` Used for `Edge
                   TPU <https://cloud.google.com/edge-tpu/>`__ devices.

                -  ``tf-saved-model`` A tensorflow model in SavedModel
                   format.

                -  ``tf-js`` A
                   `TensorFlow.js <https://www.tensorflow.org/js>`__ model
                   that can be used in the browser and in Node.js using
                   JavaScript.

                -  ``core-ml`` Used for iOS mobile devices.

                -  ``custom-trained`` A Model that was uploaded or trained
                   by custom code.
            exportable_contents (Sequence[google.cloud.aiplatform_v1beta1.types.Model.ExportFormat.ExportableContent]):
                Output only. The content of this Model that
                may be exported.
        """

        class ExportableContent(proto.Enum):
            r"""The Model content that can be exported."""
            EXPORTABLE_CONTENT_UNSPECIFIED = 0
            ARTIFACT = 1
            IMAGE = 2

        id = proto.Field(proto.STRING, number=1)

        exportable_contents = proto.RepeatedField(
            proto.ENUM, number=2, enum="Model.ExportFormat.ExportableContent",
        )

    name = proto.Field(proto.STRING, number=1)

    display_name = proto.Field(proto.STRING, number=2)

    description = proto.Field(proto.STRING, number=3)

    predict_schemata = proto.Field(proto.MESSAGE, number=4, message="PredictSchemata",)

    metadata_schema_uri = proto.Field(proto.STRING, number=5)

    metadata = proto.Field(proto.MESSAGE, number=6, message=struct.Value,)

    supported_export_formats = proto.RepeatedField(
        proto.MESSAGE, number=20, message=ExportFormat,
    )

    training_pipeline = proto.Field(proto.STRING, number=7)

    container_spec = proto.Field(proto.MESSAGE, number=9, message="ModelContainerSpec",)

    artifact_uri = proto.Field(proto.STRING, number=26)

    supported_deployment_resources_types = proto.RepeatedField(
        proto.ENUM, number=10, enum=DeploymentResourcesType,
    )

    supported_input_storage_formats = proto.RepeatedField(proto.STRING, number=11)

    supported_output_storage_formats = proto.RepeatedField(proto.STRING, number=12)

    create_time = proto.Field(proto.MESSAGE, number=13, message=timestamp.Timestamp,)

    update_time = proto.Field(proto.MESSAGE, number=14, message=timestamp.Timestamp,)

    deployed_models = proto.RepeatedField(
        proto.MESSAGE, number=15, message=deployed_model_ref.DeployedModelRef,
    )

    explanation_spec = proto.Field(
        proto.MESSAGE, number=23, message=explanation.ExplanationSpec,
    )

    etag = proto.Field(proto.STRING, number=16)

    labels = proto.MapField(proto.STRING, proto.STRING, number=17)

    encryption_spec = proto.Field(
        proto.MESSAGE, number=24, message=gca_encryption_spec.EncryptionSpec,
    )


class PredictSchemata(proto.Message):
    r"""Contains the schemata used in Model's predictions and explanations
    via
    ``PredictionService.Predict``,
    ``PredictionService.Explain``
    and
    ``BatchPredictionJob``.

    Attributes:
        instance_schema_uri (str):
            Immutable. Points to a YAML file stored on Google Cloud
            Storage describing the format of a single instance, which
            are used in
            ``PredictRequest.instances``,
            ``ExplainRequest.instances``
            and
            ``BatchPredictionJob.input_config``.
            The schema is defined as an OpenAPI 3.0.2 `Schema
            Object <https://tinyurl.com/y538mdwt#schema-object>`__.
            AutoML Models always have this field populated by AI
            Platform. Note: The URI given on output will be immutable
            and probably different, including the URI scheme, than the
            one given on input. The output URI will point to a location
            where the user only has a read access.
        parameters_schema_uri (str):
            Immutable. Points to a YAML file stored on Google Cloud
            Storage describing the parameters of prediction and
            explanation via
            ``PredictRequest.parameters``,
            ``ExplainRequest.parameters``
            and
            ``BatchPredictionJob.model_parameters``.
            The schema is defined as an OpenAPI 3.0.2 `Schema
            Object <https://tinyurl.com/y538mdwt#schema-object>`__.
            AutoML Models always have this field populated by AI
            Platform, if no parameters are supported, then it is set to
            an empty string. Note: The URI given on output will be
            immutable and probably different, including the URI scheme,
            than the one given on input. The output URI will point to a
            location where the user only has a read access.
        prediction_schema_uri (str):
            Immutable. Points to a YAML file stored on Google Cloud
            Storage describing the format of a single prediction
            produced by this Model, which are returned via
            ``PredictResponse.predictions``,
            ``ExplainResponse.explanations``,
            and
            ``BatchPredictionJob.output_config``.
            The schema is defined as an OpenAPI 3.0.2 `Schema
            Object <https://tinyurl.com/y538mdwt#schema-object>`__.
            AutoML Models always have this field populated by AI
            Platform. Note: The URI given on output will be immutable
            and probably different, including the URI scheme, than the
            one given on input. The output URI will point to a location
            where the user only has a read access.
    """

    instance_schema_uri = proto.Field(proto.STRING, number=1)

    parameters_schema_uri = proto.Field(proto.STRING, number=2)

    prediction_schema_uri = proto.Field(proto.STRING, number=3)


class ModelContainerSpec(proto.Message):
    r"""Specification of a container for serving predictions. This message
    is a subset of the Kubernetes Container v1 core
    `specification <https://tinyurl.com/k8s-io-api/v1.18/#container-v1-core>`__.

    Attributes:
        image_uri (str):
            Required. Immutable. URI of the Docker image to be used as
            the custom container for serving predictions. This URI must
            identify an image in Artifact Registry or Container
            Registry. Learn more about the container publishing
            requirements, including permissions requirements for the AI
            Platform Service Agent,
            `here <https://tinyurl.com/cust-cont-reqs#publishing>`__.

            The container image is ingested upon
            ``ModelService.UploadModel``,
            stored internally, and this original path is afterwards not
            used.

            To learn about the requirements for the Docker image itself,
            see `Custom container
            requirements <https://tinyurl.com/cust-cont-reqs>`__.

            You can use the URI to one of AI Platform's `pre-built
            container images for
            prediction <https://cloud.google.com/ai-platform-unified/docs/predictions/pre-built-containers>`__
            in this field.
        command (Sequence[str]):
            Immutable. Specifies the command that runs when the
            container starts. This overrides the container's
            `ENTRYPOINT <https://docs.docker.com/engine/reference/builder/#entrypoint>`__.
            Specify this field as an array of executable and arguments,
            similar to a Docker ``ENTRYPOINT``'s "exec" form, not its
            "shell" form.

            If you do not specify this field, then the container's
            ``ENTRYPOINT`` runs, in conjunction with the
            ``args``
            field or the container's
            ```CMD`` <https://docs.docker.com/engine/reference/builder/#cmd>`__,
            if either exists. If this field is not specified and the
            container does not have an ``ENTRYPOINT``, then refer to the
            Docker documentation about how ``CMD`` and ``ENTRYPOINT``
            `interact <https://tinyurl.com/h3kdcgs>`__.

            If you specify this field, then you can also specify the
            ``args`` field to provide additional arguments for this
            command. However, if you specify this field, then the
            container's ``CMD`` is ignored. See the `Kubernetes
            documentation <https://tinyurl.com/y8bvllf4>`__ about how
            the ``command`` and ``args`` fields interact with a
            container's ``ENTRYPOINT`` and ``CMD``.

            In this field, you can reference environment variables `set
            by AI
            Platform <https://tinyurl.com/cust-cont-reqs#aip-variables>`__
            and environment variables set in the
            ``env``
            field. You cannot reference environment variables set in the
            Docker image. In order for environment variables to be
            expanded, reference them by using the following syntax:
            $(VARIABLE_NAME) Note that this differs from Bash variable
            expansion, which does not use parentheses. If a variable
            cannot be resolved, the reference in the input string is
            used unchanged. To avoid variable expansion, you can escape
            this syntax with ``$$``; for example: $$(VARIABLE_NAME) This
            field corresponds to the ``command`` field of the Kubernetes
            Containers `v1 core
            API <https://tinyurl.com/k8s-io-api/v1.18/#container-v1-core>`__.
        args (Sequence[str]):
            Immutable. Specifies arguments for the command that runs
            when the container starts. This overrides the container's
            ```CMD`` <https://docs.docker.com/engine/reference/builder/#cmd>`__.
            Specify this field as an array of executable and arguments,
            similar to a Docker ``CMD``'s "default parameters" form.

            If you don't specify this field but do specify the
            ``command``
            field, then the command from the ``command`` field runs
            without any additional arguments. See the `Kubernetes
            documentation <https://tinyurl.com/y8bvllf4>`__ about how
            the ``command`` and ``args`` fields interact with a
            container's ``ENTRYPOINT`` and ``CMD``.

            If you don't specify this field and don't specify the
            ``command`` field, then the container's
            ```ENTRYPOINT`` <https://docs.docker.com/engine/reference/builder/#cmd>`__
            and ``CMD`` determine what runs based on their default
            behavior. See the Docker documentation about how ``CMD`` and
            ``ENTRYPOINT`` `interact <https://tinyurl.com/h3kdcgs>`__.

            In this field, you can reference environment variables `set
            by AI
            Platform <https://tinyurl.com/cust-cont-reqs#aip-variables>`__
            and environment variables set in the
            ``env``
            field. You cannot reference environment variables set in the
            Docker image. In order for environment variables to be
            expanded, reference them by using the following syntax:
            $(VARIABLE_NAME) Note that this differs from Bash variable
            expansion, which does not use parentheses. If a variable
            cannot be resolved, the reference in the input string is
            used unchanged. To avoid variable expansion, you can escape
            this syntax with ``$$``; for example: $$(VARIABLE_NAME) This
            field corresponds to the ``args`` field of the Kubernetes
            Containers `v1 core
            API <https://tinyurl.com/k8s-io-api/v1.18/#container-v1-core>`__.
        env (Sequence[google.cloud.aiplatform_v1beta1.types.EnvVar]):
            Immutable. List of environment variables to set in the
            container. After the container starts running, code running
            in the container can read these environment variables.

            Additionally, the
            ``command``
            and
            ``args``
            fields can reference these variables. Later entries in this
            list can also reference earlier entries. For example, the
            following example sets the variable ``VAR_2`` to have the
            value ``foo bar``:

            .. code:: json

               [
                 {
                   "name": "VAR_1",
                   "value": "foo"
                 },
                 {
                   "name": "VAR_2",
                   "value": "$(VAR_1) bar"
                 }
               ]

            If you switch the order of the variables in the example,
            then the expansion does not occur.

            This field corresponds to the ``env`` field of the
            Kubernetes Containers `v1 core
            API <https://tinyurl.com/k8s-io-api/v1.18/#container-v1-core>`__.
        ports (Sequence[google.cloud.aiplatform_v1beta1.types.Port]):
            Immutable. List of ports to expose from the container. AI
            Platform sends any prediction requests that it receives to
            the first port on this list. AI Platform also sends
            `liveness and health
            checks <https://tinyurl.com/cust-cont-reqs#health>`__ to
            this port.

            If you do not specify this field, it defaults to following
            value:

            .. code:: json

               [
                 {
                   "containerPort": 8080
                 }
               ]

            AI Platform does not use ports other than the first one
            listed. This field corresponds to the ``ports`` field of the
            Kubernetes Containers `v1 core
            API <https://tinyurl.com/k8s-io-api/v1.18/#container-v1-core>`__.
        predict_route (str):
            Immutable. HTTP path on the container to send prediction
            requests to. AI Platform forwards requests sent using
            ``projects.locations.endpoints.predict``
            to this path on the container's IP address and port. AI
            Platform then returns the container's response in the API
            response.

            For example, if you set this field to ``/foo``, then when AI
            Platform receives a prediction request, it forwards the
            request body in a POST request to the ``/foo`` path on the
            port of your container specified by the first value of this
            ``ModelContainerSpec``'s
            ``ports``
            field.

            If you don't specify this field, it defaults to the
            following value when you [deploy this Model to an
            Endpoint][google.cloud.aiplatform.v1beta1.EndpointService.DeployModel]:
            /v1/endpoints/ENDPOINT/deployedModels/DEPLOYED_MODEL:predict
            The placeholders in this value are replaced as follows:

            -  ENDPOINT: The last segment (following ``endpoints/``)of
               the Endpoint.name][] field of the Endpoint where this
               Model has been deployed. (AI Platform makes this value
               available to your container code as the
               ```AIP_ENDPOINT_ID`` <https://tinyurl.com/cust-cont-reqs#aip-variables>`__
               environment variable.)

            -  DEPLOYED_MODEL:
               ``DeployedModel.id``
               of the ``DeployedModel``. (AI Platform makes this value
               available to your container code as the
               ```AIP_DEPLOYED_MODEL_ID`` environment
               variable <https://tinyurl.com/cust-cont-reqs#aip-variables>`__.)
        health_route (str):
            Immutable. HTTP path on the container to send health checks
            to. AI Platform intermittently sends GET requests to this
            path on the container's IP address and port to check that
            the container is healthy. Read more about `health
            checks <https://tinyurl.com/cust-cont-reqs#checks>`__.

            For example, if you set this field to ``/bar``, then AI
            Platform intermittently sends a GET request to the ``/bar``
            path on the port of your container specified by the first
            value of this ``ModelContainerSpec``'s
            ``ports``
            field.

            If you don't specify this field, it defaults to the
            following value when you [deploy this Model to an
            Endpoint][google.cloud.aiplatform.v1beta1.EndpointService.DeployModel]:
            /v1/endpoints/ENDPOINT/deployedModels/DEPLOYED_MODEL:predict
            The placeholders in this value are replaced as follows:

            -  ENDPOINT: The last segment (following ``endpoints/``)of
               the Endpoint.name][] field of the Endpoint where this
               Model has been deployed. (AI Platform makes this value
               available to your container code as the
               ```AIP_ENDPOINT_ID`` <https://tinyurl.com/cust-cont-reqs#aip-variables>`__
               environment variable.)

            -  DEPLOYED_MODEL:
               ``DeployedModel.id``
               of the ``DeployedModel``. (AI Platform makes this value
               available to your container code as the
               ```AIP_DEPLOYED_MODEL_ID`` <https://tinyurl.com/cust-cont-reqs#aip-variables>`__
               environment variable.)
    """

    image_uri = proto.Field(proto.STRING, number=1)

    command = proto.RepeatedField(proto.STRING, number=2)

    args = proto.RepeatedField(proto.STRING, number=3)

    env = proto.RepeatedField(proto.MESSAGE, number=4, message=env_var.EnvVar,)

    ports = proto.RepeatedField(proto.MESSAGE, number=5, message="Port",)

    predict_route = proto.Field(proto.STRING, number=6)

    health_route = proto.Field(proto.STRING, number=7)


class Port(proto.Message):
    r"""Represents a network port in a container.

    Attributes:
        container_port (int):
            The number of the port to expose on the pod's
            IP address. Must be a valid port number, between
            1 and 65535 inclusive.
    """

    container_port = proto.Field(proto.INT32, number=3)


__all__ = tuple(sorted(__protobuf__.manifest))
