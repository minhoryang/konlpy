# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import io
import json
import os


installpath = os.path.dirname(os.path.realpath(__file__))


def read_json(filename, encoding='utf-8'):
    """JSON file reader."""
    with io.open(filename, 'r', encoding=encoding) as f:
        return json.load(f)


def partition(list_, indices):
    """Partitions a list to several parts using indices.

    :param list_: The target list.
    :param indices: Indices to partition the target list.
    """
    return [list_[i:j] for i, j in zip([0] + indices, indices + [None])]
