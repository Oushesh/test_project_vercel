from ninja import Schema
from typing import List

class TwitterDataIN(Schema):
    profile: str
    confidence: optional
