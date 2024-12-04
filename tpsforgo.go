package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"
)

func getTransactionResult(txid string) (map[string]interface{}, error) {
	url := fmt.Sprintf("http://localhost:8000/api/blockChain/transactionResult?transactionId=%s", txid)
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	var result map[string]interface{}
	decoder := json.NewDecoder(resp.Body)
	if err := decoder.Decode(&result); err != nil {
		return nil, err
	}

	return result, nil
}

func getBlockByHeight(blockHeight int) (map[string]interface{}, error) {
	url := fmt.Sprintf("http://localhost:8000/api/blockChain/blockByHeight?blockHeight=%d&includeTransactions=false", blockHeight)
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	var result map[string]interface{}
	decoder := json.NewDecoder(resp.Body)
	if err := decoder.Decode(&result); err != nil {
		return nil, err
	}

	header := result["Header"].(map[string]interface{})
	body := result["Body"].(map[string]interface{})
	fmt.Printf("区块时间:%s, 区块高度:%d， 对应的交易数量:%v\n", header["Time"], blockHeight, body["TransactionsCount"])
	return result, nil
}

func main() {
	startTxid := "145326c13bc7bc348042971e6db880d8103a56a39bc4f794afdf95e56148d054"
	endTxid := "362ffe9e3ec08d996541b6aef3415f8d203fcc87d8d521a09159e25c465e5a91"

	startResult, err := getTransactionResult(startTxid)
	if err != nil {
		log.Fatalf("Error getting start transaction result: %v", err)
	}
	startBlockHeight := int(startResult["BlockNumber"].(float64))

	endResult, err := getTransactionResult(endTxid)
	if err != nil {
		log.Fatalf("Error getting end transaction result: %v", err)
	}
	endBlockHeight := int(endResult["BlockNumber"].(float64))

	fmt.Printf("开始区块块高：%d\n", startBlockHeight)
	fmt.Printf("结束区块块高：%d\n", endBlockHeight)

	totalTransactionCount := 0
	for i := startBlockHeight; i <= endBlockHeight; i++ {
		block, err := getBlockByHeight(i)
		if err != nil {
			log.Fatalf("Error getting block by height: %v", err)
		}
		body := block["Body"].(map[string]interface{})
		totalTransactionCount += int(body["TransactionsCount"].(float64))
	}

	fmt.Printf("打包交易数：%d\n", totalTransactionCount)

	startBlock, _ := getBlockByHeight(startBlockHeight)
	endBlock, _ := getBlockByHeight(endBlockHeight)

	startTime, _ := time.Parse(time.RFC3339, startBlock["Header"].(map[string]interface{})["Time"].(string))
	endTime, _ := time.Parse(time.RFC3339, endBlock["Header"].(map[string]interface{})["Time"].(string))

	fmt.Printf("开始时间为：%v\n", startTime)
	fmt.Printf("结束时间为：%v\n", endTime)

	timeDifference := endTime.Sub(startTime)
	secondsDifference := timeDifference.Seconds()
	fmt.Printf("时间差为: %.0f 秒\n", secondsDifference)

	tps := float64(totalTransactionCount) / secondsDifference
	fmt.Printf("TPS为：%.2f\n", tps)

	averageTransactionsPerBlock := float64(totalTransactionCount) / float64(endBlockHeight-startBlockHeight+1)
	fmt.Printf("打包区块数量: %d\n", endBlockHeight-startBlockHeight+1)
	fmt.Printf("平均每个区块的交易数量: %.2f\n", averageTransactionsPerBlock)
}
