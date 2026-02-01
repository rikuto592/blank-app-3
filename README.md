食材選択式レシピ提案アプリ（Streamlit × Supabase）

アプリのURL

https://blank-app-js0shr4lyl.streamlit.app/

📌 概要

このアプリは、冷蔵庫にある食材を選ぶだけで作れるレシピを提案してくれるWebアプリです。
Streamlit を使って画面を作成し、レシピデータは Supabase のデータベースから取得しています。

選択した食材が 1つでも一致していればレシピを表示し、
「使える食材」「足りない食材」を分かりやすく表示するのが特徴です。

🎯 主な機能

Supabase に保存されたレシピデータを取得

食材を複数選択できるマルチセレクト機能

選択した食材と一致するレシピを自動提案

使える食材の数が多い順にレシピを並び替え

各レシピの

カロリー

使える食材

足りない食材

作り方
を表示

🛠 使用技術

Python

Streamlit（Webアプリ作成）

Supabase（データベース）

PostgreSQL（Supabase 内部DB）

🗂 Supabase テーブル構成（例）
recipes テーブル
カラム名	型	説明
id	int	レシピID
name	text	レシピ名
ingredients	text[]	使用食材（配列）
steps	text	作り方
calorie	int	カロリー



🚀 起動方法
streamlit run app.py

💡 工夫した点

Supabase から取得した ingredients を set型に変換し、
食材の一致判定を高速かつ簡潔に実装した点

使える食材の数でソートすることで、
「今すぐ作れそうなレシピ」が上に来るようにした点

st.expander を使い、画面が見やすくなるよう工夫した点

😵 大変だった点

Supabase の 配列型（list）と Python の set の違いを理解するところ

secrets の設定を忘れるとエラーが出る点

データが空のときの例外処理

📈 今後の改善案

お気に入り機能の追加

調理時間や難易度での絞り込み

レシピ投稿機能の追加

利用履歴の保存
