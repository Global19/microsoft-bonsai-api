"""
Tests for BonsaiClient class
Copyright 2020 Microsoft
"""
from unittest.mock import Mock, patch
from microsoft_bonsai_api.client import Config, BonsaiClient
from azure.core.exceptions import HttpResponseError


def test_default_client_construction():
    config = Config()
    BonsaiClient(config)


def test_400_err_registration():
    config = Config()
    config.server = "http://127.0.0.1:9000"
    config.workspace = "badrequest"
    config.access_key = "111"

    client = BonsaiClient(config)

    try:
        client.create_session("a", 1, "c")
    except HttpResponseError as err:
        assert err.status_code == 400


def test_401_err_registration():
    config = Config()
    config.server = "http://127.0.0.1:9000"
    config.workspace = "unauthorized"
    config.access_key = "111"

    client = BonsaiClient(config)

    try:
        client.create_session("a", 1, "c")
    except HttpResponseError as err:
        assert err.status_code == 401


def test_403_err_registration():
    config = Config()
    config.server = "http://127.0.0.1:9000"
    config.workspace = "forbidden"
    config.access_key = "111"

    client = BonsaiClient(config)

    try:
        client.create_session("a", 1, "c")
    except HttpResponseError as err:
        assert err.status_code == 403


def test_404_err_registration():
    config = Config()
    config.server = "http://127.0.0.1:9000"
    config.workspace = "notfound"
    config.access_key = "111"

    client = BonsaiClient(config)

    try:
        client.create_session("a", 1, "c")
    except HttpResponseError as err:
        assert err.status_code == 404


def test_502_err_registration():
    config = Config()
    config.server = "http://127.0.0.1:9000"
    config.workspace = "badgateway"
    config.access_key = "111"

    client = BonsaiClient(config)

    try:
        client.create_session("a", 1, "c")
    except HttpResponseError as err:
        assert err.status_code == 502


def test_503_err_registration():
    config = Config()
    config.server = "http://127.0.0.1:9000"
    config.workspace = "unavailable"
    config.access_key = "111"

    client = BonsaiClient(config)

    try:
        client.create_session("a", 1, "c")
    except HttpResponseError as err:
        assert err.status_code == 503


def test_504_err_timeout():
    config = Config()
    config.server = "http://127.0.0.1:9000"
    config.workspace = "gatewaytimeout"
    config.access_key = "111"

    client = BonsaiClient(config)

    try:
        client.create_session("a", 1, "c")
    except HttpResponseError as err:
        assert err.status_code == 504


def test_training():
    config = Config()
    config.server = "http://127.0.0.1:9000"
    config.workspace = "train"
    config.access_key = "111"

    client = BonsaiClient(config)
    client.create_session("a", 1, "c")

    counter = 0
    while counter < 100:
        client.advance("1", 1, {})
        counter += 1


@patch("time.sleep", return_value=None)
def test_flaky_sim(patched_sleep: Mock):
    config = Config()
    config.server = "http://127.0.0.1:9000"
    config.workspace = "flaky"
    config.access_key = "111"

    client = BonsaiClient(config)
    client.create_session("a", 1, "c")

    counter = 0
    while counter < 100:
        client.advance("1", 1, {})
        counter += 1
