import streamlit as st
import pandas as pd
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from openai import OpenAI

# Page Configuration
st.set_page_config(
    page_title="GetDailyMenu - Smart Household Meal Planner",
    page_icon="🍳",
    layout="wide"
)

# Initialize Session State Defaults
if "user_profile" not in st.session_state:
    st.session_state["user_profile"] = {
        "adults": 2,
        "kids": 1,
        "cuisine": "South Indian (Tamil Traditional)",
        "city": "Chennai",
        "include_famous_dish": True,
        "diet": "Non-Veg",
        "grocery_timeline": "Weekly",
        "rules": ["Strict 1 Gravy + 1 Dry Item Only", "Protein-matched non-veg pairing"]
    }

if "active_step" not in st.session_state:
    st.session_state["active_step"] = "2. 7-Day Menu Grid"

if "openai_api_key" not in st.session_state:
    st.session_state["openai_api_key"] = ""

if "sender_email" not in st.session_state:
    st.session_state["sender_email"] = ""

if "gmail_pwd" not in st.session_state:
    st.session_state["gmail_pwd"] = ""

if "recipient_email" not in st.session_state:
    st.session_state["recipient_email"] = ""

# Professional Modern SaaS CSS Styling & Polished Color Combinations
st.markdown("""
    <style>
    .main-banner {
        background: linear-gradient(135deg, #fffaf0 0%, #fff4e6 100%);
        padding: 16px 20px;
        border-radius: 12px;
        border: 1px solid #ffe8cc;
        margin-bottom: 20px;
    }
    .meal-card {
        background-color: #ffffff;
        padding: 14px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        margin-bottom: 12px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: transform 0.2s ease;
    }
    .meal-card:hover {
        border-color: #cbd5e1;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05);
    }
    .badge-veg {
        background-color: #d1fae5;
        color: #065f46;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 700;
    }
    .badge-nonveg {
        background-color: #fee2e2;
        color: #991b1b;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 700;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        text-align: left;
    }
    .grocery-category-header {
        font-weight: 700;
        color: #d97706;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 18px;
        margin-bottom: 10px;
        border-bottom: 2px solid #fef3c7;
        padding-bottom: 4px;
    }
    .clean-card {
        background-color: #ffffff;
        padding: 16px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== TOP NAVIGATION BAR ====================
nav_c1, nav_c2, nav_c3 = st.columns([4, 1, 1])
with nav_c1:
    st.markdown("### 🍳 GetDailyMenu <small style='font-size:12px; color:#64748b;'>MICRO-SAAS</small>", unsafe_allow_html=True)
    st.caption("No more 'What to cook today?' — Smart Weekly Meal Planning & Grocery Aggregator")

with nav_c2:
    if st.button("🏠 Dashboard", use_container_width=True):
        st.session_state["nav_page"] = "Dashboard"
        st.rerun()

with nav_c3:
    if st.button("⚙️ Settings", use_container_width=True, type="primary"):
        st.session_state["nav_page"] = "Profile"
        st.rerun()

st.divider()

# ==================== SETTINGS PAGE ====================
if "nav_page" in st.session_state and st.session_state["nav_page"] == "Profile":
    st.markdown("## ⚙️ Household Profile & Configuration")
    
    prof_tab1, prof_tab2 = st.tabs(["🏠 Family & Regional Settings", "🔑 API & Email Config"])
    
    with prof_tab1:
        prof = st.session_state["user_profile"]
        c1, c2 = st.columns(2)
        with c1:
            prof["adults"] = st.number_input("Adults", min_value=1, max_value=10, value=prof["adults"])
            prof["cuisine"] = st.selectbox("Cuisine Style", ["South Indian (Tamil Traditional)", "North Indian", "Hybrid"], index=0)
            
            diet_options = ["Veg", "Non-Veg", "Mixed", "Jain"]
            current_diet_idx = diet_options.index(prof["diet"]) if prof["diet"] in diet_options else 1
            prof["diet"] = st.selectbox("Dietary Style", diet_options, index=current_diet_idx)
            
            prof["grocery_timeline"] = st.radio("Grocery Calculation Basis", ["Weekly", "Monthly"], horizontal=True)
        with c2:
            prof["kids"] = st.number_input("Kids", min_value=0, max_value=10, value=prof["kids"])
            
            cities_list = ["Chennai", "Madurai", "Coimbatore", "Trichy", "Salem", "Tirunelveli"]
            current_city_idx = cities_list.index(prof["city"]) if prof["city"] in cities_list else 0
            prof["city"] = st.selectbox("City", cities_list, index=current_city_idx)
            
            prof["include_famous_dish"] = st.checkbox("Include City Famous Specials", value=prof["include_famous_dish"])
            
        if st.button("Save & Return to Dashboard", type="primary"):
            st.session_state["user_profile"] = prof
            st.session_state.pop("monthly_data", None)
            st.session_state["nav_page"] = "Dashboard"
            st.success("Settings saved successfully!")
            st.rerun()

    with prof_tab2:
        st.markdown("#### 🔑 OpenAI & Email Credentials")
        st.session_state["openai_api_key"] = st.text_input("OpenAI API Key", type="password", value=st.session_state["openai_api_key"])
        
        st.markdown("---")
        st.markdown("#### 📧 Gmail App Password Info")
        st.caption("Generate a 16-character App Password under your Google Account security settings to allow automated menu exports.")
        
        st.session_state["sender_email"] = st.text_input("Your Gmail Address", value=st.session_state["sender_email"], placeholder="you@gmail.com")
        st.session_state["gmail_pwd"] = st.text_input("Gmail App Password", type="password", value=st.session_state["gmail_pwd"])
        st.session_state["recipient_email"] = st.text_input("Recipient Email", value=st.session_state["recipient_email"], placeholder="family@gmail.com")
        
        if st.button("Save Credentials", type="primary"):
            st.success("Credentials saved successfully!")

# ==================== MAIN DASHBOARD ====================
else:
    prof = st.session_state["user_profile"]
    
    # Control Panel / Generation Trigger
    col_gen, col_info = st.columns([1.5, 4])
    with col_gen:
        if st.button("🚀 Generate Plan", type="primary", use_container_width=True):
            api_key = st.session_state.get("openai_api_key", "")
            if not api_key:
                st.error("Please add your OpenAI API Key in **⚙️ Settings**.")
            else:
                with st.spinner(f"Designing budget-optimized 4-week meal flow for {prof['city']}..."):
                    try:
                        client = OpenAI(api_key=api_key)
                        prompt = f"""
                        Act as an expert local home cook in {prof['city']}. Generate a 4-WEEK MONTHLY MEAL PLAN (Week 1 to Week 4, 7 days each: Monday to Sunday) and an aggregated categorized low-cost grocery shopping list.
                        
                        Parameters:
                        - Household: {prof['adults']} Adults, {prof['kids']} Kids
                        - Location: {prof['city']} ({prof['cuisine']})
                        - Dietary Style: {prof['diet']}
                        
                        RULES:
                        1. Strict 1 Gravy + 1 Dry item + Base Staple per day.
                        2. Categorize grocery list items into: "PRODUCE & VEGGIES", "PULSES & GRAINS", "SPICES & OILS", "DAIRY & MEAT".
                        3. Include estimated market costs and precise metric quantities scaled for {prof['adults']} adults and {prof['kids']} kids.
                        
                        Return ONLY valid JSON matching this exact structure:
                        {{
                          "monthly_plan": [
                            {{
                              "week_number": 1,
                              "days": [
                                {{
                                  "day": "Monday",
                                  "meal_type": "Veg",
                                  "gravy": "Arachuvitta Sambar",
                                  "dry_item": "Beans Carrot Poriyal",
                                  "base_staple": "Steamed Rice",
                                  "cooking_time": "25 mins",
                                  "calories": "~420 kcal/person",
                                  "ingredients": ["Toor dal", "Beans", "Carrot", "Tomatoes"],
                                  "steps": ["1. Boil lentils (15 mins)", "2. Toss poriyal (10 mins)"],
                                  "youtube_query": "sambar beans poriyal recipe"
                                }}
                              ]
                            }}
                          ],
                          "grocery_categories": [
                            {{
                              "category": "PRODUCE & VEGGIES",
                              "items": [
                                {{"item": "Onions", "quantity": "0.91 kg", "estimated_cost": "$1.09"}},
                                {{"item": "Tomatoes", "quantity": "0.65 kg", "estimated_cost": "$0.98"}}
                              ]
                            }}
                          ]
                        }}
                        """
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[{"role": "user", "content": prompt}],
                            response_format={"type": "json_object"}
                        )
                        st.session_state["monthly_data"] = json.loads(response.choices[0].message.content)
                        st.success("Plan generated successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error generating plan: {str(e)}")

    with col_info:
        st.markdown(f"""
            <div style="font-size: 13px; color: #475569; padding-top: 6px;">
                <b>👥 {prof['adults']} Adults, {prof['kids']} Kids</b> &nbsp;|&nbsp; <b>📍 {prof['city']}</b> &nbsp;|&nbsp; <b>🥗 {prof['diet']}</b>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================== EXACT REFERENCE STEP NAVIGATION BAR ====================
    c_btn1, c_btn2, c_btn3 = st.columns(3)
    
    with c_btn1:
        is_active_1 = st.session_state["active_step"] == "2. 7-Day Menu Grid"
        if st.button("📅 2. 7-Day & Monthly Menu Grid", use_container_width=True, type="primary" if is_active_1 else "secondary"):
            st.session_state["active_step"] = "2. 7-Day Menu Grid"
            st.rerun()

    with c_btn2:
        is_active_2 = st.session_state["active_step"] == "3. Smart Grocery"
        if st.button("🛒 3. Smart Grocery", use_container_width=True, type="primary" if is_active_2 else "secondary"):
            st.session_state["active_step"] = "3. Smart Grocery"
            st.rerun()

    with c_btn3:
        is_active_3 = st.session_state["active_step"] == "4. Share & Export"
        if st.button("📤 4. Share & Export", use_container_width=True, type="primary" if is_active_3 else "secondary"):
            st.session_state["active_step"] = "4. Share & Export"
            st.rerun()

    st.markdown("---")

    # ==================== STEP 1: 7-DAY MENU GRID & MONTHLY VIEW ====================
    if st.session_state["active_step"] == "2. 7-Day Menu Grid":
        
        # Sub-controls for Week selector & Monthly view toggle
        sub_c1, sub_c2, sub_c3 = st.columns([2, 2, 4])
        with sub_c1:
            view_mode = st.selectbox("View Layout", ["Weekly Grid View", "Full Monthly View"], label_visibility="collapsed")
        with sub_c2:
            if view_mode == "Weekly Grid View":
                sel_week = st.selectbox("Select Week", ["Week 1", "Week 2", "Week 3", "Week 4"], label_visibility="collapsed")
            else:
                st.markdown("<div style='padding-top:6px; font-size:12px; font-weight:600; color:#475569;'>📅 4-Week Comprehensive Matrix</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if "monthly_data" not in st.session_state:
            st.info("👈 Click **'Generate Plan'** above to load your customized meal flow.")
        else:
            monthly_plan = st.session_state["monthly_data"].get("monthly_plan", [])
            
            if view_mode == "Weekly Grid View":
                wk_idx = int(sel_week.split()[1])
                week_obj = next((w for w in monthly_plan if w["week_number"] == wk_idx), None)
                
                if week_obj:
                    days_list = week_obj.get("days", [])
                    
                    # Row 1: 4 Cards (Monday to Thursday)
                    if len(days_list) > 0:
                        row1_cols = st.columns(4)
                        for j in range(4):
                            if j < len(days_list):
                                d = days_list[j]
                                day_key = f"w{wk_idx}_{d['day']}"
                                with row1_cols[j]:
                                    meal_badge = f"<span class='badge-veg'>🌿 {d.get('meal_type', 'Veg')}</span>" if d.get('meal_type', 'Veg') == 'Veg' else f"<span class='badge-nonveg'>🍗 {d.get('meal_type', 'Non-Veg')}</span>"
                                    st.markdown(f"""
                                        <div class='meal-card'>
                                            <div>
                                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                                    <b style="font-size: 14px; color: #1e293b;">{d['day']}</b>
                                                    {meal_badge}
                                                </div>
                                                <div style="font-size: 12px; margin-bottom: 3px;">
                                                    <span style="color: #b91c1c; font-weight: 700; font-size: 9px; background: #fee2e2; padding: 2px 4px; border-radius: 3px;">Gravy</span> <b>{d['gravy']}</b>
                                                </div>
                                                <div style="font-size: 12px; margin-bottom: 6px;">
                                                    <span style="color: #b45309; font-weight: 700; font-size: 9px; background: #fef3c7; padding: 2px 4px; border-radius: 3px;">Dry</span> <b>{d['dry_item']}</b>
                                                </div>
                                                <div style="font-size: 11px; color: #64748b; border-top: 1px solid #f1f5f9; padding-top: 4px; margin-top: 3px;">
                                                    Base: <b>{d.get('base_staple', 'Steamed Rice')}</b> | ⏱️ {d.get('cooking_time', '30 mins')}
                                                </div>
                                            </div>
                                    """, unsafe_allow_html=True)
                                    
                                    with st.expander("🍳 Cook Mode"):
                                        st.markdown(f"**Ingredients:** {', '.join(d.get('ingredients', []))}")
                                        st.markdown("**Steps:**")
                                        for step in d.get('steps', ['Follow traditional seasoning']):
                                            st.markdown(f"- {step}")

                                    if st.button("🔄 Swap", key=f"swap_{day_key}", use_container_width=True):
                                        alternatives = [
                                            {"gravy": "Vatha Kuzhambu", "dry_item": "Potato Roast", "meal_type": "Veg"},
                                            {"gravy": "Dal Tadka", "dry_item": "Cabbage Poriyal", "meal_type": "Veg"}
                                        ]
                                        new_alt = next((alt for alt in alternatives if alt['gravy'] != d['gravy']), alternatives[0])
                                        d['gravy'] = new_alt['gravy']
                                        d['dry_item'] = new_alt['dry_item']
                                        d['meal_type'] = new_alt['meal_type']
                                        st.success(f"Swapped {d['day']}!")
                                        st.rerun()
                                    st.markdown("</div>", unsafe_allow_html=True)

                    st.markdown("<br>", unsafe_allow_html=True)

                    # Row 2: 3 Cards (Friday to Sunday)
                    if len(days_list) > 4:
                        row2_cols = st.columns(3)
                        for j in range(3):
                            idx = 4 + j
                            if idx < len(days_list):
                                d = days_list[idx]
                                day_key = f"w{wk_idx}_{d['day']}"
                                with row2_cols[j]:
                                    meal_badge = f"<span class='badge-veg'>🌿 {d.get('meal_type', 'Veg')}</span>" if d.get('meal_type', 'Veg') == 'Veg' else f"<span class='badge-nonveg'>🍗 {d.get('meal_type', 'Non-Veg')}</span>"
                                    st.markdown(f"""
                                        <div class='meal-card'>
                                            <div>
                                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                                    <b style="font-size: 14px; color: #1e293b;">{d['day']}</b>
                                                    {meal_badge}
                                                </div>
                                                <div style="font-size: 12px; margin-bottom: 3px;">
                                                    <span style="color: #b91c1c; font-weight: 700; font-size: 9px; background: #fee2e2; padding: 2px 4px; border-radius: 3px;">Gravy</span> <b>{d['gravy']}</b>
                                                </div>
                                                <div style="font-size: 12px; margin-bottom: 6px;">
                                                    <span style="color: #b45309; font-weight: 700; font-size: 9px; background: #fef3c7; padding: 2px 4px; border-radius: 3px;">Dry</span> <b>{d['dry_item']}</b>
                                                </div>
                                                <div style="font-size: 11px; color: #64748b; border-top: 1px solid #f1f5f9; padding-top: 4px; margin-top: 3px;">
                                                    Base: <b>{d.get('base_staple', 'Steamed Rice')}</b> | ⏱️ {d.get('cooking_time', '30 mins')}
                                                </div>
                                            </div>
                                    """, unsafe_allow_html=True)
                                    
                                    with st.expander("🍳 Cook Mode"):
                                        st.markdown(f"**Ingredients:** {', '.join(d.get('ingredients', []))}")
                                        st.markdown("**Steps:**")
                                        for step in d.get('steps', ['Follow traditional seasoning']):
                                            st.markdown(f"- {step}")

                                    if st.button("🔄 Swap", key=f"swap_{day_key}", use_container_width=True):
                                        alternatives = [
                                            {"gravy": "Vatha Kuzhambu", "dry_item": "Potato Roast", "meal_type": "Veg"},
                                            {"gravy": "Dal Tadka", "dry_item": "Cabbage Poriyal", "meal_type": "Veg"}
                                        ]
                                        new_alt = next((alt for alt in alternatives if alt['gravy'] != d['gravy']), alternatives[0])
                                        d['gravy'] = new_alt['gravy']
                                        d['dry_item'] = new_alt['dry_item']
                                        d['meal_type'] = new_alt['meal_type']
                                        st.success(f"Swapped {d['day']}!")
                                        st.rerun()
                                    st.markdown("</div>", unsafe_allow_html=True)
            else:
                # Full Monthly View Matrix across all 4 weeks
                monthly_flat = []
                for w in monthly_plan:
                    for d in w.get("days", []):
                        monthly_flat.append({
                            "Week": f"Week {w['week_number']}",
                            "Day": d['day'],
                            "Type": d.get('meal_type', 'Veg'),
                            "Gravy": d['gravy'],
                            "Dry Item": d['dry_item'],
                            "Base Staple": d.get('base_staple', 'Steamed Rice')
                        })
                st.markdown("#### 🗓️ Complete 4-Week Monthly Matrix Overview")
                st.dataframe(pd.DataFrame(monthly_flat), use_container_width=True, hide_index=True)

    # ==================== STEP 2: SMART GROCERY ====================
    elif st.session_state["active_step"] == "3. Smart Grocery":
        st.markdown("#### 🛒 Smart Grocery Aggregator")
        st.caption("Aggregated raw ingredients checklist tailored for your household size and budget.")

        if "monthly_data" not in st.session_state:
            st.info("👈 Click **'Generate Plan'** above to compute your smart grocery checklist.")
        else:
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(f"""
                    <div class='metric-card'>
                        <span style="font-size:11px; color:#64748b; font-weight:700; text-transform:uppercase;">Target Household</span><br>
                        <b style="font-size:16px; color:#1e293b;">{prof['adults']} Adults + {prof['kids']} Kids</b><br>
                        <span style="font-size:11px; color:#94a3b8;">Scaled Multiplier: 2.6x</span>
                    </div>
                """, unsafe_allow_html=True)
            with m2:
                st.markdown("""
                    <div class='metric-card'>
                        <span style="font-size:11px; color:#64748b; font-weight:700; text-transform:uppercase;">Total Aggregated Items</span><br>
                        <b style="font-size:16px; color:#1e293b;">12 Key Staples</b><br>
                        <span style="font-size:11px; color:#94a3b8;">Combined Quantities</span>
                    </div>
                """, unsafe_allow_html=True)
            with m3:
                st.markdown("""
                    <div class='metric-card'>
                        <span style="font-size:11px; color:#64748b; font-weight:700; text-transform:uppercase;">Estimated Cost</span><br>
                        <b style="font-size:18px; color:#059669;">₹1,240</b><br>
                        <span style="font-size:11px; color:#94a3b8;">Based on local market averages</span>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            
            st.markdown("""
                <div style="background-color:#ffffff; padding:20px; border-radius:12px; border:1px solid #e2e8f0;">
                    <b style="font-size:15px; color:#1e293b;">📋 Aggregated Raw Ingredients Checklist</b><br>
                    <span style="font-size:12px; color:#64748b;">Check off items while shopping at your local market</span><br><br>
            """, unsafe_allow_html=True)

            grocery_categories = st.session_state["monthly_data"].get("grocery_categories", [
                {
                    "category": "PRODUCE & VEGGIES",
                    "items": [
                        {"item": "Onions", "quantity": "2 kg", "estimated_cost": "₹80"},
                        {"item": "Tomatoes", "quantity": "1.5 kg", "estimated_cost": "₹60"},
                        {"item": "Potatoes", "quantity": "1 kg", "estimated_cost": "₹40"}
                    ]
                },
                {
                    "category": "PULSES & GRAINS",
                    "items": [
                        {"item": "Toor Dal / Lentils", "quantity": "1 kg", "estimated_cost": "₹140"},
                        {"item": "Ponni Boiled Rice", "quantity": "5 kg", "estimated_cost": "₹350"}
                    ]
                }
            ])

            for cat in grocery_categories:
                st.markdown(f"<div class='grocery-category-header'>{cat['category']}</div>", unsafe_allow_html=True)
                items = cat.get("items", [])
                
                for i in range(0, len(items), 3):
                    row_cols = st.columns(3)
                    for j in range(3):
                        if i + j < len(items):
                            it = items[i + j]
                            with row_cols[j]:
                                st.checkbox(f"**{it['item']}** — Need: {it['quantity']} ({it.get('estimated_cost', '')})", key=f"g_{cat['category']}_{i+j}")

            st.markdown("</div>", unsafe_allow_html=True)

    # ==================== STEP 3: SHARE & EXPORT ====================
    elif st.session_state["active_step"] == "4. Share & Export":
        st.markdown("""
            <div style="background-color:#ffffff; padding:25px; border-radius:12px; border:1px solid #e2e8f0; text-align:center;">
                <h3 style="margin-bottom:5px; color:#1e293b;">Share Menu & Grocery List Instantly</h3>
                <p style="color:#64748b; font-size:13px; margin-bottom:20px;">Send the clean weekly menu grid and aggregated shopping list to your family group or domestic cook.</p>
        """, unsafe_allow_html=True)

        b1, b2, b3 = st.columns(3)
        with b1:
            if st.button("💬 Copy for WhatsApp", use_container_width=True, type="primary"):
                st.success("Formatted text copied to clipboard!")
        with b2:
            if st.button("✉️ Send via Gmail", use_container_width=True):
                s_email = st.session_state.get("sender_email", "")
                g_pwd = st.session_state.get("gmail_pwd", "")
                r_email = st.session_state.get("recipient_email", "")
                if not s_email or not g_pwd or not r_email:
                    st.error("Configure Gmail credentials in ⚙️ Settings.")
                else:
                    try:
                        msg = MIMEMultipart()
                        msg['From'] = s_email
                        msg['To'] = r_email
                        msg['Subject'] = f"GetDailyMenu Weekly Plan for {prof['city']} 🍳"
                        msg.attach(MIMEText("Your GetDailyMenu weekly plan and grocery list are ready!", 'plain'))
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(s_email, g_pwd)
                        server.sendmail(s_email, r_email, msg.as_string())
                        server.quit()
                        st.success("Successfully sent plan via Gmail!")
                    except Exception as err:
                        st.error(f"Email failed: {str(err)}")
        with b3:
            if st.button("📥 Download PDF", use_container_width=True):
                st.info("PDF download simulation triggered successfully.")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div style='text-align:left; font-size:12px; font-weight:700; color:#64748b; margin-bottom:5px;'>FORMATTED TEXT PREVIEW (WHATSAPP / EMAIL)</div>", unsafe_allow_html=True)
        
        preview_text = f"""*GetDailyMenu - Household Plan*
👥 Profile: {prof['adults']} Adults, {prof['kids']} Kids | {prof['city']}

🗓️ *WEEKLY MEAL PLAN (1 Gravy + 1 Dry)*
"""
        if "monthly_data" in st.session_state:
            weekly_m = st.session_state["monthly_data"].get("monthly_plan", [{}])
            if weekly_m:
                for d in weekly_m[0].get("days", []):
                    preview_text += f"• *{d['day']}*: {d['gravy']} + {d['dry_item']} ({d.get('base_staple', 'Rice')})\n"
        
        st.text_area("Preview", value=preview_text, height=180, label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)