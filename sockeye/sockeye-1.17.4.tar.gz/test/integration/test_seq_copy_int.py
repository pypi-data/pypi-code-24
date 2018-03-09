# Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not
# use this file except in compliance with the License. A copy of the License
# is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

import pytest

from test.common import run_train_translate, tmp_digits_dataset

_TRAIN_LINE_COUNT = 100
_DEV_LINE_COUNT = 10
_TEST_LINE_COUNT = 10
_TEST_LINE_COUNT_EMPTY = 2
_LINE_MAX_LENGTH = 9
_TEST_MAX_LENGTH = 20

ENCODER_DECODER_SETTINGS = [
    # "Vanilla" LSTM encoder-decoder with attention
    ("--encoder rnn --num-layers 1 --rnn-cell-type lstm --rnn-num-hidden 16 --num-embed 8 --rnn-attention-type mlp"
     " --rnn-attention-num-hidden 16 --batch-size 8 --loss cross-entropy --optimized-metric perplexity --max-updates 10"
     " --checkpoint-frequency 10 --optimizer adam --initial-learning-rate 0.01",
     "--beam-size 2",
     True, False, False),
    # "Kitchen sink" LSTM encoder-decoder with attention
    ("--encoder rnn --num-layers 4:2 --rnn-cell-type lstm --rnn-num-hidden 16"
     " --rnn-residual-connections"
     " --num-embed 16 --rnn-attention-type coverage --rnn-attention-num-hidden 16 --weight-tying "
     "--rnn-attention-use-prev-word --rnn-context-gating --layer-normalization --batch-size 8 "
     "--loss cross-entropy --label-smoothing 0.1 --loss-normalization-type batch --optimized-metric perplexity"
     " --max-updates 10 --checkpoint-frequency 10 --optimizer adam --initial-learning-rate 0.01"
     " --rnn-dropout-inputs 0.5:0.1 --rnn-dropout-states 0.5:0.1 --embed-dropout 0.1 --rnn-decoder-hidden-dropout 0.01"
     " --rnn-decoder-state-init avg --rnn-encoder-reverse-input --rnn-dropout-recurrent 0.1:0.0"
     " --learning-rate-decay-param-reset --weight-normalization --source-factors-num-embed 5",
     "--beam-size 2",
     False, True, True),
    # Convolutional embedding encoder + LSTM encoder-decoder with attention
    ("--encoder rnn-with-conv-embed --conv-embed-max-filter-width 3 --conv-embed-num-filters 4:4:8"
     " --conv-embed-pool-stride 2 --conv-embed-num-highway-layers 1 --num-layers 1 --rnn-cell-type lstm"
     " --rnn-num-hidden 16 --num-embed 8 --rnn-attention-num-hidden 16 --batch-size 8 --loss cross-entropy"
     " --optimized-metric perplexity --max-updates 10 --checkpoint-frequency 10 --optimizer adam"
     " --initial-learning-rate 0.01",
     "--beam-size 2",
     False, False, False),
    # Transformer encoder, GRU decoder, mhdot attention
    ("--encoder transformer --num-layers 2:1 --rnn-cell-type gru --rnn-num-hidden 16 --num-embed 8:16"
     " --transformer-attention-heads 2 --transformer-model-size 8"
     " --transformer-feed-forward-num-hidden 32 --transformer-activation-type gelu"
     " --rnn-attention-type mhdot --rnn-attention-mhdot-heads 4 --rnn-attention-num-hidden 16 --batch-size 8 "
     " --max-updates 10 --checkpoint-frequency 10 --optimizer adam --initial-learning-rate 0.01"
     " --weight-init-xavier-factor-type avg --weight-init-scale 3.0 --embed-weight-init normal",
     "--beam-size 2",
     False, True, False),
    # LSTM encoder, Transformer decoder
    ("--encoder rnn --decoder transformer --num-layers 2:2 --rnn-cell-type lstm --rnn-num-hidden 16 --num-embed 16"
     " --transformer-attention-heads 2 --transformer-model-size 16"
     " --transformer-feed-forward-num-hidden 32 --transformer-activation-type swish1"
     " --batch-size 8 --max-updates 10"
     " --checkpoint-frequency 10 --optimizer adam --initial-learning-rate 0.01",
     "--beam-size 3",
     False, True, False),
    # Full transformer
    ("--encoder transformer --decoder transformer"
     " --num-layers 3 --transformer-attention-heads 2 --transformer-model-size 16 --num-embed 16"
     " --transformer-feed-forward-num-hidden 32"
     " --transformer-dropout-prepost 0.1 --transformer-preprocess n --transformer-postprocess dr"
     " --weight-tying --weight-tying-type src_trg_softmax"
     " --batch-size 8 --max-updates 10"
     " --checkpoint-frequency 10 --optimizer adam --initial-learning-rate 0.01",
     "--beam-size 2",
     True, False, False),
    # Full transformer with source factor
    ("--encoder transformer --decoder transformer"
     " --num-layers 3 --transformer-attention-heads 2 --transformer-model-size 16 --num-embed 16"
     " --transformer-feed-forward-num-hidden 32"
     " --transformer-dropout-prepost 0.1 --transformer-preprocess n --transformer-postprocess dr"
     " --weight-tying --weight-tying-type src_trg_softmax"
     " --batch-size 8 --max-updates 10"
     " --checkpoint-frequency 10 --optimizer adam --initial-learning-rate 0.01 --source-factors-num-embed 4",
     "--beam-size 2",
     True, False, True),
    # 3-layer cnn
    ("--encoder cnn --decoder cnn "
     " --batch-size 16 --num-layers 3 --max-updates 10 --checkpoint-frequency 10"
     " --cnn-num-hidden 32 --cnn-positional-embedding-type fixed"
     " --optimizer adam --initial-learning-rate 0.001",
     "--beam-size 2",
     True, False, False)]


