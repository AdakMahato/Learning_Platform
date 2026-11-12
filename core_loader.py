"""
Core Engine & Subject Registry for the Unified Engineering Learning Platform.
Dynamically loads and caches the 5 specialized computer science disciplines:
1. Database Management Systems (DBMS)
2. Artificial Intelligence (AI)
3. Software Engineering (SE)
4. Cloud Computing (Cloud)
5. Object-Oriented Programming in C++ (OOP)
"""

import os
import sys
import importlib.util
from typing import Dict, List, Any, Optional

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SUBJECT_REGISTRY = {
    "dbms": {
        "id": "dbms",
        "folder": "dbms_story_lab",
        "name": "Database Management Systems",
        "short_name": "DBMS",
        "icon": "🗄️",
        "color": "#10B981",
        "badge": "Data Architecture & Storage",
        "gradient": "linear-gradient(135deg, #064E3B 0%, #059669 50%, #10B981 100%)",
        "border_color": "rgba(16, 185, 129, 0.35)",
        "tagline": "Master relational calculus, SQL optimization, normalization surgery, ACID concurrency, and internal storage structures like B+ Trees.",
        "tags": ["Relational Algebra", "SQL Plans", "ACID", "2PL & WAL", "B+ Trees", "Normalization", "Storage Engines"],
        "hero_stat": "12 Forensic Cases • 48 In-Depth Modules"
    },
    "ai": {
        "id": "ai",
        "folder": "ai_story_lab",
        "name": "Artificial Intelligence",
        "short_name": "AI",
        "icon": "🧠",
        "color": "#8B5CF6",
        "badge": "Cognitive Systems & Search",
        "gradient": "linear-gradient(135deg, #4C1D95 0%, #6D28D9 50%, #8B5CF6 100%)",
        "border_color": "rgba(139, 92, 246, 0.35)",
        "tagline": "Explore goal-oriented agents, heuristic A* state-space search, adversarial Minimax, CSP solvers, Bayesian networks, and reinforcement learning.",
        "tags": ["A* & Heuristics", "Minimax & Alpha-Beta", "CSPs", "Propositional Logic", "Bayesian Inference", "Q-Learning"],
        "hero_stat": "25 Forensic Cases • 100 In-Depth Modules"
    },
    "se": {
        "id": "se",
        "folder": "se_story_lab",
        "name": "Software Engineering",
        "short_name": "SE",
        "icon": "💻",
        "color": "#6366F1",
        "badge": "SDLC, Architecture & Testing",
        "gradient": "linear-gradient(135deg, #312E81 0%, #4338CA 50%, #6366F1 100%)",
        "border_color": "rgba(99, 102, 241, 0.35)",
        "tagline": "Investigate real architectural breakdowns, agile lifecycle evolutions, IEEE SRS requirements, UML topologies, SOLID patterns, and automated test suites.",
        "tags": ["Waterfall & Scrum", "IEEE SRS & QFD", "Process DFDs", "UML Topologies", "Cohesion & Coupling", "Forensics"],
        "hero_stat": "16 Forensic Cases • 64 In-Depth Modules"
    },
    "cloud": {
        "id": "cloud",
        "folder": "cloud_story_lab",
        "name": "Cloud Computing",
        "short_name": "Cloud",
        "icon": "☁️",
        "color": "#38BDF8",
        "badge": "Distributed Systems & Infra",
        "gradient": "linear-gradient(135deg, #0C4A6E 0%, #0369A1 50%, #38BDF8 100%)",
        "border_color": "rgba(56, 189, 248, 0.35)",
        "tagline": "Engineer hyperscale cloud topologies, contrast AWS primitives (SQS, S3, EC2), dissect hypervisors, orchestrate MapReduce, and design green FinOps architectures.",
        "tags": ["AWS SQS/S3/EC2", "Type-1/2 Hypervisors", "SDN & VPCs", "Hadoop & MapReduce", "NoSQL Ring", "FinOps & PUE"],
        "hero_stat": "16 Forensic Cases • 64 In-Depth Modules"
    },
    "oop": {
        "id": "oop",
        "folder": "oop_story_lab",
        "name": "Object-Oriented Programming (C++)",
        "short_name": "C++ OOP",
        "icon": "⚡",
        "color": "#F59E0B",
        "badge": "Memory Layout & System Design",
        "gradient": "linear-gradient(135deg, #78350F 0%, #B45309 50%, #F59E0B 100%)",
        "border_color": "rgba(245, 158, 11, 0.35)",
        "tagline": "Master low-level memory layouts, pointers, VTable dispatch mechanisms, virtual destructors, RAII, move semantics, and enterprise design patterns.",
        "tags": ["Stack & Heap Layout", "Pointers & References", "Virtual Dispatch", "Polymorphism", "Templates", "Design Patterns"],
        "hero_stat": "29 Forensic Cases • 116 In-Depth Modules"
    },
    "dsa": {
        "id": "dsa",
        "folder": "dsa_story_lab",
        "name": "Data Structures & Algorithms",
        "short_name": "DSA",
        "icon": "🧩",
        "color": "#06B6D4",
        "badge": "LeetCode • Code360 • CS Theory",
        "gradient": "linear-gradient(135deg, #164E63 0%, #0891B2 50%, #06B6D4 100%)",
        "border_color": "rgba(6, 182, 212, 0.38)",
        "tagline": "Crack A-Z algorithmic interviews with an interactive dual Python 3 + C++17 Online Judge paired with asymptotic proofs, Master Theorem, DP recurrences, and graph invariants.",
        "tags": ["Dual Python+C++ Judge", "Arrays/Sliding Window", "Trees & Graphs", "Dynamic Programming", "Asymptotic Proofs", "Tries & Bitmask"],
        "hero_stat": "19 Forensic Cases • 76 Modules • 38 Judges"
    },
    "sd": {
        "id": "sd",
        "folder": "sd_story_lab",
        "name": "System Design (HLD & LLD)",
        "short_name": "Sys Design",
        "icon": "🏛️",
        "color": "#EC4899",
        "badge": "HLD Architecture • Machine Coding",
        "gradient": "linear-gradient(135deg, #831843 0%, #BE185D 50%, #EC4899 100%)",
        "border_color": "rgba(236, 72, 153, 0.38)",
        "tagline": "Architect web-scale distributed backends and clean SOLID OOP systems: consistent hashing, Raft quorums, LRU & rate limiters, Snowflake IDs, TinyURL, Chat & Parking Lot.",
        "tags": ["Back-of-Envelope Math", "Caching & Hash Ring", "CAP/PACELC & Raft", "HLD Case Studies", "SOLID & Concurrency", "Machine Coding Labs"],
        "hero_stat": "14 Forensic Cases • 56 In-Depth Modules"
    },
    "ip": {
        "id": "ip",
        "folder": "ip_story_lab",
        "name": "Image Processing",
        "short_name": "Img Proc",
        "icon": "🎞️",
        "color": "#F43F5E",
        "badge": "Spatial • Spectral • Video Coding",
        "gradient": "linear-gradient(135deg, #881337 0%, #E11D48 50%, #F43F5E 100%)",
        "border_color": "rgba(244, 63, 94, 0.38)",
        "tagline": "Master digital image topology, 2-D Fourier & homomorphic filters, Wiener restoration, HSI/color segmentation, wavelets, morphology, Hough/Otsu, and MPEG/SVC video coding.",
        "tags": ["2D FFT & Wiener", "HSI & Wavelets", "Morphology & Otsu", "Motion & MPEG/SVC", "Python NumPy Labs"],
        "hero_stat": "16 Forensic Cases • 64 In-Depth Modules"
    }
}

