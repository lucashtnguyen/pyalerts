import pytest

import pyalerts


def test_Mailto():
    result = pyalerts.alerts.Mailto({}, {}, None, 'aq')
    assert hasattr(result, 'data')
    assert hasattr(result, 'metadata')
    assert hasattr(result, 'mtype')