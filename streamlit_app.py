import streamlit as st

st.title("🥕 食材選択式レシピ提案アプリ")
st.write("使いたい食材を選択してください。**1つでも一致すればレシピを提案**します。")

# =====================
# レシピデータベース
# =====================
recipes = [
    {
        "name": "ベーコンオムレツ",
        "ingredients": {"卵", "ベーコン"},
        "steps": "1. 卵を溶く\n2. ベーコンを炒める\n3. 卵を加えて焼く",
        "calorie": 350
    },
    {
        "name": "オニオンスープ",
        "ingredients": {"玉ねぎ", "コンソメ"},
        "steps": "1. 玉ねぎを薄切り\n2. 鍋で炒める\n3. 水とコンソメを加えて煮る",
        "calorie": 120
    },
    {
        "name": "卵チャーハン",
        "ingredients": {"卵", "ご飯", "ネギ"},
        "steps": "1. 卵を炒める\n2. ご飯とネギを加える\n3. 味付け",
        "calorie": 500
    },
    {
        "name": "野菜炒め",
        "ingredients": {"キャベツ", "人参", "ピーマン"},
        "steps": "1. 野菜を切る\n2. 炒める\n3. 味付け",
        "calorie": 180
    },
    {
        "name": "豚の生姜焼き",
        "ingredients": {"豚肉", "玉ねぎ", "生姜"},
        "steps": "1. 豚肉を焼く\n2. 玉ねぎを加える\n3. 生姜だれ",
        "calorie": 450
    },
    {
        "name": "ミートソースパスタ",
        "ingredients": {"パスタ", "ひき肉", "トマト"},
        "steps": "1. ひき肉を炒める\n2. トマトを加える\n3. パスタと合わせる",
        "calorie": 650
    },
    {
        "name": "チキンソテー",
        "ingredients": {"鶏肉", "にんにく"},
        "steps": "1. 鶏肉を焼く\n2. にんにくで香り付け",
        "calorie": 400
    },
    {
        "name": "ポテトサラダ",
        "ingredients": {"じゃがいも", "マヨネーズ", "卵"},
        "steps": "1. じゃがいもを茹でる\n2. 卵とマヨネーズで和える",
        "calorie": 300
    }
]

# =====================
# 食材一覧
# =====================
all_ingredients = sorted(set().union(*[r["ingredients"] for r in recipes]))

selected_ingredients = st.multiselect(
    "🥬 食材を選択",
    all_ingredients,
    placeholder="冷蔵庫にある食材を選んでください"
)

# =====================
# レシピ提案
# =====================
if not selected_ingredients:
    st.info("👆 まずは食材を選択してください")
else:
    user_ingredients = set(selected_ingredients)
    results = []

    for recipe in recipes:
        used = recipe["ingredients"] & user_ingredients
        if used:
            results.append({
                "recipe": recipe,
                "used": used,
                "missing": recipe["ingredients"] - user_ingredients
            })

    # 使える食材が多い順に並び替え
    results.sort(key=lambda x: len(x["used"]), reverse=True)

    st.subheader("🍳 提案メニュー")

    if not results:
        st.warning("選択した食材を使えるレシピがありません")
    else:
        for r in results:
            recipe = r["recipe"]
            with st.expander(f"🍽 {recipe['name']}（使える食材 {len(r['used'])}）"):
                st.write(f"🔥 **カロリー**: {recipe['calorie']} kcal")
                st.write(f"✅ 使える食材: {', '.join(r['used'])}")
                if r["missing"]:
                    st.write(f"❌ 足りない食材: {', '.join(r['missing'])}")
                st.text(recipe["steps"])
