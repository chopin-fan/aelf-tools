#!/usr/bin/python3 

from datetime import datetime
from dateutil import parser
import requests


def get_transaction_result(txid):
    headers = {
        'accept': 'text/plain; v=1.0',
    }
    params = {
        'transactionId': txid
    }
    response = requests.get('http://localhost:8000/api/blockChain/transactionResult', params=params, headers=headers)
    return response.json()


def get_block_by_height(block_height):
    headers = {
        'accept': 'text/plain; v=1.0',
    }
    params = {
        'blockHeight': block_height,
        'includeTransactions': 'false',
    }
    response = requests.get('http://localhost:8000/api/blockChain/blockByHeight', params=params, headers=headers)
    print(f"区块时间:{response.json()['Header']['Time']},区块高度:{block_height}，对应的交易数量:{response.json()['Body']['TransactionsCount']}")
    return response.json()


if __name__ == '__main__':
    start_txid = "145326c13bc7bc348042971e6db880d8103a56a39bc4f794afdf95e56148d054"
    end_txid = "362ffe9e3ec08d996541b6aef3415f8d203fcc87d8d521a09159e25c465e5a91"
    start_block_height = get_transaction_result(start_txid)['BlockNumber']

    end_block_height = get_transaction_result(end_txid)['BlockNumber']
    print(f"开始区块块高：{start_block_height}")
    print(f"结束区块块高：{end_block_height}")

    count_list = []
    total_transaction_count = 0
    for i in range(start_block_height, end_block_height + 1):
        count_list.append(get_block_by_height(i)['Body']['TransactionsCount'])

    for j in count_list:
        total_transaction_count += j


    print(f"打包交易数：{total_transaction_count}")

    start_time_str = get_block_by_height(start_block_height)['Header']['Time']
    end_time_str = get_block_by_height(end_block_height)['Header']['Time']

    start_time = parser.parse(start_time_str)
    end_time = parser.parse(end_time_str)
    print(f"开始时间为：{start_time}")
    print(f"结束时间为：{end_time}")

    time_difference = end_time - start_time
    seconds_difference = time_difference.total_seconds()
    print(f"时间差为: {seconds_difference} 秒")

    tps = round(total_transaction_count / seconds_difference, 2)
    print(f"TPS为：{tps}")

    average_transactions_per_block = total_transaction_count / (end_block_height - start_block_height + 1)
    print(f"打包区块数量: {(end_block_height - start_block_height + 1)}")
    print(f"平均每个区块的交易数量: {average_transactions_per_block:.2f}")
