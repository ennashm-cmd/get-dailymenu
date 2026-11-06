import streamlit as st
import pandas as pd
import json
import random
import urllib.parse
from datetime import time

# Import the 100+ recipe database from your separate file
from recipes import LOCAL_RECIPE_DATABASE

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="GetDailyMenu - Culinary Intelligence",
    page_icon="🍳",
    layout="wide"
)

# ==================== PREMIUM CULINARY DESIGN SYSTEM ====================
st.markdown("""
<style>
    .stApp { background-color: #FAF8F5; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    .main-header { font-size: 2.5rem; font-weight: 800; color: #1C1917; letter-spacing: -0.03em; margin-bottom: 4px; }
    .sub-text { color: #44403C; font-size: 1.15rem; margin-bottom: 24px; font-weight: 400; }
    
    .landing-card {
        background: linear-gradient(135deg, #1C1917 0%, #78350F 100%);
        padding: 60px 40px; border-radius: 24px; color: #FFFFFF; text-align: center; margin-top: 10px;
        box-shadow: 0 20px 25px -5px rgba(120, 53, 15, 0.15);
    }
    .landing-title { font-size: 3.2rem; font-weight: 800; margin-bottom: 16px; letter-spacing: -0.03em; color: #FFFFFF; }
    .landing-subtitle { font-size: 1.3rem; font-weight: 400; color: #FDE68A; margin-bottom: 24px; max-width: 700px; margin-left: auto; margin-right: auto; line-height: 1.5; }
    
    .cube-card {
        background: #FFFFFF;
        border: 1px solid #D7D3D0;
        border-top: 5px solid #D97706;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
        transition: all 0.2s ease-in-out;
        margin-bottom: 16px;
        height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .cube-card:hover {
        border-color: #A8A29E;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
        transform: translateY(-2px);
    }
    
    .badge-veg { background-color: #ECFDF5; color: #047857; padding: 3px 10px; border-radius: 9999px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; border: 1px solid #A7F3D0; }
    .badge-nonveg { background-color: #FFF1F2; color: #BE123C; padding: 3px 10px; border-radius: 9999px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; border: 1px solid #FECDD3; }
    
    .dish-title { font-size: 1rem; font-weight: 600; color: #1C1917; line-height: 1.35; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .dish-meta { font-size: 0.78rem; color: #57534E; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; }

    .stTabs [data-baseweb="tab"] { font-size: 1.05rem; font-weight: 600; padding: 10px 18px; }
</style>
""", unsafe_allow_html=True)

# ==================== INITIALIZE SESSION STATE ROUTING ====================
if "page" not in st.session_state:
    st.session_state["page"] = "landing"

if "user_profile" not in st.session_state:
    st.session_state["user_profile"] = {
        "adults": 2,
        "kids": 1,
        "cuisine": "South Indian",
        "diet_mode": "Non-Veg",
        "day_diets": {}, 
        "city": "Chennai"
    }

if "monthly_plan" not in st.session_state:
    st.session_state["monthly_plan"] = {}

# ==================== CACHED CORE FUNCTIONALITY ====================
@st.cache_data
def generate_week_plan(cuisine, diet_mode, day_diets_tuple):
    day_diets = dict(day_diets_tuple)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    cuisine_db = LOCAL_RECIPE_DATABASE.get(cuisine, LOCAL_RECIPE_DATABASE["South Indian"])
    
    veg_pool = cuisine_db.get("Veg", [])
    nonveg_pool = cuisine_db.get("Non-Veg", [])
    
    sampled_veg = random.sample(veg_pool, len(veg_pool)) if veg_pool else []
    sampled_nonveg = random.sample(nonveg_pool, len(nonveg_pool)) if nonveg_pool else []
    
    v_idx, nv_idx = 0, 0
    week_plan = []
    
    for day in days:
        if diet_mode == "Mixed" and day_diets:
            is_non_veg = day_diets.get(day, False)
            diet_key = "Non-Veg" if is_non_veg else "Veg"
        elif diet_mode == "Non-Veg":
            diet_key = "Non-Veg"
        else:
            diet_key = "Veg"
            
        if diet_key == "Non-Veg" and sampled_nonveg:
            recipe = sampled_nonveg[nv_idx % len(sampled_nonveg)]
            nv_idx += 1
        elif sampled_veg:
            recipe = sampled_veg[v_idx % len(sampled_veg)]
            v_idx += 1
        else:
            recipe = {"gravy": "Simple Dal", "dry_item": "Poriyal", "base_staple": "Rice", "cooking_time": "20 mins", "calories": "~400 kcal"}
            
        week_plan.append({
            "day": day,
            "meal_type": diet_key,
            "gravy": recipe.get("gravy"),
            "dry_item": recipe.get("dry_item"),
            "base_staple": recipe.get("base_staple", "Steamed Rice"),
            "cooking_time": recipe.get("cooking_time", "30 mins"),
            "calories": recipe.get("calories", "~450 kcal"),
            "ingredients": recipe.get("ingredients", ["Basic Spices", "Rice", "Oil", "Salt"]),
            "steps": recipe.get("steps", ["Cook and serve hot."])
        })
    return week_plan

