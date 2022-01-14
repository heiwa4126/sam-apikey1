# sam-apikey1

AWS SAMで
APIにAPI keyをセットするサンプル。

Lamdaの中身はPythonのサンプルのhello worldです。


# デプロイ

```sh
sam build
sam deploy --guided  # --guidedは最初の1回
```

`sam deploy --guided` は

```
HelloWorldFunction may not have authorization defined, Is this okay? [y/N]: y
```

以外はデフォルトでいいです。


# テスト

## 設定の抜き出し

最初に1回
```sh
pip3 install -U -r requirements.txt
```

すること(`--user`つけるとか適宜アレンジ)

あとは sam deployごとに
```sh
./export_config.py
```

を実行して、`tmp_config.sh` を生成してください。

## テストの実行

```sh
./run_test.sh
```


# スタックの削除

```sh
sam delete
```
で消えます。


# 参考

* [AWS Serverless API with API Key - Script Tips by Payton Chertude](https://scripttips.net/aws-serverless-api-with-api-key/)
* [AWS SAMでAPIキーと使用量プランのリソース作成に失敗する場合の対処方法 - Qiita](https://qiita.com/hayao_k/items/4bee4a27a2b15f19fad8)


# メモ

SAMが生成するCFnのAWS::ApiGateway::Stageの名前をDependsOnに指定するのがコツ
