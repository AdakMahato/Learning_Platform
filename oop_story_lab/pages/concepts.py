import streamlit as st
from ui import configure_page, sidebar

configure_page()
sidebar(active="concepts")

st.markdown('<div class="workspace-eyebrow">REFERENCE</div><h1>▤ Concept Library</h1>', unsafe_allow_html=True)
st.write("Search for any C++ or Object-Oriented concept below for a quick refresher.")

search = st.text_input("Search Concepts...", placeholder="e.g. Virtual, RAII, Constructor")

CONCEPTS = {
    "RAII": {
        "title": "RAII (Resource Acquisition Is Initialization)",
        "desc": "A C++ programming technique which binds the life cycle of a resource (allocated memory, thread execution, open socket, open file, locked mutex) to the lifetime of an object.",
        "example": "std::unique_ptr, std::lock_guard"
    },
    "Virtual Function": {
        "title": "Virtual Function",
        "desc": "A member function that you expect to be redefined in derived classes. When you refer to a derived class object using a pointer or a reference to the base class, you can call a virtual function for that object and execute the derived class's version of the function.",
        "example": "virtual void draw() = 0;"
    },
    "Rule of Five": {
        "title": "The Rule of Five",
        "desc": "If a class requires a user-defined destructor, copy constructor, or copy assignment operator, it almost certainly requires all five: Destructor, Copy Constructor, Copy Assignment Operator, Move Constructor, Move Assignment Operator.",
        "example": "MyClass(MyClass&& other) noexcept;"
    },
    "Polymorphism": {
        "title": "Polymorphism",
        "desc": "The provision of a single interface to entities of different types. In C++, this is typically achieved through inheritance and virtual functions (runtime polymorphism) or templates (compile-time polymorphism).",
        "example": "Animal* a = new Dog(); a->speak();"
    },
    "Encapsulation": {
        "title": "Encapsulation",
        "desc": "The bundling of data with the methods that operate on that data, or the restricting of direct access to some of an object's components.",
        "example": "class User { private: std::string password; };"
    },
    "Move Semantics": {
        "title": "Move Semantics",
        "desc": "Introduced in C++11, move semantics allows resources owned by an rvalue to be moved into an lvalue without copying them.",
        "example": "std::vector<int> a = std::move(b);"
    }
}

for k, v in CONCEPTS.items():
    if not search or search.lower() in k.lower() or search.lower() in v["desc"].lower():
        with st.expander(f"**{v['title']}**"):
            st.markdown(v["desc"])
            st.markdown(f"`{v['example']}`")