# Cache loaded subject modules
_SUBJECT_CACHE: Dict[str, Dict[str, Any]] = {}

def get_subject_meta(subject_id: str) -> Optional[Dict[str, Any]]:
    return SUBJECT_REGISTRY.get(subject_id)

def get_all_subject_metas() -> List[Dict[str, Any]]:
    return list(SUBJECT_REGISTRY.values())

def load_subject_data(subject_id: str) -> Dict[str, Any]:
    if subject_id in _SUBJECT_CACHE:
        return _SUBJECT_CACHE[subject_id]
        
    meta = SUBJECT_REGISTRY.get(subject_id)
    if not meta:
        raise ValueError(f"Unknown subject identifier: {subject_id}")
        
    folder_path = os.path.join(BASE_DIR, meta["folder"])
    sd_path = os.path.join(folder_path, "story_data.py")
    lc_path = os.path.join(folder_path, "level_content.py")
    
    # Load story_data
    spec_sd = importlib.util.spec_from_file_location(f"{subject_id}_story_data", sd_path)
    mod_sd = importlib.util.module_from_spec(spec_sd)
    spec_sd.loader.exec_module(mod_sd)
    
    # Load level_content
    spec_lc = importlib.util.spec_from_file_location(f"{subject_id}_level_content", lc_path)
    mod_lc = importlib.util.module_from_spec(spec_lc)
    spec_lc.loader.exec_module(mod_lc)
    
    stories = getattr(mod_sd, "STORIES", [])
    level_content = getattr(mod_lc, "LEVEL_CONTENT", {})
    
    subject_bundle = {
        "meta": meta,
        "stories": stories,
        "level_content": level_content,
        "stories_by_id": {s["id"]: s for s in stories}
    }
    
    _SUBJECT_CACHE[subject_id] = subject_bundle
    return subject_bundle

def get_case(subject_id: str, case_id: int) -> Optional[Dict[str, Any]]:
    bundle = load_subject_data(subject_id)
    return bundle["stories_by_id"].get(case_id)

def get_case_modules(subject_id: str, case_id: int) -> List[Dict[str, Any]]:
    bundle = load_subject_data(subject_id)
    lc = bundle["level_content"]
    data = lc.get(str(case_id), lc.get(case_id, {}))
    return data.get("episodes", [])
