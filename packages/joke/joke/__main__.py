from pystac_client import Client
import planetary_computer as pc
from odc.stac import stac_load
from math import floor
import pandas as pd
import geopandas as gpd
from sqlalchemy import create_engine
import psycopg2
import os

def main(args):
    name = args.get("name", "stranger")
    greeting = "Hello " + name + "!"
    print(greeting)
    return {"body": greeting}
