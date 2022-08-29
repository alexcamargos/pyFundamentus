#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: http_requester.py
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

STATUS_CODE = 200

RESPONSE_CONTEXT = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>requests-mock test page</title>
</head>
<body>
    <h1>requests-mock test page</h1>
    <p>This is a test page for requests-mock.</p>    
</body>
</html>
'''

REQUESTER_MOCK = {
    'status_code': STATUS_CODE,
    'content': RESPONSE_CONTEXT
}
