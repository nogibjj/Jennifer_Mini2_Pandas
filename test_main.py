"""
Test goes here

"""

from main import stats_overview, gender_chart
import numpy as np
import pandas as pd


def test_stats_overview():
    overview = stats_overview()
    assert overview is not None


def test_gender_chart():
    chart = gender_chart()
    assert chart is not None
