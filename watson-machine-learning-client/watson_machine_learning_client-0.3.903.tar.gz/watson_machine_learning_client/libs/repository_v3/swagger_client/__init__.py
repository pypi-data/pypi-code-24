# coding: utf-8

"""
    IBM Watson Machine Learning REST API

    ## Authorization  ### IBM Watson Machine Learning Credentials  To start working with API one needs to generate an `access token` using the `username` and `password` available on the Service Credentials tab of the IBM Watson Machine Learning service instance or also available in the VCAP environment variable.  Example of the Service Credentials:  ```json {     \"url\": \"https://ibm-watson-ml.mybluemix.net\",     \"access_key\": \"ERY9vcBfE4sE+F4g8hcotF9L+j81WXWeZv\",     \"username\": \"c1ef4b80-2ee2-458e-ab92-e9ca97ec657d\",     \"password\": \"030528d4-5a3e-4d4c-9258-5d553513be6f\" } ```  Example of obtaining `access token` from Token Endpoint using HTTP Basic Auth (for details please refer to Token section below):  ` curl --basic --user username:password https://ibm-watson-ml.mybluemix.net/v3/identity/token `   ### Apache Spark Service Credentials  The IBM Watson Machine Learning co-operates with the Apache Spark as a Service to deploy pipeline models. For API methods requiring Apache Spark Service instance a custom header: `X-Spark-Service-Instance` with Service Credentials must be specified. The header value is a **base64 encoded** string with the Service Credentials JSON data.  [Example of API method requiring Apache Spark Service](https://console.ng.bluemix.net/docs/services/PredictiveModeling/index-gentopic1.html#pm_service_api_spark_batch)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

# import models into sdk package
from .models.array_model_metrics_output import ArrayModelMetricsOutput
from .models.array_model_output import ArrayModelOutput
from .models.array_model_version_output import ArrayModelVersionOutput
from .models.array_pipeline_output import ArrayPipelineOutput
from .models.array_pipeline_version_output import ArrayPipelineVersionOutput
from .models.artifact_author import ArtifactAuthor
from .models.artifact_version_metadata import ArtifactVersionMetadata
from .models.artifact_version_short_metadata import ArtifactVersionShortMetadata
from .models.batch_deploy_output import BatchDeployOutput
from .models.batch_deploy_output_entity import BatchDeployOutputEntity
from .models.batch_deploy_output_entity_execution import BatchDeployOutputEntityExecution
from .models.batch_deploy_output_meta import BatchDeployOutputMeta
from .models.batch_input import BatchInput
from .models.batch_output import BatchOutput
from .models.batch_output_array import BatchOutputArray
from .models.cols_output import ColsOutput
from .models.connection import Connection
from .models.deploy_input import DeployInput
from .models.error_message import ErrorMessage
from .models.evaluation_definition import EvaluationDefinition
from .models.evaluation_definition_metrics import EvaluationDefinitionMetrics
from .models.input_data_schema import InputDataSchema
from .models.internal_input_batch import InternalInputBatch
from .models.internal_output_batch import InternalOutputBatch
from .models.json_patch_array import JsonPatchArray
from .models.json_patch_entity import JsonPatchEntity
from .models.meta_object import MetaObject
from .models.meta_object_metadata import MetaObjectMetadata
from .models.model_input import ModelInput
from .models.model_metrics import ModelMetrics
from .models.model_metrics_values import ModelMetricsValues
from .models.model_output import ModelOutput
from .models.model_output_entity import ModelOutputEntity
from .models.model_output_entity_pipeline_version import ModelOutputEntityPipelineVersion
from .models.model_training_data_ref import ModelTrainingDataRef
from .models.model_type import ModelType
from .models.model_version_input import ModelVersionInput
from .models.model_version_output import ModelVersionOutput
from .models.model_version_output_entity import ModelVersionOutputEntity
from .models.model_version_output_entity_model import ModelVersionOutputEntityModel
from .models.online_deploy_output import OnlineDeployOutput
from .models.online_output import OnlineOutput
from .models.online_output_array import OnlineOutputArray
from .models.pipeline_input import PipelineInput
from .models.pipeline_output import PipelineOutput
from .models.pipeline_output_entity import PipelineOutputEntity
from .models.pipeline_type import PipelineType
from .models.pipeline_version_input import PipelineVersionInput
from .models.pipeline_version_output import PipelineVersionOutput
from .models.pipeline_version_output_entity import PipelineVersionOutputEntity
from .models.pipeline_version_output_entity_parent import PipelineVersionOutputEntityParent
from .models.runtime_environment import RuntimeEnvironment
from .models.score_input import ScoreInput
from .models.score_output import ScoreOutput
from .models.spark_service import SparkService
from .models.stream_input_internal import StreamInputInternal
from .models.stream_internal import StreamInternal
from .models.stream_output import StreamOutput
from .models.stream_output_array import StreamOutputArray
from .models.stream_output_internal import StreamOutputInternal
from .models.token_response import TokenResponse
from .models.training_data_schema import TrainingDataSchema

# import v3 models into sdk package
from .models.array_data_input_repository import ArrayDataInputRepository
from .models.artifact_version_repository import ArtifactVersionRepository
from .models.author_repository import AuthorRepository
from .models.connection_object_with_name_repository import ConnectionObjectWithNameRepository
from .models.error_repository import ErrorRepository
from .models.error_repository_target import ErrorRepositoryTarget
from .models.error_schema_repository import ErrorSchemaRepository
from .models.evaluation_definition_repository import EvaluationDefinitionRepository
from .models.evaluation_definition_repository_metrics import EvaluationDefinitionRepositoryMetrics
from .models.framework_output_repository import FrameworkOutputRepository
from .models.framework_output_repository_libraries import FrameworkOutputRepositoryLibraries
from .models.framework_output_repository_runtimes import  FrameworkOutputRepositoryRuntimes
from .models.meta_object_repository import MetaObjectRepository
from .models.meta_object_repository_metadata import MetaObjectRepositoryMetadata
from .models.ml_assets_create_experiment_input import MlAssetsCreateExperimentInput
from .models.ml_assets_create_experiment_output import MlAssetsCreateExperimentOutput
from .models.ml_assets_create_experiment_output_array import MlAssetsCreateExperimentOutputArray
from .models.ml_assets_create_model_input import MlAssetsCreateModelInput
from .models.ml_assets_create_model_output import MlAssetsCreateModelOutput
from .models.ml_assets_create_model_output_array import MlAssetsCreateModelOutputArray
from .models.content_location import ContentLocation
from .models.content_status import ContentStatus





# import models into sdk package
from .models.array_model_version_metrics_experiments import ArrayModelVersionMetricsExperiments
from .models.array_training_output_experiments import ArrayTrainingOutputExperiments
from .models.author_experiments import AuthorExperiments
from .models.compute_configuration_experiments import ComputeConfigurationExperiments
from .models.connection_object_source_experiments import ConnectionObjectSourceExperiments
from .models.connection_object_target_experiments import ConnectionObjectTargetExperiments
from .models.error_experiments import ErrorExperiments
from .models.error_experiments_target import ErrorExperimentsTarget
from .models.error_schema_experiments import ErrorSchemaExperiments
from .models.evaluation_definition_experiments import EvaluationDefinitionExperiments
from .models.experiment_asset_tag import ExperimentAssetTag
from .models.experiment_input import ExperimentInput
from .models.experiment_input_settings import ExperimentInputSettings
from .models.experiment_output_array import ExperimentOutputArray
from .models.experiment_output_array_first import ExperimentOutputArrayFirst
from .models.experiment_output import ExperimentOutput
from .models.experiment_patch import ExperimentPatch
from .models.experiment_status_experiments import ExperimentStatusExperiments
from .models.hyper_parameters_experiments import HyperParametersExperiments
from .models.hyper_parameters_experiments_inner_values_range import HyperParametersExperimentsInnerValuesRange
from .models.hyper_parameters_for_status_experiments import HyperParametersForStatusExperiments
from .models.hyper_parameters_for_status_experiments_inner import HyperParametersForStatusExperimentsInner
from .models.hyper_parameters_optimization_experiments import HyperParametersOptimizationExperiments
from .models.meta_object_experiments import MetaObjectExperiments
from .models.meta_object_experiments_metadata import MetaObjectExperimentsMetadata
from .models.metric_object_experiments import MetricObjectExperiments
from .models.model_version_metrics_experiments import ModelVersionMetricsExperiments
from .models.patch_operation_experiments import PatchOperationExperiments
from .models.training_output_experiments import TrainingOutputExperiments
from .models.training_reference_experiments import TrainingReferenceExperiments
from .models.training_status_experiments import TrainingStatusExperiments
from .models.training_status_experiments_result import TrainingStatusExperimentsResult
from .models.hyper_parameters import HyperParameters














# import apis into sdk package
from .apis.repository_api import RepositoryApi
from .apis.token_api import TokenApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
