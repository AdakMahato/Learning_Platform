with open("ui.py", "r") as f:
    content = f.read()

# Let's inspect the code lab block in ui.py and replace tabs with 4 rich tabs
old_code_lab = '''        elif btype in ("code_experiment", "code_lab"):
            st.markdown(f"### 💻 {block.get('title', 'Code Lab')}")

            # Using Tabs for LeetCode-style UI
            tab_editor, tab_edge_cases = st.tabs(["📝 Code Editor & Tests", "⚠️ Edge Cases & Analysis"])'''

new_code_lab = '''        elif btype in ("code_experiment", "code_lab"):
            st.markdown(f"### 💻 {block.get('title', 'Code Lab')}")

            # 4 Rich Engineering & LeetCode Tabs
            tab_editor, tab_why, tab_alternatives, tab_edge_cases = st.tabs([
                "📝 Code Editor & Execution", 
                "💡 Why This Solution Works", 
                "🔀 Alternative Approaches & Trade-offs", 
                "⚠️ Edge Cases & Failure Modes"
            ])'''

if old_code_lab in content:
    content = content.replace(old_code_lab, new_code_lab)
    print("Replaced code lab tabs!")
else:
    print("old_code_lab not found exactly, let's inspect")

# Now let's see how tab_why and tab_alternatives are added after tab_editor
old_after_editor = '''            with tab_edge_cases:
                st.info("In a real engineering environment, your code will face unexpected constraints. Consider these edge cases:")'''

new_after_editor = '''            with tab_why:
                why_text = block.get("why_it_works") or block.get("explanation") or "**Mathematical & Algorithmic Mechanics:**\\nThis solution correctly enforces the invariant required for this problem."
                st.markdown(why_text)
                
                if block.get("complexity"):
                    st.markdown("#### ⏱️ Computational Complexity")
                    st.markdown(block.get("complexity"))

            with tab_alternatives:
                alts = block.get("alternatives")
                if alts:
                    st.markdown(alts)
                else:
                    st.markdown("""
                    #### 🔀 Candidate Architectural Alternatives
                    - **Alternative 1: Brute Force Search / Naive Enumeration**
                      - *Trade-off:* Trivial to implement, but suffers from exponential time complexity $O(b^d)$ or $O(N^2)$, making it unusable on real-world inputs.
                    - **Alternative 2: Heuristic / Greedy Approximation**
                      - *Trade-off:* Dramatically faster query time ($O(N \\log N)$ or $O(1)$), but may sacrifice theoretical optimality if the heuristic is inadmissible.
                    - **Alternative 3: Probabilistic / Empirical Learning**
                      - *Trade-off:* Handles noise and high-dimensional inputs well, but requires large training datasets and lacks deterministic guarantees.
                    """)

            with tab_edge_cases:
                st.info("In a real engineering environment, your code will face unexpected constraints. Consider these edge cases:")'''

if old_after_editor in content:
    content = content.replace(old_after_editor, new_after_editor)
    print("Added tab_why and tab_alternatives to ui.py!")
else:
    print("old_after_editor not found exactly")

with open("ui.py", "w") as f:
    f.write(content)

print("ui.py updated!")
