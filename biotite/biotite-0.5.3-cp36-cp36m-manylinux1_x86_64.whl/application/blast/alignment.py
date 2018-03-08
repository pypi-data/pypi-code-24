# Copyright 2017 Patrick Kunzmann.
# This source code is part of the Biotite package and is distributed under the
# 3-Clause BSD License. Please see 'LICENSE.rst' for further information.

from ...sequence.align.alignment import Alignment

__all__ = ["BlastAlignment"]

class BlastAlignment(Alignment):
    """
    A specialized `Alignment` class for alignments using the BLAST
    application. It stores additional data, like the E-value, the HSP
    position and a description of the hit sequence.
    
    Like its superclass, all attributes of a `BlastAlignment` are
    public. The attributes are the same as the constructor parameters.
    
    Parameters
    ----------
    sequences : list
        A list of aligned sequences. Does actually not contain the
        complete original sequences, but the HSP sequences.
    trace : ndarray, dtype=int, shape=(n,m)
        The alignment trace.
    score : int
        Alignment score.
    e_value : float
        Expectation value for the number of random sequences of a
        similar sized database getting an equal or higher score by
        change when aligned with the query sequence.
    query_interval : tuple of int
        Describes the position of the HSP part of the query sequence
        in the original query sequence. The first element is the start
        position, the second element is the inclusive stop position.
        Indexing starts at 1.
    hit_interval : tuple of int
        Analogous to `query_interval`, this describes the position of
        the HSP part of the hit sequence in the complete hit sequence.
    hit_id : str
        The NCBI *unique identifier* (UID) of the hit sequence.
    hit_definition : str
        The name of the hit sequence.
    """
    
    def __init__(self, sequences, trace, score, e_value,
                 query_interval, hit_interval, hit_id, hit_definition):
        super().__init__(sequences, trace, score)
        self.e_value = e_value
        self.query_interval = query_interval
        self.hit_interval = hit_interval
        self.hit_id = hit_id
        self.hit_definition = hit_definition