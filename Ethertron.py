from web3 import Web3, HTTPProvider
import asyncio
import json

web3 = Web3(HTTPProvider('https://mainnet.infura.io/v3/4d76e0a7dd3d4d8995f8d64311885612'))

print(web3.is_connected())

def handle_events(event):
    try:
        transaction = Web3.to_json(event).strip('"')
        transaction = web3.eth.get_transaction(transaction)
        print(transaction)
    except Exception as err:
        print(f"Error:{err}")
    
async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_events(event)
        await asyncio.sleep(poll_interval)

def main():
    tx_filter = web3.eth.filter("latest")
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
            log_loop(tx_filter, 2)
            )
        )
    finally:
        loop.close()

if __name__ == "__main__":
    main()





