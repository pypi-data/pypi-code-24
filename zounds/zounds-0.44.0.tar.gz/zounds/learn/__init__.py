"""
The `learn` module includes classes that make it possible to define processing
graphs whose leaves are trained machine learning models.

While much of :module:`zounds.soundfile`, :module:`zounds.spectral`, and
:module:`zounds.timeseries` focus on processing nodes that can be composed into
a processing graph to extract features from a single piece of audio, the `learn`
module focuses on defining graphs that extract features or trained models from
an entire corpus of audio.
"""

from learn import KMeans, Learned

from preprocess import \
    MeanStdNormalization, UnitNorm, Log, PreprocessingPipeline, Multiply, \
    Slicer, InstanceScaling, Reshape, Weighted, MuLawCompressed, SimHash, \
    AbsoluteValue, Binarize, Sharpen

from sklearn_preprocessor import SklearnModel, WithComponents

from pytorch_model import PyTorchAutoEncoder, PyTorchGan, PyTorchNetwork

from gan import GanTrainer
from wgan import WassersteinGanTrainer
from supervised import SupervisedTrainer
from embedding import TripletEmbeddingTrainer

from random_samples import Reservoir, ReservoirSampler, ShuffledSamples

from util import simple_settings, object_store_pipeline_settings, model_hash

from graph import learning_pipeline, infinite_streaming_learning_pipeline

from functional import hyperplanes, simhash, example_wise_unit_norm

try:
    from util import \
        Conv1d, ConvTranspose1d, Conv2d, ConvTranspose2d, to_var, from_var, \
        try_network, apply_network, feature_map_size, sample_norm, \
        FrequencyDecompositionAnalyzer, FrequencyDecompositionGenerator
    from gan_experiment import GanExperiment
    from sample_embedding import RawSampleEmbedding
    from dct_transform import DctTransform
    from gated import GatedConvTransposeLayer, GatedConvLayer
except ImportError:
    pass


