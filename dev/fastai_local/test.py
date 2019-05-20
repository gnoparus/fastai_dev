#AUTOGENERATED! DO NOT EDIT! File to edit: dev/00_test.ipynb (unless otherwise specified).

from fastai.gen_doc.nbdoc import show_doc
import matplotlib.pyplot as plt,numpy as np,pandas as pd
import torch,operator,sys,os,re,PIL,os,mimetypes,csv,itertools
from typing import Iterable,Iterator,Generator,Callable,Sequence,List,Tuple,Union,Optional
from torch import as_tensor,Tensor
from numpy import array,ndarray
from IPython.core.debugger import set_trace
from pathlib import Path
from collections import OrderedDict,defaultdict,Counter
from enum import Enum,IntEnum
from warnings import warn
from functools import partial,reduce

def test_fail(f, msg='', contains=''):
    "Fails with `msg` unless `f()` raises an exception and (optionally) has `contains` in `e.args`"
    try:
        f()
        assert False,f"Expected exception but none raised. {msg}"
    except Exception as e: assert not contains or contains in str(e)

def test(a, b, cmp,cname=None):
    "`assert` that `cmp(a,b)`; display inputs and `cname or cmp.__name__` if it fails"
    if cname is None: cname=cmp.__name__
    assert cmp(a,b),f"{cname}:\n{a}\n{b}"

def equals(a,b):
    "Compares `a` and `b` for equality; supports sublists, tensors and arrays too"
    cmp = (torch.equal    if isinstance(a, Tensor  ) else
           np.array_equal if isinstance(a, ndarray ) else
           operator.eq    if isinstance(a, str     ) else
           _all_equal     if isinstance(a, Iterable) else
           operator.eq)
    return cmp(a,b)

def _all_equal(a,b): return len(a)==len(b) and all(equals(a_,b_) for a_,b_ in zip(a,b))

def nequals(a,b):
    "Compares `a` and `b` for `not equals`"
    return not equals(a,b)

def test_eq(a,b):
    "`test` that `a==b`"
    test(a,b,equals, '==')

def test_ne(a,b):
    "`test` that `a!=b`"
    test(a,b,nequals,'!=')

def test_is(a,b):
    "`test` that `a is b`"
    test(a,b,operator.is_, 'is')