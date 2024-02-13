# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : tests.py
#
#* Purpose :
#
#* Creation Date : 10-12-2022
#
#* Last Modified : Saturday 10 December 2022 11:04:52 PM
#
#* Created By : Yaay Nands
#_._._._._._._._._._._._._._._._._._._._._.#
import requests
import json
data = {'subject':'test', 'inputs': [['a'],['k'],['.p,'],['euo']]}
resp = requests.post('http://127.0.0.1:8000/ikigai/',
                        headers={'Content-Type': 'application/json'},
                        data=json.dumps(data))
print(resp.status_code)
print(resp.json())
