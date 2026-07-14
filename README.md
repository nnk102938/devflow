# DevFlow

## アプリ概要

DevFlowは、Djangoで開発した開発作業支援ツールです。

開発中によく使うコードやコマンド、作業手順を一元管理し、効率的に参照できるようにすることを目的としています。

---

## 主な機能

- Reference管理（コード・コマンド・ショートカット）
- Flow管理（作業手順）
- Category管理（管理画面）
- キーワード検索
- お気に入り登録
- ワンクリックコピー

---

## 開発環境

- Python 3.13.11
- Django 6.0.6
- SQLite3

---

## セットアップ

### 1. 仮想環境を作成

#### Windows

```bash
python -m venv .venv
```

#### macOS / Linux

```bash
python3 -m venv .venv
```

### 2. 仮想環境を有効化

#### Windows

```bash
.venv\Scripts\activate
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

### 3. 必要なライブラリをインストール

```bash
pip install -r requirements.txt
```

### 4. データベースを準備

提出物には、サンプルデータを含む `db.sqlite3` を同梱しています。

`db.sqlite3` が存在しない場合は、以下を実行してデータベースを作成してください。

```bash
python manage.py migrate
```

`db.sqlite3` を使用しない場合、初期状態ではデータベースは空です。

ReferenceやFlowを登録する前に、管理画面からCategoryを登録してください。

### 5. 開発サーバーを起動

#### Windows

```bash
python manage.py runserver
```

#### macOS / Linux

```bash
python3 manage.py runserver
```

---

## 起動方法

サーバー起動後、ブラウザで以下のURLへアクセスしてください。

```
http://127.0.0.1:8000/reference/
```

---

## .env

このアプリでは `.env` ファイルは使用していません。
