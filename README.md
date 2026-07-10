# DevFlow

## アプリ概要

DevFlowは、Djangoで開発した開発作業支援ツールです。

開発中によく使うコードやコマンド、作業手順を一元管理し、作業効率を向上させることを目的としています。

## 主な機能

- Reference（コード・コマンド・ショートカット管理）
- Category管理
- Flow（作業フロー）
- 検索機能
- お気に入り機能
- コピー機能

## 開発環境

- Python 3.13.11
- Django 6.0.6
- SQLite3

## セットアップ

### 1. 仮想環境を作成

```bash
python -m venv .venv
```

### 2. 仮想環境を有効化

Windows

```bash
.venv\Scripts\activate
```

### 3. 必要なライブラリをインストール

```bash
pip install -r requirements.txt
```

### 4. サーバーを起動

```bash
python manage.py runserver
```

ブラウザで以下のURLにアクセスしてください。

```
http://127.0.0.1:8000/
```

## データベース

- データベースにはSQLite3を使用しています。
- `db.sqlite3`を提出物に含めています。
- 動作確認用のサンプルデータ（Reference・Flowなど）が登録されています。

## .env

`.env`ファイルは使用していません。
