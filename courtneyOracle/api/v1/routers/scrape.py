import argparse
import argcomplete
from argcomplete.completers import ChoicesCompleter
from argcomplete.completers import EnvironCompleter
import requests
import datetime
#from bthread import BookingThread
from bs4 import BeautifulSoup
#from file_writer import FileWriter

from typing import List
from ninja import Router
import urllib, requests
import os,sys
from dotenv import load_dotenv, find_dotenv
from llama_index import download_loader
from courtneyOracle.api.v1.utils.utils import *
from courtneyOracle.api.v1.utils.Notion.injest import *
from courtneyOracle.api.v1.utils.Notion.qa import *
from django.http import JsonResponse

"""
Get current directory the unusual way
"""

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent) #append the parent directory from where the file is found.

router = Router()

@router.get("/bookingscrape")
def scrape_booking(request,url:str):
  response = "Hi Baby Girl"
  return {"Output":response}

"""
if __name__=="__main__":
  print ("Hi")
  parser = argparse.ArgumentParser()
  parser.add_argument("--url",help="The url to scrape")
  argcomplete.autocomplete(parser)
  args = parser.parse_args()
  scrape_booking(args.url)
"""