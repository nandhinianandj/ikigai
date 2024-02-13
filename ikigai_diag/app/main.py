# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name :
#
#* Purpose :
#
#* Creation Date : 05-12-2022
#
#* Last Modified : Saturday 10 December 2022 10:55:31 PM
#
#* Created By : Yaay Nands
#_._._._._._._._._._._._._._._._._._._._._.#

from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

from ikigai_diagram import draw_ikigai
app = FastAPI()

class IkigaiRequest(BaseModel):
    subject: str
    inputs: list[str]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/ikigai/")
def read_item(request: IkigaiRequest):

    import pdb; pdb.set_trace()
    #assert len(request['inputs']) == 4
    #assert all(map(isinstance(obj, list) for obj in request['inputs']))
    draw_ikigai(request['subject'], request['inputs'])
    return {"inputs": request['inputs']}