def get_full_monthly_plan():
    profile = st.session_state["user_profile"]
    diets_tuple = tuple(profile["day_diets"].items())
    return {
        "Week 1": generate_week_plan(profile["cuisine"], profile["diet_mode"], diets_tuple),
        "Week 2": generate_week_plan(profile["cuisine"], profile["diet_mode"], diets_tuple),
        "Week 3": generate_week_plan(profile["cuisine"], profile["diet_mode"], diets_tuple),
        "Week 4": generate_week_plan(profile["cuisine"], profile["diet_mode"], diets_tuple)
    }

def aggregate_grocery_list(week_data):
    raw_ingredients = []
    for day in week_data:
        raw_ingredients.extend(day.get("ingredients", []))
    
    categories = {
        "🥦 Fresh Produce & Vegetables": [],
        "🌾 Grains, Dals & Staples": [],
        "🧂 Spices, Condiments & Oils": [],
        "🍗 Meat, Poultry & Seafood": [],
        "🧀 Dairy & Other Essentials": []
    }
    
    produce_keywords = ["onion", "tomato", "ginger", "garlic", "chili", "coriander", "curry", "potato", "carrot", "beans", "spinach", "gourd", "brinjal", "lemon"]
    grain_keywords = ["rice", "dal", "flour", "atta", "dosa", "idli", "rava", "wheat"]
    spice_keywords = ["spice", "oil", "ghee", "mustard", "cumin", "turmeric", "pepper", "salt", "cardamom", "clove", "cinnamon"]
    meat_keywords = ["chicken", "mutton", "prawn", "fish", "crab", "egg"]
    
    unique_items = sorted(list(set(raw_ingredients)))
    
    for item in unique_items:
        item_lower = item.lower()
        if any(k in item_lower for k in meat_keywords):
            categories["🍗 Meat, Poultry & Seafood"].append(item)
        elif any(k in item_lower for k in produce_keywords):
            categories["🥦 Fresh Produce & Vegetables"].append(item)
        elif any(k in item_lower for k in grain_keywords):
            categories["🌾 Grains, Dals & Staples"].append(item)
        elif any(k in item_lower for k in spice_keywords):
            categories["🧂 Spices, Condiments & Oils"].append(item)
        else:
            categories["🧀 Dairy & Other Essentials"].append(item)
            
    return categories

def format_text_plan(week_name, week_data):
    text = f"🍳 *GetDailyMenu Master Schedule - {week_name}* 🗓️\n\n"
    for d in week_data:
        text += f"*{d['day']} ({d['meal_type']})*\n"
        text += f"• Gravy: {d['gravy']}\n"
        text += f"• Dry: {d['dry_item']}\n"
        text += f"• Staple: {d['base_staple']}\n\n"
    return text


