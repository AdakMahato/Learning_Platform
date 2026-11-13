path = '/Users/aadarshamahato/Downloads/LEARNING_PLATFORM/ai_story_lab/ui.py'
with open(path, 'r') as f:
    content = f.read()

# Replace the interactive block handling with enhanced feedback and study guide expander
old_interactive_block = '''        elif btype in ("micro_challenge", "mastery_challenge", "interactive"):
            st.markdown(f"### 🏆 {block.get('title', 'Challenge')}")
            q = block.get("question") or block.get("content", "")
            st.write(q)
            with st.form(key=f"mc_form_{story_id}_{viewing}_{block_idx}"):
                chosen = st.radio("Select answer:", block["options"], key=f"mc_radio_{story_id}_{viewing}_{block_idx}")
                if st.form_submit_button("Submit"):
                    idx = block["options"].index(chosen)
                    ans = block.get("answer", -1)
                    if idx == ans or chosen == ans:
                        st.success("Correct!")
                        if block.get("explanation"): st.info(block.get("explanation"))
                    else:
                        st.error("Incorrect.")
                        if block.get("explanation"): st.info(block.get("explanation"))'''

new_interactive_block = '''        elif btype in ("micro_challenge", "mastery_challenge", "interactive"):
            st.markdown(f"### 🏆 {block.get('title', 'Knowledge & Concept Challenge')}")
            q = block.get("question") or block.get("content", "")
            st.markdown(f"**{q}**")
            
            with st.form(key=f"mc_form_{story_id}_{viewing}_{block_idx}"):
                chosen = st.radio("Select your answer:", block["options"], key=f"mc_radio_{story_id}_{viewing}_{block_idx}")
                submitted = st.form_submit_button("Submit Answer ▶")
                if submitted:
                    idx = block["options"].index(chosen)
                    ans = block.get("answer", -1)
                    
                    is_correct = False
                    if isinstance(ans, int) and idx == ans:
                        is_correct = True
                    elif isinstance(ans, str):
                        if chosen.strip().lower() == ans.strip().lower():
                            is_correct = True
                        elif ans.isdigit() and idx == int(ans) - 1:
                            is_correct = True
                            
                    if is_correct:
                        st.success(f"✅ **Correct!** `{chosen}` is the right answer.")
                    else:
                        correct_str = ans if isinstance(ans, str) else block["options"][ans]
                        st.error(f"❌ **Incorrect.** You selected `{chosen}`. The correct answer is **`{correct_str}`**.")
                    
                    if block.get("explanation"):
                        st.markdown(f"""
                        <div style="background: rgba(124, 77, 255, 0.08); border: 1px solid rgba(124, 77, 255, 0.3); border-left: 5px solid #7C4DFF; padding: 20px 24px; border-radius: 8px; margin-top: 16px;">
                            {block.get("explanation")}
                        </div>
                        """, unsafe_allow_html=True)
                        
            if block.get("explanation"):
                with st.expander("💡 Study Guide: Reveal In-Depth Answer & Explanation"):
                    st.markdown(block.get("explanation"))'''

assert old_interactive_block in content, "old_interactive_block not found in ui.py!"
content = content.replace(old_interactive_block, new_interactive_block, 1)

# Also enhance fill_in_the_blank
old_fib_block = '''        elif btype == "fill_in_the_blank":
            st.markdown(f"### ✍️ {block.get('title', 'Fill in the Blank')}")
            q = block.get("question", "")
            
            with st.form(key=f"fib_form_{story_id}_{viewing}_{block_idx}"):
                st.markdown(q.replace("_____", "___"))
                user_ans = st.text_input("Your Answer:", key=f"fib_input_{story_id}_{viewing}_{block_idx}")
                
                if st.form_submit_button("Submit"):
                    ans = block.get("answer", "")
                    if user_ans.strip().lower() == ans.strip().lower():
                        st.success("Correct!")
                        if block.get("explanation"): st.info(block.get("explanation"))
                    else:
                        st.error("Incorrect.")
                        if block.get("explanation"): st.info(block.get("explanation"))'''

new_fib_block = '''        elif btype == "fill_in_the_blank":
            st.markdown(f"### ✍️ {block.get('title', 'Fill in the Blank Challenge')}")
            q = block.get("question", "")
            
            with st.form(key=f"fib_form_{story_id}_{viewing}_{block_idx}"):
                st.markdown(q.replace("_____", "___"))
                user_ans = st.text_input("Your Answer:", key=f"fib_input_{story_id}_{viewing}_{block_idx}")
                
                submitted = st.form_submit_button("Submit Answer ▶")
                if submitted:
                    ans = block.get("answer", "")
                    if user_ans.strip().lower() == ans.strip().lower():
                        st.success(f"✅ **Correct!** `{user_ans}` is the right answer.")
                    else:
                        st.error(f"❌ **Incorrect.** You entered `{user_ans}`. The expected answer is **`{ans}`**.")
                    
                    if block.get("explanation"):
                        st.markdown(f"""
                        <div style="background: rgba(124, 77, 255, 0.08); border: 1px solid rgba(124, 77, 255, 0.3); border-left: 5px solid #7C4DFF; padding: 20px 24px; border-radius: 8px; margin-top: 16px;">
                            {block.get("explanation")}
                        </div>
                        """, unsafe_allow_html=True)
                        
            if block.get("explanation"):
                with st.expander("💡 Study Guide: Reveal In-Depth Answer & Explanation"):
                    st.markdown(block.get("explanation"))'''

assert old_fib_block in content, "old_fib_block not found in ui.py!"
content = content.replace(old_fib_block, new_fib_block, 1)

with open(path, 'w') as f:
    f.write(content)

print("ui.py successfully upgraded with enhanced quiz rendering and study guide expanders!")
