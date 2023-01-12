from pydantic import BaseModel
from typing import List
from cloudclient.datamodel import GridConnection, GridNode, Actor
from cloudclient.datamodel.policies import Policy
import json


class Payload(BaseModel):
    gridconnections: List[GridConnection]
    gridnodes: List[GridNode]
    actors: List[Actor]
    policies: List[Policy]
    etm_upscale_sliders: dict
    etm_upscale_curve_labels: dict

    def to_json(self):
        return {
            "gridconnections": [
                json.loads(grid_connection.json())
                for grid_connection in self.gridconnections
            ],
            "gridnodes": [json.loads(grid_node.json()) for grid_node in self.gridnodes],
            "actors": [json.loads(actor.json()) for actor in self.actors],
            "policies": [json.loads(parameter.json()) for parameter in self.policies],
        }
