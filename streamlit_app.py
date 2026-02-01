import streamlit as st
from supabase import create_client

# =====================
# Supabase 接続
# =====================
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("🥕 食材選択式レシピ提案アプリ")
st.write("使いたい食材を選択してください。**1つでも一致すればレシピを提案**します。")

# =====================
# レシピ取得
# =====================
response = supabase.table("recipes").select("*").execute()
recipes = response.data

# Supabaseの ingredients は list なので set に変換
for r in recipes:
    r["ingredients"] = set(r["ingredients"])

# =====================
# 食材一覧
# =====================
all_ingredients = sorted(
    set().union(*[r["ingredients"] for r in recipes])
)

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

    # 使える食材が多い順
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
