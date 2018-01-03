<h1>Whale Hunter 1.0.0</h1>

Automated trading of pump and dumps.

1. navigate to folder and install requirements: 

pip install -r requirements.txt

Running:

- Insert keys into user.py
- Choose a strategy in user.py


Notes:

- When making changes, update version log with new version, and update new features added. Place old version of program folder labeled with version number into the folder: versions
- Make sure to only call API once per data gathering turn.
- All the data should be coming from the feed database, feed.db, which is running concurrently
- feed.py concurrency is initiated by main.py


To do:


Short term

- get to paper trading MVP
- get feed.db, and feed.py up and running
- detect sudden spikes in whale activity
- detect a drop off in price activity


Long term

- get to live trading MVP 
- create bokeh graph to picture equity over time
- create front end user interface in javascript and flask
- get paper trading to work consistently enough to test with real capital



feed.py

- main.py runs the feed.py file with a multi-process
- feed.py writes to one file per coin and broker. ex. binance_wabi.py















