import datetime
import json
import os
import random
import sys
import time
from dataclasses import dataclass

import confluent_kafka

tickers = ['AAPL', 'GOOG', 'META', 'NFLX', 'AMZN', 'INTC', 'CSCO', 'BABA', 'NVDA']

prices = {}

@dataclass
class Config:
    kafka_server: dict
    kafka_topic: str
    events_per_second: int

def load_config() -> Config:
    kafka_addr = os.environ.get("KAFKA_BOOTSTRAP_SERVERS") or "localhost:19092"
    kafka_topic = os.environ.get("TOPIC") or "sql_basics.trades"
    kafka_security_protocol = os.environ.get("KAFKA_SECURITY_PROTOCOL")
    kafka_sasl_mechanism = os.environ.get("KAFKA_SASL_MECHANISM")
    kafka_username = os.environ.get("KAFKA_USERNAME")
    kafka_password = os.environ.get("KAFKA_PASSWORD")
    eps = int(os.environ.get("EVENTS_PER_SECOND") or "1")
    kafka_config = {
        "bootstrap.servers": kafka_addr,
        "linger.ms": 0,
    }
    if kafka_security_protocol:
        kafka_config["security.protocol"] = kafka_security_protocol
    if kafka_sasl_mechanism:
        kafka_config["sasl.mechanism"] = kafka_sasl_mechanism
    if kafka_username:
        kafka_config["sasl.username"] = kafka_username
    if kafka_password:
        kafka_config["sasl.password"] = kafka_password
    return Config(
        kafka_server=kafka_config,
        kafka_topic=kafka_topic,
        events_per_second=eps,
    )

# updates the next price
def update_price(curr_price, symbol):
    step = random.choice([+2.0, -2.0])
    prices[symbol] = round(curr_price + step, 2)
    if prices[symbol] <= 0:
        prices[symbol] = round(curr_price + 1.0, 2)
    elif prices[symbol] >= 999.0:
        prices[symbol] = round(curr_price - 1.0, 2)

# returns id, ticker, price, trade_ts, amt
def fake_trade(tid):
    symbol = random.choice(tickers)
    price = prices[symbol]
    result = {}
    result['id'] = tid
    result['ticker'] = symbol
    result['price'] = price
    result['trade_ts'] = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
    #result['trade_ts'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result['amt'] = random.randint(1, 99)
    update_price(price, symbol)
    return result

def main():
    print("loading config")
    cfg = load_config()
    print ("Using cfg {}", cfg)
    producer = confluent_kafka.Producer(cfg.kafka_server)
    print("Created Producer")

    # contains the next price that will be used for each symbol
    for ticker in tickers:
        prices[ticker] = round(random.uniform(1.0, 999.0), 2)

    sleep_time = float(os.environ.get("SLEEP_TIME") or 1)

    next_trade_id = 1
    while True:
        trade = json.dumps(fake_trade(next_trade_id)).encode('utf-8')
        next_trade_id += 1
        producer.produce(cfg.kafka_topic, trade)
        print(f'TRADE {trade}')
        producer.flush()
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()
