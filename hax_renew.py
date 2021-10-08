# Author: misakano2975

# 导入必需库
import os
import re
import json
import time
import base64
import requests
from bs4 import BeautifulSoup

# 设置UA
user_agent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/94.0.4606.61 Safari/537.36 "
)