from flask import Flask, render_template
from flask_apscheduler import APScheduler
from datetime import datetime, timedelta
from apscheduler.triggers.interval import IntervalTrigger
import requests
import os
from dotenv import load_dotenv

load_dotenv('dt.env')

bt = os.getenv('bt')
cid = os.getenv('cid')

print(cid)