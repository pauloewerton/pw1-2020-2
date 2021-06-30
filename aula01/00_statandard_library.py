# Usar console interativo

import sys
sys.platform
sys.version

import os
os.getcwd()
os.environ
os.getenv('HOME')

import datetime
datetime.date.today()
datetime.date.today().day
datetime.date.today().month
datetime.date.today().year

datetime.date.isoformat(datetime.date.today())

import time
time.strftime('%H:%M')

import html
html.escape("Este fragmento de HTML contém uma tag <script>script</script>.")
html.unescape("Eu &hearts; a &lt;biblioteca padrão&gt; do Python.")