@pytest.mark.parametrize("train_params, translate_params, restrict_lexicon, use_prepared_data, use_source_factors",
                         ENCODER_DECODER_SETTINGS)
def test_seq_copy(train_params: str,
                  translate_params: str,
                  restrict_lexicon: bool,
                  use_prepared_data: bool,
                  use_source_factors: bool):
    """Task: copy short sequences of digits"""

    with tmp_digits_dataset(prefix="test_seq_copy",
                            train_line_count=_TRAIN_LINE_COUNT,
                            train_max_length=_LINE_MAX_LENGTH,
                            dev_line_count=_DEV_LINE_COUNT,
                            dev_max_length=_LINE_MAX_LENGTH,
                            test_line_count=_TEST_LINE_COUNT,
                            test_line_count_empty=_TEST_LINE_COUNT_EMPTY,
                            test_max_length=_TEST_MAX_LENGTH,
                            sort_target=False) as data:

        # Test model configuration, including the output equivalence of batch and no-batch decoding
        translate_params_batch = translate_params + " --batch-size 2"

        # When using source factors
        train_source_factor_paths, dev_source_factor_paths, test_source_factor_paths = None, None, None
        if use_source_factors:
            train_source_factor_paths = [data['source']]
            dev_source_factor_paths = [data['validation_source']]
            test_source_factor_paths = [data['test_source']]

        # Ignore return values (perplexity and BLEU) for integration test
        run_train_translate(train_params=train_params,
                            translate_params=translate_params,
                            translate_params_equiv=translate_params_batch,
                            train_source_path=data['source'],
                            train_target_path=data['target'],
                            dev_source_path=data['validation_source'],
                            dev_target_path=data['validation_target'],
                            test_source_path=data['test_source'],
                            test_target_path=data['test_target'],
                            train_source_factor_paths=train_source_factor_paths,
                            dev_source_factor_paths=dev_source_factor_paths,
                            test_source_factor_paths=test_source_factor_paths,
                            max_seq_len=_LINE_MAX_LENGTH + 1,
                            restrict_lexicon=restrict_lexicon,
                            work_dir=data['work_dir'],
                            use_prepared_data=use_prepared_data)
