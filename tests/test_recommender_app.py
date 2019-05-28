#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `recommender_app` package."""


import pytest
from recommender_app import recommender_awesome


def test_recommender():
    assert recommender_awesome.get_recommendation() == 'Shrek'
