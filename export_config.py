#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
毎回stackにアクセスするのが面倒なので
必要な情報を.config.jsonとして書き出す。
また
`sam local invoke HelloWorldFunction -n env.json`
で使う env.json も書き出す

config.sh追加。環境変数版
"""

import json

# import pprint

import boto3
import toml

# PP = pprint.PrettyPrinter(indent=2).pprint


def read_samconfig(profile: str = "default") -> dict:
    """Read parameters from './samconfig.toml' ."""
    sam = toml.load(open("./samconfig.toml"))
    return sam[profile]["deploy"]["parameters"]


def main():
    """main"""
    # samconfig.tomlを読む
    sam = read_samconfig()

    # stackからoutputを得てdictにする
    CFn = boto3.client("cloudformation", region_name=sam["region"])
    res = CFn.describe_stacks(StackName=sam["stack_name"])
    output = {k["OutputKey"]: k["OutputValue"] for k in res["Stacks"][0]["Outputs"]}

    # API Key IDからapi keyを得る
    # AWSCLIだと
    # aws apigateway get-api-key --api-key {ApiKeyID} --include-value
    AGW = boto3.client("apigateway", region_name=sam["region"])
    apikey = AGW.get_api_key(apiKey=output["ApiKeyID"], includeValue=True)

    # tmp_config.shを作成(TODO:もうすこしなんとかする)
    with open("tmp_config.sh", "w") as f:
        f.write(
            f"""
StackName={sam["stack_name"]}
AWS_REGION={sam["region"]}
ApiKeyID={output["ApiKeyID"]}
ApiKey={apikey["value"]}
HelloWorldApi={output["HelloWorldApi"]}
"""
        )


if __name__ == "__main__":
    main()
