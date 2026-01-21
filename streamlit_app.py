import streamlit as st

st.title("🥕 食材からレシピを提案するアプリ")

st.write("使いたい食材をカンマ（,）で区切って入力してください。")

# 食材入力
ingredients_input = st.text_input("食材を入力", "例：卵, 玉ねぎ, ベーコン")

# 簡易レシピデータベース
recipes = [
    {
        "name": "ベーコンオムレツ",
        "ingredients": {"卵", "ベーコン"},
        "steps": "1. 卵を溶く\n2. ベーコンを炒める\n3. 卵を加えて焼く"
    },
    {
        "name": "オニオンスープ",
        "ingredients": {"玉ねぎ"},
        "steps": "1. 玉ねぎを薄切りにする\n2. 鍋で炒める\n3. 水とコンソメを加えて煮る"
    },
    {
        "name": "卵チャーハン",
        "ingredients": {"卵", "ご飯"},
        "steps": "1. フライパンで卵を炒める\n2. ご飯を加える\n3. 塩こしょうで味付け"
    }
]

if ingredients_input:
    user_ingredients = {i.strip() for i in ingredients_input.split(",")}

    st.subheader("🍳 提案されたレシピ")
    found = False

    for recipe in recipes:
        if recipe["ingredients"].issubset(user_ingredients):
            st.markdown(f"### {recipe['name']}")
            st.text(recipe["steps"])
            found = True

    if not found:
        st.write("該当するレシピが見つかりませんでした。")
        st.write("食材を追加してみてください。")
