# learning-langchain

## 依存関係

- Python
- Poetry

バージョンは [.tool-verisons](.tool-versions) に書かれています。

> **Note**
> .tool-verisons は [asdf](https://asdf-vm.com/) の設定ファイルです。

## 実行手順

Python のパッケージは Poetry で管理しています。
以下のコマンドでインストールしてください。

```console
poetry install
```

各サンプルコードは以下のコマンドで実行できます。

```console
poetry run python learning_langchain/<ファイル名>
```

### 4.indexes.py を実行する場合

4.indexes.py は、langchain のドキュメントを読み込んで使う例となっています。

以下のコマンドで langchain のドキュメントを準備してから実行してください。

```console
git submodule update --init
cd langchain
poetry install
make docs_build
```
