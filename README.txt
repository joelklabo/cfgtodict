-- ConfigToDictionary
Convert a python config file of to a python dictionary

-- Example
Return the information in `info.cfg` as a `JSON` response from a `Flask` server:

info.cfg
----------
[info]
name = risk
version = 1
description = A simple game of chance. Risk 1000 Satoshis, win 2000, or lose them all.
project = https://github.com/joelklabo/risk

[risk]
price = 1000
description = 49/100 chance you will double your satoshis
```

server.py
----------
from flask import Flask
from flask.ext.responses import json_response
from cfgtodict import ConfigToDictionary

app = Flask(__name__)

@app.route('/info')
def info():
  about = ConfigToDictionary('info.cfg').dict() 
  return json_response(about)
```

JSON response
----------
{
  "info": {
    "description": "A simple game of chance. Risk 1000 Satoshis, win 2000, or lose them all.",
    "name": "risk",
    "project": "https://github.com/joelklabo/risk",
    "version": "1"
  },
  "risk": {
    "description": "49/100 chance you will double your satoshis",
    "price": "1000"
  }
}
```