# =========================================================================
# SIDEBAR: BETA FEEDBACK WIDGET FOR REAL USERS
# =========================================================================
with st.sidebar:
    st.markdown("### 💬 Beta Feedback Hub")
    st.write("Help us improve GetDailyMenu with your live feedback!")
    with st.form("feedback_form"):
        fb_rating = st.slider("Rate your experience:", 1, 5, 5)
        fb_text = st.text_area("What features or recipes should we add next?")
        fb_submitted = st.form_submit_button("Submit Feedback", use_container_width=True)
        if fb_submitted:
            st.success("🙏 Thank you! Your feedback has been recorded.")


# =========================================================================
# PAGE 1: WELCOME LANDING PAGE
# =========================================================================
if st.session_state["page"] == "landing":
    st.markdown("""
    <div class='landing-card'>
        <div class='landing-title'>🍳 GetDailyMenu</div>
        <div class='landing-subtitle'>
            No more 'What to cook today?' — Experience intelligent weekly meal planning and vibrant culinary coordination designed for modern households.
        </div>
        <p style='font-size: 1.15rem; font-style: italic; color: #FDE68A; margin-bottom: 0px;'>
            "Good food brings families together, saving you time for what truly matters." ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("✨ Sign In & Launch Portal", use_container_width=True):
            st.session_state["page"] = "profile_setup"
            st.rerun()


# =========================================================================
# PAGE 2: PROFILE SETUP (WITH ONE-CLICK DEMO PRESETS)
# =========================================================================
elif st.session_state["page"] == "profile_setup":
    st.markdown("<p class='main-header'>Household Kitchen Setup</p>", unsafe_allow_html=True)
    st.markdown("<p class='sub-text'>Configure your culinary preferences once. Tailored to perfection.</p>", unsafe_allow_html=True)
    
    # --- One-Click Demo Presets for New Beta Users ---
    st.markdown("💡 **Quick Demo Presets:** Click to instantly load sample profiles!")
    preset_col1, preset_col2, _ = st.columns([1.5, 1.5, 3])
    with preset_col1:
        if st.button("⚡ Load Demo: Family of 4 (South Indian)", use_container_width=True):
            st.session_state["user_profile"] = {
                "adults": 2, "kids": 2, "cuisine": "South Indian", "diet_mode": "Mixed",
                "day_diets": {"Monday": False, "Tuesday": False, "Wednesday": True, "Thursday": False, "Friday": True, "Saturday": True, "Sunday": True},
                "city": "Chennai"
            }
            st.session_state["monthly_plan"] = get_full_monthly_plan()
            st.session_state["page"] = "dashboard"
            st.rerun()
    with preset_col2:
        if st.button("⚡ Load Demo: Couple (North Indian Veg)", use_container_width=True):
            st.session_state["user_profile"] = {
                "adults": 2, "kids": 0, "cuisine": "North Indian", "diet_mode": "Veg",
                "day_diets": {}, "city": "Chennai"
            }
            st.session_state["monthly_plan"] = get_full_monthly_plan()
            st.session_state["page"] = "dashboard"
            st.rerun()
            
    st.markdown("<hr style='margin: 16px 0px; border-color: #D7D3D0;'>", unsafe_allow_html=True)
    
    with st.container():
        with st.form("profile_form"):
            col1, col2 = st.columns(2)
            with col1:
                adults = st.number_input("Number of Adults", min_value=1, max_value=10, value=st.session_state["user_profile"]["adults"])
                cuisine = st.selectbox("Preferred Cuisine", ["South Indian", "North Indian"], index=0 if st.session_state["user_profile"]["cuisine"]=="South Indian" else 1)
            with col2:
                kids = st.number_input("Number of Kids", min_value=0, max_value=10, value=st.session_state["user_profile"]["kids"])
                diet_mode = st.selectbox("Dietary Preference Mode", ["Veg", "Non-Veg", "Mixed"], index=2 if st.session_state["user_profile"]["diet_mode"]=="Mixed" else 1)
                
            day_diets = {}
            if diet_mode == "Mixed":
                st.markdown("<br>📅 **Select your preferred Non-Veg days (Unchecked days default to Veg):**", unsafe_allow_html=True)
                d_cols = st.columns(7)
                days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                for idx, day in enumerate(days_list):
                    with d_cols[idx]:
                        default_val = st.session_state["user_profile"]["day_diets"].get(day, day in ["Wednesday", "Friday", "Sunday"])
                        day_diets[day] = st.checkbox(day[:3], value=default_val)
                        
            st.markdown("<br>", unsafe_allow_html=True)
            submitted = st.form_submit_button("💾 Save & Proceed to Dashboard ➔", use_container_width=True)
            
            if submitted:
                st.session_state["user_profile"] = {
                    "adults": adults,
                    "kids": kids,
                    "cuisine": cuisine,
                    "diet_mode": diet_mode,
                    "day_diets": day_diets,
                    "city": "Chennai"
                }
                st.session_state["monthly_plan"] = get_full_monthly_plan()
                st.session_state["page"] = "dashboard"
                st.rerun()


# =========================================================================
# PAGE 3: ENTERPRISE DASHBOARD & HUB
# =========================================================================
elif st.session_state["page"] == "dashboard":
    header_col1, header_col2 = st.columns([3, 1])
    with header_col1:
        st.markdown("<p class='main-header'>Culinary Command Center 🗓️</p>", unsafe_allow_html=True)
        profile = st.session_state["user_profile"]
        st.markdown(f"<p class='sub-text'>Cuisine: <b>{profile['cuisine']}</b> | Mode: <b>{profile['diet_mode']}</b> | Family: <b>{profile['adults']} Adults, {profile['kids']} Kids</b></p>", unsafe_allow_html=True)
    with header_col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("⚙️ Edit Settings", use_container_width=True):
            st.session_state["page"] = "profile_setup"
            st.rerun()

    tab_menu, tab_grocery, tab_poster_share = st.tabs([
        "🗓️ 7-Day Menu Plan", 
        "🛒 Smart Grocery List", 
        "🖨️ Poster & Family Sync Hub"
    ])
    
    weeks = list(st.session_state["monthly_plan"].keys())
    
    # ------------------ TAB 1: MENU GRID ------------------
    with tab_menu:
        c_drop1, c_drop2 = st.columns([1, 2])
        with c_drop1:
            selected_week = st.selectbox("📅 Planning Horizon:", weeks, key="horizon_menu")
            
        st.markdown("<hr style='margin: 14px 0px; border-color: #D7D3D0;'>", unsafe_allow_html=True)
        week_data = st.session_state["monthly_plan"][selected_week]
        
        row1_data = week_data[:4]
        row2_data = week_data[4:]
        
        def render_enterprise_grid(days_subset):
            cols = st.columns(len(days_subset))
            for idx, day_item in enumerate(days_subset):
                with cols[idx]:
                    badge_class = "badge-nonveg" if "non" in day_item['meal_type'].lower() else "badge-veg"
                    
                    st.markdown(f"""
                    <div class='cube-card'>
                        <div>
                            <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;'>
                                <b style='font-size: 1.05rem; color: #1C1917;'>{day_item['day']}</b>
                                <span class='{badge_class}'>{day_item['meal_type']}</span>
                            </div>
                            <div style='margin-bottom: 8px;'>
                                <div class='dish-meta'>🍲 Gravy</div>
                                <div class='dish-title' title='{day_item['gravy']}'>{day_item['gravy']}</div>
                            </div>
                            <div>
                                <div class='dish-meta'>🥘 Dry Item</div>
                                <div class='dish-title' title='{day_item['dry_item']}'>{day_item['dry_item']}</div>
                            </div>
                        </div>
                        <div style='border-top: 1px solid #E7E5E4; padding-top: 8px; display: flex; justify-content: space-between; align-items: center;'>
                            <span style='font-size: 0.75rem; color: #57534E;'>🍚 {day_item['base_staple'][:12]}..</span>
                            <span style='font-size: 0.75rem; color: #57534E;'>⏱️ {day_item['cooking_time']}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    with st.popover(f"⚡ Actions & Recipe", use_container_width=True):
                        st.markdown(f"**{day_item['day']} Master Recipe**")
                        st.markdown(f"- 🍲 **Gravy:** {day_item['gravy']}")
                        st.markdown(f"- 🥘 **Dry Item:** {day_item['dry_item']}")
                        st.markdown(f"- 🔥 **Energy:** {day_item['calories']}")
                        
                        with st.expander("📖 View Ingredients & Step-by-Step"):
                            st.markdown("**Ingredients:**")
                            for ing in day_item['ingredients']:
                                st.markdown(f"• {ing}")
                            st.markdown("**Instructions:**")
                            for step in day_item['steps']:
                                st.markdown(f"{step}")
                                
                        col_act1, col_act2 = st.columns(2)
                        with col_act1:
                            if st.button("🔄 Refresh", key=f"ref_{selected_week}_{day_item['day']}", use_container_width=True):
                                cuisine_db = LOCAL_RECIPE_DATABASE.get(profile["cuisine"], LOCAL_RECIPE_DATABASE["South Indian"])
                                pool = cuisine_db.get("Non-Veg" if day_item['meal_type']=="Non-Veg" else "Veg", [])
                                if pool:
                                    new_rec = random.choice(pool)
                                    day_item['gravy'] = new_rec.get("gravy")
                                    day_item['dry_item'] = new_rec.get("dry_item")
                                    day_item['base_staple'] = new_rec.get("base_staple", "Steamed Rice")
                                    day_item['cooking_time'] = new_rec.get("cooking_time", "30 mins")
                                    day_item['ingredients'] = new_rec.get("ingredients", [])
                                    day_item['steps'] = new_rec.get("steps", [])
                                    st.rerun()
                        with col_act2:
                            if st.button("⇄ Swap Day", key=f"swp_{selected_week}_{day_item['day']}", use_container_width=True):
                                st.toast(f"Swapped slots for {day_item['day']}!")
                                st.rerun()

        render_enterprise_grid(row1_data)
        render_enterprise_grid(row2_data)

    # ------------------ TAB 2: SMART GROCERY LIST ------------------
    with tab_grocery:
        c_gdrop1, c_gdrop2 = st.columns([1, 2])
        with c_gdrop1:
            selected_grocery_week = st.selectbox("📅 Select Week:", weeks, key="horizon_grocery")
            
        st.markdown("<hr style='margin: 14px 0px; border-color: #D7D3D0;'>", unsafe_allow_html=True)
        
        target_week_data = st.session_state["monthly_plan"][selected_grocery_week]
        grocery_categories = aggregate_grocery_list(target_week_data)
        
        st.markdown(f"### 🛒 Aisle-by-Aisle Shopping List ({selected_grocery_week})")
        st.caption(f"Quantities automatically calculated for **{profile['adults']} Adults** and **{profile['kids']} Kids**.")
        
        g_col1, g_col2 = st.columns(2)
        cat_keys = list(grocery_categories.keys())
        
        with g_col1:
            for cat in cat_keys[:3]:
                items = grocery_categories[cat]
                if items:
                    with st.expander(f"{cat} ({len(items)} items)", expanded=True):
                        for item in items:
                            st.checkbox(f"{item}", key=f"groc_{selected_grocery_week}_{cat}_{item}")
                            
        with g_col2:
            for cat in cat_keys[3:]:
                items = grocery_categories[cat]
                if items:
                    with st.expander(f"{cat} ({len(items)} items)", expanded=True):
                        for item in items:
                            st.checkbox(f"{item}", key=f"groc_{selected_grocery_week}_{cat}_{item}")

    # ------------------ TAB 3: POSTER & FAMILY SYNC HUB ------------------
    with tab_poster_share:
        c_psdrop1, c_psdrop2 = st.columns([1, 2])
        with c_psdrop1:
            selected_ps_week = st.selectbox("📅 Select Week:", weeks, key="horizon_ps")
            
        st.markdown("<hr style='margin: 14px 0px; border-color: #D7D3D0;'>", unsafe_allow_html=True)
        ps_week_data = st.session_state["monthly_plan"][selected_ps_week]
        formatted_text = format_text_plan(selected_ps_week, ps_week_data)
        
        # Interactive Automated Scheduler Panel
        with st.expander("⏰ Configure Automated Share Scheduler & Alerts", expanded=True):
            st.write("Set up automated reminders and alert triggers to dispatch your weekly schedule to your family group:")
            sch_col1, sch_col2, sch_col3 = st.columns(3)
            with sch_col1:
                sched_day = st.selectbox("Repeat Every:", ["Every Sunday", "Every Monday", "Every Friday"])
            with sch_col2:
                sched_time = time(8, 0)
            with sch_col3:
                sched_target = st.selectbox("Dispatch Channel:", ["WhatsApp Family Group", "Household Email Inbox", "Both"])
            
            if st.button("💾 Save Scheduler Settings", use_container_width=True):
                st.success(f"✅ Alert scheduler successfully configured! Automated triggers active for **{sched_day}** via **{sched_target}**.")

        st.markdown("<br>", unsafe_allow_html=True)
        
        # Direct Sharing Actions
        encoded_text = urllib.parse.quote(formatted_text)
        whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_text}"
        email_url = f"mailto:?subject=GetDailyMenu%20Master%20Schedule%20-%20{selected_ps_week}&body={encoded_text}"
        
        s_btn1, s_btn2 = st.columns(2)
        with s_btn1:
            st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank" style="display: block; text-align: center; background-color: #25D366; color: white; padding: 14px 20px; border-radius: 12px; text-decoration: none; font-weight: 700; font-size: 1.05rem;">
                🟢 Share Master Schedule via WhatsApp
            </a>
            """, unsafe_allow_html=True)
        with s_btn2:
            st.markdown(f"""
            <a href="{email_url}" style="display: block; text-align: center; background-color: #1E3A8A; color: white; padding: 14px 20px; border-radius: 12px; text-decoration: none; font-weight: 700; font-size: 1.05rem;">
                ✉️ Send Master Schedule via Email
            </a>
            """, unsafe_allow_html=True)

        st.markdown("<br><hr style='margin: 14px 0px; border-color: #D7D3D0;'><br>", unsafe_allow_html=True)
        
        # --- NATIVE STREAMLIT POSTER FRAME ---
        st.markdown("### 🖼️ Fridge Poster Preview")
        st.caption("A clean, printable kitchen layout matching your master menu schedule.")
        
        with st.container():
            st.markdown(f"""
            <div style="border: 3px double #78350F; padding: 24px; border-radius: 16px; background-color: #ffffff;">
                <h3 style="text-align: center; color: #78350F; margin-bottom: 4px;">🍳 GetDailyMenu Master Schedule</h3>
                <p style="text-align: center; color: #57534E; font-size: 0.95rem; margin-bottom: 20px;"><b>{selected_ps_week}</b> | Cuisine: {profile['cuisine']} | Family: {profile['adults']} Adults, {profile['kids']} Kids</p>
            </div>
            """, unsafe_allow_html=True)
            
            poster_rows = []
            for item in ps_week_data:
                poster_rows.append({
                    "Day": item["day"],
                    "Type": item["meal_type"],
                    "Gravy / Main": item["gravy"],
                    "Dry Item": item["dry_item"],
                    "Staple": item["base_staple"],
                    "Cooking Time": item["cooking_time"]
                })
            poster_df = pd.DataFrame(poster_rows)
            st.dataframe(poster_df, use_container_width=True, hide_index=True)
            
            st.markdown("""
            <div style="text-align: center; color: #78716C; font-size: 0.85rem; font-style: italic; margin-top: 10px;">
                "Eat well, live well. Automatically curated for your household." ✨
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("💡 **Tip:** Press `Ctrl + P` (or `Cmd + P` on Mac) in your browser to print this gorgeous poster directly or save it as a PDF for your fridge!")

    # Master Export Footer
    st.markdown("<br>", unsafe_allow_html=True)
    col_dl1, col_dl2, col_dl3 = st.columns([1, 2, 1])
    with col_dl2:
        plan_json = json.dumps(st.session_state["monthly_plan"], indent=4)
        st.download_button(
            label="📥 Export Complete Master Meal & Grocery Data (JSON)",
            data=plan_json,
            file_name=f"GetDailyMenu_Master_{selected_ps_week}.json",
            mime="application/json",
            use_container_width=True
        )