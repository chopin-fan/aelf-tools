#!/bin/bash

# Function to fetch and display block height and transaction pool status
fetch_and_display() {
    local network_name=$1
    local block_height_url=$2
    local transaction_pool_url=$3

    echo "=== $network_name ==="

    # Fetch and display block height
    echo -n "区块高度: "
    curl -s "$block_height_url" | python3 -c "import sys, json; print(json.dumps(json.load(sys.stdin), separators=(',', ': ')))"

    # Fetch and display transaction pool status
    echo -n " | 交易池情况: "
    curl -s "$transaction_pool_url" | python3 -c "import sys, json; print(json.dumps(json.load(sys.stdin), separators=(',', ': ')))"

    echo
}

# Testnets
fetch_and_display "测试网 - aelf-test-node" \
    "https://aelf-test-node.aelf.io/api/blockChain/blockHeight" \
    "https://aelf-test-node.aelf.io/api/blockChain/transactionPoolStatus"

fetch_and_display "测试网 - tdvw-test-node" \
    "https://tdvw-test-node.aelf.io/api/blockChain/blockHeight" \
    "https://tdvw-test-node.aelf.io/api/blockChain/transactionPoolStatus"

# Mainnets
fetch_and_display "主网 - aelf-public-node" \
    "https://aelf-public-node.aelf.io/api/blockChain/blockHeight" \
    "https://aelf-public-node.aelf.io/api/blockChain/transactionPoolStatus"

fetch_and_display "主网 - tdvv-public-node" \
    "https://tdvv-public-node.aelf.io/api/blockChain/blockHeight" \
    "https://tdvv-public-node.aelf.io/api/blockChain/transactionPoolStatus"