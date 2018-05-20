#!/usr/bin/env python
# coding=utf-8
from nose.tools import *
import re

def assert_response(resp, contain=None, headers=None, matches=None, status="200"):
    assert status in resp.status, "Expected response %r not in %r" % (status, resp.status)
    if status == "200":
        assert resp.data, "Response data is empty."

    if contain:
        assert contain in resp.data, "Response does not contain %r " % contain

    if matches:
        reg = re.compile(matches)
        assert reg.matches(resp.data), "Response does not match %r" % matches

    if headers:
        assert_equal(resp.headers, headers)
