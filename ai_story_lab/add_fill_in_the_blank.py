import re

with open("ui.py", "r") as f:
    content = f.read()

fill_in_blank_code = '''
        elif btype == "fill_in_the_blank":
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
                        if block.get("explanation"): st.info(block.get("explanation"))
'''

if 'btype == "fill_in_the_blank"' not in content:
    content = content.replace('elif btype == "memory_layout":', fill_in_blank_code + '\n        elif btype == "memory_layout":')

with open("ui.py", "w") as f:
    f.write(content)

print("Added fill in the blank UI!")
