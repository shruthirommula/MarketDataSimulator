from app import initialize_app

app = initialize_app()
if __name__=='__main__':
    app.run(debug=True) 

# (Python with Kafka-Python):

    
from kafka import KafkaProducer
import json  

import random
import datetime
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

tickers = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

while True:
    data = {
        "ticker": random.choice(tickers),
        "bid_price": round(random.uniform(100, 1500), 2),
        "ask_price": round(random.uniform(100, 1500), 2),
        "last_trade_price": round(random.uniform(100, 1500), 2),
        "volume": random.randint(100, 10000),
        "timestamp": datetime.datetime.now().isoformat()
    }
    producer.send('equity_market_data', value=data)
    print(f"Sent: {data}")
    time.sleep(1)