# sam-apikey1

AWS SAMで
APIにAPI keyをセットするサンプル。

Lamdaの中身は


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

あとは sam deplyごとに
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
