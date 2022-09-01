#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: random_user_agent_test.py
#  Version: 0.0.1
#
#  Summary: Python Fundamentus
#           Python Fundamentus is a Python API that allows you to quickly
#           access the main fundamental indicators of the main stocks
#           in the Brazilian market.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
# ------------------------------------------------------------------------------

"""Random User Agent Test."""

from .random_user_agent import ALL_USER_AGENTS, get_random_user_agent


def test_get_random_user_agent() -> None:
    """Test get random user agent."""

    user_agent = get_random_user_agent()

    assert isinstance(user_agent, str)
    assert user_agent in ALL_USER_AGENTS
