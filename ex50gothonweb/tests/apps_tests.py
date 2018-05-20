#!/usr/bin/env python
# coding=utf-8
from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    # check that we get 404 on the / url
    resp = app.request('/')
    assert_response(resp, status='404')

    # test first get request to /hello
    resp = app.request('/hello')
    assert_response(resp)

    #test default valur work for form
    resp = app.request('/hello', method='POST')
    assert_response(resp, contain='nobody')

    #test input works
    data = {'name': 'Lyndon'}
    resp = app.request('/hello', method='POST', data=data)
    assert_response(resp, contain='Lyndon')
