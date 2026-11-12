"""Image & Video Processing Curriculum: Cases 08 through 15 (Lossy/Wavelets -> Video Coding)."""

CASES_08_15 = {
    "8": {
        "title": "Case 08: Subband Budgets: Lossy Compression, Wavelets & Standards",
        "episodes": [
            {
                "title": "Module 1: Transform Coding & JPEG 8x8 DCT",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Blocky Halos Ruin Low-Bitrate Architectural Blueprints",
                        "text": "High-compression baseline JPEG splits images into independent $8\\times 8$ DCT blocks, causing harsh grid seams and mosquito ringing along sharp blueprint lines.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Understand lossy transform coding (DCT vs. KLT), quantization matrix design, Wavelet subband compression, and JPEG/JPEG-2000 standards.",
                    },
                    {
                        "type": "concept",
                        "title": "JPEG Baseline Pipeline",
                        "content": "1. Level-shift pixel values by $-128$ and partition into $8\\times 8$ blocks.\n2. Apply 2-D **Discrete Cosine Transform (DCT)** — packs energy into top-left low-frequency coefficients.\n3. Divide by psychovisual **Quantization Table** $Q(u,v)$ and round (this is the *lossy* step!).\n4. **Zig-zag scan** orders zeros together -> DPCM on DC + RLE/Huffman on AC coefficients.\n\n**Fidelity Criteria:** Objective MSE, **PSNR** $= 10\\log_{10}(255^2 / \\text{MSE})$ dB, and perceptual SSIM.",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Compute PSNR from Mean-Square Error",
                        "formula": "$$\\text{PSNR} = 10 \\log_{10}\\left(\\frac{255^2}{\\text{MSE}}\\right)\\text{ dB}$$",
                        "problem": "An 8-bit lossy decoder produces an image with $\\text{MSE} = 65.025$ (note $255^2 = 65025$). What is the **PSNR in dB**?",
                        "answer": "30",
                        "alternatives": ["30.0", "30 dB"],
                        "step_by_step": "$$\\text{PSNR} = 10 \\log_{10}(65025 / 65.025) = 10 \\log_{10}(1000) = 30\\text{ dB}.$$",
                    },
                ],
            },
            {
                "title": "Module 2: Wavelets in Image Compression (DWT)",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Multi-Resolution Subband Decomposition (LL, LH, HL, HH)",
                        "content": "Unlike block-based DCT, the **2-D Discrete Wavelet Transform (DWT)** decomposes the entire image across scales without block boundaries:\n- **LL:** Coarse low-pass approximation (recursively decomposed!).\n- **LH / HL:** Horizontal and vertical edge details.\n- **HH:** Diagonal high-frequency details.\n\nWavelet coders (EZW, SPIHT) exploit cross-scale **zero-trees** where insignificant parent coefficients predict zero children.",
                    },
                ],
            },
            {
                "title": "Module 3: Compression Standards Comparison",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "PNG, JBIG2, JPEG vs. JPEG-2000",
                        "content": "- **PNG / TIFF-LZW:** Lossless spatial prediction + Deflate/LZW.\n- **JBIG2:** Bi-level document/fax compression using symbol pattern matching.\n- **JPEG:** $8\\times 8$ DCT + Huffman (fast, universal, blocking at $<0.25$ bpp).\n- **JPEG-2000:** CDF 5/3 (lossless integer) & 9/7 (lossy) Wavelets + EBCOT arithmetic tier coding -> **progressive resolution & quality streaming, zero blocking**.",
                    },
                    {
                        "type": "interactive",
                        "question": "Why does JPEG-2000 eliminate the 8x8 grid blocking artifacts seen in standard JPEG at extreme compression ratios?",
                        "options": [
                            "JPEG-2000 applies a full-frame (or large-tile) Wavelet transform with overlapping basis functions instead of independent 8x8 DCT blocks.",
                            "JPEG-2000 forces every pixel to 1-bit black and white.",
                            "JPEG-2000 stores uncompressed raw RGB pixels.",
                            "JPEG-2000 disables quantization completely.",
                        ],
                        "answer": "JPEG-2000 applies a full-frame (or large-tile) Wavelet transform with overlapping basis functions instead of independent 8x8 DCT blocks.",
                        "explanation": "Full-frame DWT multi-resolution filtering avoids hard $8\\times 8$ block discontinuities.",
                    },
                ],
            },
            {
                "title": "Module 4: 2-D Haar Wavelet & Quantization Lab (Python)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 08: 2-D Haar Wavelet Subband Decomposition & PSNR",
                        "language": "python",
                        "instructions": "Implement `haar_2d_step(block_2x2)` returning `(LL, LH, HL, HH)` normalized by `/2.0` (`(a+b+c+d)/2`, etc. or unnormalized averages `/4.0`? Use orthogonal Haar factor `0.5`: `LL=(a+b+c+d)/2`, `LH=(a+b-c-d)/2`, `HL=(a-b+c-d)/2`, `HH=(a-b-c+d)/2`).",
                        "starter_code": """import numpy as np

def haar_2d_step(b):
    # b is 2x2 float array: a=b[0,0], b1=b[0,1], c=b[1,0], d=b[1,1]
    pass

blk = np.array([[10.0, 10.0], [10.0, 10.0]])
blk2 = np.array([[10.0, 20.0], [10.0, 20.0]])
print("CONST:", haar_2d_step(blk), "VERT_EDGE:", haar_2d_step(blk2))
""",
                        "solution_code": """import numpy as np

def haar_2d_step(b):
    a, b1, c, d = float(b[0, 0]), float(b[0, 1]), float(b[1, 0]), float(b[1, 1])
    ll = (a + b1 + c + d) / 2.0
    lh = (a + b1 - c - d) / 2.0
    hl = (a - b1 + c - d) / 2.0
    hh = (a - b1 - c + d) / 2.0
    return ll, lh, hl, hh

blk = np.array([[10.0, 10.0], [10.0, 10.0]])
blk2 = np.array([[10.0, 20.0], [10.0, 20.0]])
print("CONST:", haar_2d_step(blk), "VERT_EDGE:", haar_2d_step(blk2))
""",
                        "expected_output": "CONST: (20.0, 0.0, 0.0, 0.0) VERT_EDGE: (30.0, 0.0, -10.0, 0.0)",
                    },
                ],
            },
        ],
    },
    "9": {
        "title": "Case 09: Structural Surgery: Binary & Grayscale Morphology",
        "episodes": [
            {
                "title": "Module 1: Erosion, Dilation, Opening & Closing",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "PCB Copper Traces Plagued by Pinholes and Whisker Spurs",
                        "text": "Automated optical inspection detects isolated dust specks on background and tiny pinholes inside copper pads.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Master set-theoretic Morphology: Dilation, Erosion, Opening/Closing duality, Hit-or-Miss, structural algorithms, and Grayscale Top-Hat extensions.",
                    },
                    {
                        "type": "concept",
                        "title": "Morphological Primitives with Structuring Element B",
                        "content": "- **Erosion ($A \\ominus B$):** Set of origins $z$ where $(B)_z \\subseteq A$. Shrinks objects, eliminates thin bridges and isolated small noise specks.\n- **Dilation ($A \\oplus B$):** Set of origins $z$ where $(\\hat{B})_z \\cap A \\ne \\emptyset$. Grows objects, bridges small gaps.\n- **Opening ($A \\circ B = (A \\ominus B) \\oplus B$):** Smooths contours, breaks narrow isthmuses, deletes thin protrusions.\n- **Closing ($A \\bullet B = (A \\oplus B) \\ominus B$):** Fuses narrow breaks, fills small internal holes.",
                    },
                    {
                        "type": "interactive",
                        "question": "Which morphological operation removes small isolated white noise specks on a dark background WITHOUT shrinking the overall area of large foreground blobs?",
                        "options": [
                            "Opening (Erosion followed by Dilation)",
                            "Closing (Dilation followed by Erosion)",
                            "Pure Dilation",
                            "Image Negation",
                        ],
                        "answer": "Opening (Erosion followed by Dilation)",
                        "explanation": "Erosion erases specks smaller than the structuring element; Dilation then restores the surviving large foreground blobs back to their original scale.",
                    },
                ],
            },
            {
                "title": "Module 2: Basic Morphological Algorithms",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Hit-or-Miss, Boundary Extraction, Hole Filling & Skeletons",
                        "content": "- **Hit-or-Miss ($A \\circledast B$):** Uses foreground SE $B_1$ and background SE $B_2$ to locate exact local shape patterns (e.g., endpoints, corners).\n- **Boundary Extraction:** $\\beta(A) = A - (A \\ominus B)$.\n- **Region / Hole Filling:** Iterative conditional dilation inside $A^c$: $X_k = (X_{k-1} \\oplus B) \\cap A^c$.\n- **Connected Components, Convex Hull, Thinning & Skeletons:** Medial-axis descriptors built recursively via erosions and openings.",
                    },
                ],
            },
            {
                "title": "Module 3: Extension to Grayscale Morphology",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Grayscale Dilation/Erosion & Top-Hat Illumination Correction",
                        "content": "Replacing binary set intersection/containment with local neighborhood extrema over flat structuring element $b$:\n- **Grayscale Dilation:** $(f \\oplus b)(x,y) = \\max_{(s,t)\\in b}\\{f(x-s, y-t)\\}$ (brightens & expands bright peaks).\n- **Grayscale Erosion:** $(f \\ominus b)(x,y) = \\min_{(s,t)\\in b}\\{f(x+s, y+t)\\}$ (darkens & shrinks bright peaks).\n- **Morphological Gradient:** $(f \\oplus b) - (f \\ominus b)$ highlights edges.\n- **White Top-Hat ($f - (f \\circ b)$):** Extracts bright objects smaller than $b$ while subtracting uneven slow background shading!",
                    },
                ],
            },
            {
                "title": "Module 4: Morphological Boundary & Grayscale Top-Hat Lab (Python)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 09: Binary Boundary Extraction & Grayscale Top-Hat",
                        "language": "python",
                        "instructions": "Implement `erode_3x3(img)` (min filter over 3x3 with edge pad), `dilate_3x3(img)` (max filter), `boundary_extract(bin_img)` ($A - (A \\ominus B)$), and `top_hat_3x3(gray_img)` ($f - \\text{dilate}(\\text{erode}(f))$).",
                        "starter_code": """import numpy as np

def erode_3x3(img):
    # Return 3x3 min over padded image
    pass

def dilate_3x3(img):
    # Return 3x3 max over padded image
    pass

def boundary_extract(bin_img):
    return bin_img - erode_3x3(bin_img)

def top_hat_3x3(gray_img):
    opened = dilate_3x3(erode_3x3(gray_img))
    return gray_img - opened

box = np.zeros((5, 5), dtype=np.int32)
box[1:4, 1:4] = 1
bnd = boundary_extract(box)
gray = np.array([[10, 10, 10], [10, 80, 10], [10, 10, 10]], dtype=np.int32)
th = top_hat_3x3(gray)
print(f"BND_SUM={int(bnd.sum())}, TOPHAT_CENTER={int(th[1, 1])}")
""",
                        "solution_code": """import numpy as np

def erode_3x3(img):
    p = np.pad(img, 1, mode="edge")
    out = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            out[i, j] = np.min(p[i:i+3, j:j+3])
    return out

def dilate_3x3(img):
    p = np.pad(img, 1, mode="edge")
    out = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            out[i, j] = np.max(p[i:i+3, j:j+3])
    return out

def boundary_extract(bin_img):
    return bin_img - erode_3x3(bin_img)

def top_hat_3x3(gray_img):
    opened = dilate_3x3(erode_3x3(gray_img))
    return gray_img - opened

box = np.zeros((5, 5), dtype=np.int32)
box[1:4, 1:4] = 1
bnd = boundary_extract(box)
gray = np.array([[10, 10, 10], [10, 80, 10], [10, 10, 10]], dtype=np.int32)
th = top_hat_3x3(gray)
print(f"BND_SUM={int(bnd.sum())}, TOPHAT_CENTER={int(th[1, 1])}")
""",
                        "expected_output": "BND_SUM=8, TOPHAT_CENTER=70",
                    },
                ],
            },
        ],
    },
    "10": {
        "title": "Case 10: Contours & Cuts: Edge Linking, Hough & Thresholding",
        "episodes": [
            {
                "title": "Module 1: Discontinuity Detection & Canny Edge Detector",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Broken Highway Lane Markings Defeat Naive Edge Masks",
                        "text": "Shadows and worn asphalt break lane lines into fragmented dots under a raw Sobel threshold.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Detect points, lines, and edges (Sobel, LoG, Canny), link discontinuous edges via Hough Transform, and compute optimal Otsu & Adaptive thresholds.",
                    },
                    {
                        "type": "concept",
                        "title": "Canny Pipeline: NMS & Hysteresis",
                        "content": "1. **Gaussian Smoothing** suppresses high-frequency noise.\n2. **Gradient Magnitude & Orientation** (Sobel).\n3. **Non-Maximum Suppression (NMS):** Thins broad gradient ridges down to **1-pixel-wide contours** by zeroing non-peak neighbors along the gradient normal.\n4. **Hysteresis (Double) Thresholding:** Uses $T_{\\text{high}}$ (strong edges) and $T_{\\text{low}}$ (weak edges kept *only* if 8-connected to a strong edge).",
                    },
                ],
            },
            {
                "title": "Module 2: Edge Linking & The Hough Transform",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Polar Line Parameterization (rho, theta)",
                        "content": "To avoid infinite slopes $m \\to \\infty$ for vertical lines in $y = mx + b$, the **Hough Transform** maps every edge pixel $(x_i, y_i)$ to a sinusoidal curve in $(\\rho, \\theta)$ accumulator space:\n$$x \\cos\\theta + y \\sin\\theta = \\rho$$\nCollinear edge points — even with huge gaps or occlusions — intersect at the exact same accumulator bin $(\\rho^*, \\theta^*)$, robustly linking broken lines!",
                    },
                ],
            },
            {
                "title": "Module 3: Optimal Global (Otsu) & Adaptive Thresholding",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Otsu's Between-Class Variance Maximization",
                        "content": "Instead of manual trial-and-error, **Otsu's Method** picks threshold $k^*$ maximizing between-class variance $\\sigma_B^2(k)$ between background $C_1$ (prob $P_1$, mean $m_1$) and foreground $C_2$ (prob $P_2$, mean $m_2$):\n$$\\sigma_B^2(k) = P_1(k) P_2(k) [m_1(k) - m_2(k)]^2$$\nWhen illumination slopes unevenly across the frame, **Adaptive / Local Thresholding** computes $T(x,y) = a \\cdot \\sigma_{xy} + b \\cdot m_{xy}$ per neighborhood.",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Compute Otsu Between-Class Variance",
                        "formula": "$$\\sigma_B^2 = P_1 P_2 (m_1 - m_2)^2$$",
                        "problem": "At candidate threshold $k$, background has $P_1 = 0.5, m_1 = 20$ and foreground has $P_2 = 0.5, m_2 = 60$. What is $\\sigma_B^2$?",
                        "answer": "400",
                        "alternatives": ["400.0"],
                        "step_by_step": "$$\\sigma_B^2 = 0.5 \\times 0.5 \\times (20 - 60)^2 = 0.25 \\times 1600 = 400.$$",
                    },
                ],
            },
            {
                "title": "Module 4: Otsu Thresholding & Hough Vote Lab (Python)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 10: Otsu Threshold Optimizer & Hough Line Accumulator",
                        "language": "python",
                        "instructions": "Implement `otsu_between_var(vals, t)` returning $\\sigma_B^2$ for threshold `t` (`<= t` vs `> t`), and `hough_rho(x, y, theta_deg)` returning `round(x*cos + y*sin, 3)`.",
                        "starter_code": """import numpy as np
import math

def otsu_between_var(vals, t):
    # Compute P1*P2*(m1-m2)^2 for vals <= t vs vals > t
    pass

def hough_rho(x, y, theta_deg):
    rad = math.radians(theta_deg)
    return round(x * math.cos(rad) + y * math.sin(rad), 3)

arr = np.array([10, 20, 30, 190, 200, 210], dtype=np.float64)
v_good = round(otsu_between_var(arr, 100), 1)
v_bad = round(otsu_between_var(arr, 15), 1)
print(f"VAR_100={v_good}, VAR_15={v_bad}, RHO={hough_rho(3, 4, 0)}")
""",
                        "solution_code": """import numpy as np
import math

def otsu_between_var(vals, t):
    c1 = vals[vals <= t]
    c2 = vals[vals > t]
    if len(c1) == 0 or len(c2) == 0:
        return 0.0
    p1 = len(c1) / len(vals)
    p2 = len(c2) / len(vals)
    return float(p1 * p2 * ((c1.mean() - c2.mean()) ** 2))

def hough_rho(x, y, theta_deg):
    rad = math.radians(theta_deg)
    return round(x * math.cos(rad) + y * math.sin(rad), 3)

arr = np.array([10, 20, 30, 190, 200, 210], dtype=np.float64)
v_good = round(otsu_between_var(arr, 100), 1)
v_bad = round(otsu_between_var(arr, 15), 1)
print(f"VAR_100={v_good}, VAR_15={v_bad}, RHO={hough_rho(3, 4, 0)}")
""",
                        "expected_output": "VAR_100=8100.0, VAR_15=2000.0, RHO=3.0",
                    },
                ],
            },
        ],
    },
    "11": {
        "title": "Case 11: Regions & Invariants: Watersheds, Chains & Moments",
        "episodes": [
            {
                "title": "Module 1: Region-Oriented & Motion-Based Segmentation",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Touching Biological Cells Must Be Separated & Measured",
                        "text": "Clustered cells fuse into one blob under thresholding, while rotated samples fool raw pixel templates.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Master Region Growing, Quadtree Split-and-Merge, Watersheds, Motion-based segmentation, Boundary Representations, and Rotation/Scale-Invariant Descriptors.",
                    },
                    {
                        "type": "concept",
                        "title": "Region Growing, Split/Merge, Watersheds & Motion",
                        "content": "- **Region Growing:** Expands from seed pixels by appending 8-connected neighbors satisfying a homogeneity predicate $P(R)$.\n- **Split-and-Merge (Quadtrees):** Recursively splits non-uniform quadrants into 4, then merges adjacent similar quadrants.\n- **Morphological Watersheds:** Treats gradient magnitude as a topographic surface; flooding from regional minima builds **watershed dam lines** cleanly splitting touching objects!\n- **Motion-Based Segmentation:** Accumulative Difference Images (ADI) $A(x,y)$ count frames where $|f(x,y,t) - r(x,y)| > T$ to separate moving foregrounds from static backgrounds.",
                    },
                ],
            },
            {
                "title": "Module 2: Representation Schemes (Chain Codes & Polygons)",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Freeman Chain Codes & First Differences",
                        "content": "- **Freeman 4/8-Directional Chain Code:** Represents a closed boundary by directional step codes ($0..7$).\n- **Starting-Point & Rotation Normalization:** Cyclic shift to the **minimum-magnitude integer** normalizes the start point; taking the **first difference** (modulo 4 or 8) makes the code **rotation invariant**!\n- **Other Schemes:** Minimum-perimeter polygonal approximation, 1-D radial **Signatures** $r(\\theta)$, and Medial-Axis Skeletons.",
                    },
                ],
            },
            {
                "title": "Module 3: Boundary & Regional Descriptors (Fourier & Hu Moments)",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Fourier Descriptors & Hu's 7 Moment Invariants",
                        "content": "- **Boundary Descriptors:** Length, diameter, eccentricity, **Fourier Descriptors** (1-D DFT of complex boundary coordinates $s(k) = x_k + j y_k$: discarding high $u$ smooths contours; magnitude normalization grants translation/scale/rotation invariance).\n- **Regional Descriptors:** Area $A$, Perimeter $P$, **Compactness** $= P^2 / A$ (minimized at $4\\pi$ for a circle), Euler number ($V - Q + F$ / Holes), GLCM texture contrast/entropy, and **Hu's 7 Central Moments** $\\phi_1..\\phi_7$ (invariant to translation, scale, and rotation!).",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Scale-Invariant Circle Compactness",
                        "formula": "$$\\text{Compactness} = \\frac{P^2}{A}$$",
                        "problem": "For an ideal continuous circle of radius $r$, what is its exact **Compactness** $\\frac{P^2}{A}$ rounded to the nearest integer (use $\\pi \\approx 3.14159$, $4\\pi \\approx 12.566$)?",
                        "answer": "13",
                        "alternatives": ["12.57", "12.566", "4pi"],
                        "step_by_step": "$$P = 2\\pi r, \\quad A = \\pi r^2 \\implies \\frac{P^2}{A} = \\frac{4\\pi^2 r^2}{\\pi r^2} = 4\\pi \\approx 12.57 \\to 13.$$",
                    },
                ],
            },
            {
                "title": "Module 4: Region Growing & First-Difference Chain Code Lab (Python)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 11: 4-Connected Region Growing & Rotation-Invariant Chain Diff",
                        "language": "python",
                        "instructions": "Implement `chain_first_diff_4(code)` computing modulo-4 circular differences `(code[(i+1)%n] - code[i]) % 4` and `region_grow_4(img, seed, tol)` returning count of pixels in the grown region.",
                        "starter_code": """import numpy as np
from collections import deque

def chain_first_diff_4(code):
    # Return circular first difference modulo 4
    pass

def region_grow_4(img, seed, tol):
    # BFS from seed=(r,c) including 4-neighbors with abs(val - seed_val) <= tol
    pass

grid = np.array([[10, 12, 90], [11, 13, 95], [80, 85, 92]], dtype=np.int32)
cnt = region_grow_4(grid, (0, 0), tol=4)
diff = chain_first_diff_4([0, 1, 2, 3])
print(f"GROWN={cnt}, DIFF={diff}")
""",
                        "solution_code": """import numpy as np
from collections import deque

def chain_first_diff_4(code):
    n = len(code)
    return [(code[(i + 1) % n] - code[i]) % 4 for i in range(n)]

def region_grow_4(img, seed, tol):
    h, w = img.shape
    sr, sc = seed
    ref = int(img[sr, sc])
    visited = {(sr, sc)}
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and (nr, nc) not in visited:
                if abs(int(img[nr, nc]) - ref) <= tol:
                    visited.add((nr, nc))
                    q.append((nr, nc))
    return len(visited)

grid = np.array([[10, 12, 90], [11, 13, 95], [80, 85, 92]], dtype=np.int32)
cnt = region_grow_4(grid, (0, 0), tol=4)
diff = chain_first_diff_4([0, 1, 2, 3])
print(f"GROWN={cnt}, DIFF={diff}")
""",
                        "expected_output": "GROWN=4, DIFF=[1, 1, 1, 1]",
                    },
                ],
            },
        ],
    },
    "12": {
        "title": "Case 12: Pattern Classifier: Statistical & Structural Recognition",
        "episodes": [
            {
                "title": "Module 1: Patterns, Pattern Classes & Minimum-Distance Classifier",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Silicon Wafer Defects Need Automated Classification",
                        "text": "Segmented die defects extract regional descriptors $[x_1, x_2]^T$ (compactness, aspect ratio) that must be assigned accurately to pattern classes.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Formulate Pattern Classes, implement Decision-Theoretic classifiers (Minimum-Distance, Correlation, Bayes Gaussian), and build Structural String/Grammar recognizers.",
                    },
                    {
                        "type": "concept",
                        "title": "Decision-Theoretic Pattern Vectors",
                        "content": "An object is represented as a $n$-D feature vector $\\mathbf{x} = [x_1, x_2, \\dots, x_n]^T$ belonging to one of $W$ pattern classes $\\omega_1, \\dots, \\omega_W$.\n- **Minimum-Distance Classifier:** Assigns $\\mathbf{x}$ to class $\\omega_j$ minimizing Euclidean distance to class prototype mean $\\mathbf{m}_j$, equivalent to maximizing linear decision function: $$d_j(\\mathbf{x}) = \\mathbf{x}^T \\mathbf{m}_j - \\frac{1}{2} \\mathbf{m}_j^T \\mathbf{m}_j$$\n- **Template Matching (Normalized Correlation):** Slides prototype subimage $w$ over $f$, invariant to linear brightness scaling.",
                    },
                ],
            },
            {
                "title": "Module 2: Bayes Statistical Classifier for Gaussian Classes",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Minimizing Expected Loss via Bayes Rule",
                        "content": "Using prior probabilities $P(\\omega_j)$ and class-conditional PDFs $p(\\mathbf{x}|\\omega_j)$, **Bayes Classifier** maximizes $P(\\omega_j) p(\\mathbf{x}|\\omega_j)$.\nFor multivariate Gaussian classes $\\mathcal{N}(\\mathbf{m}_j, \\mathbf{C}_j)$:\n$$d_j(\\mathbf{x}) = \\ln P(\\omega_j) - \\frac{1}{2}\\ln|\\mathbf{C}_j| - \\frac{1}{2}(\\mathbf{x} - \\mathbf{m}_j)^T \\mathbf{C}_j^{-1} (\\mathbf{x} - \\mathbf{m}_j)$$\nNotice: when $\\mathbf{C}_j = \\sigma^2 \\mathbf{I}$ and priors are equal, Bayes reduces *identically* to the Minimum-Distance classifier!",
                    },
                ],
            },
            {
                "title": "Module 3: Structural Methods — Strings & Syntactic Grammars",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Recognizing Primitives by Relationships, Not Just Numbers",
                        "content": "When geometric structure matters more than scalar size:\n- **String Matching:** Encodes boundary segments as symbol strings $a = a_1 \\dots a_n$ and $b = b_1 \\dots b_m$. Similarity measure $R = \\frac{M}{\\max(|a|, |b|) - M}$ where $M$ is exact aligned character matches.\n- **Syntactic (Formal Grammar) Recognition:** Defines primitives (terminals $\\Sigma$) and production rules $G = (N, \\Sigma, P, S)$ — e.g. parsing staircase/ladder contours via a context-free grammar.",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Structural String Matching Ratio",
                        "formula": "$$R = \\frac{M}{\\max(|a|, |b|) - M}$$",
                        "problem": "Two contour strings `a = \"abcde\"` and `b = \"abxde\"` (length 5 each) match at $M = 4$ positions. What is the similarity ratio $R$?",
                        "answer": "4",
                        "alternatives": ["4.0"],
                        "step_by_step": "$$R = \\frac{4}{5 - 4} = 4.0.$$ (Perfect match yields $R \\to \\infty$; zero match yields $R = 0$.)",
                    },
                ],
            },
            {
                "title": "Module 4: Minimum-Distance & String Matcher Lab (Python)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 12: Linear Discriminant Minimum-Distance & Structural Matcher",
                        "language": "python",
                        "instructions": "Implement `min_dist_predict(x, means)` returning index of class maximizing $x^T m_j - 0.5 m_j^T m_j$, and `string_similarity(a, b)` computing $M / (\\max(|a|,|b|) - M)$ (return `float('inf')` if denominator is 0).",
                        "starter_code": """import numpy as np

def min_dist_predict(x, means):
    # Return argmax_j (x.T @ m_j - 0.5 * m_j.T @ m_j)
    pass

def string_similarity(a, b):
    # Count positional matches M, return M / (max(len(a), len(b)) - M)
    pass

means = [np.array([0.0, 0.0]), np.array([10.0, 10.0])]
pred = min_dist_predict(np.array([8.0, 7.0]), means)
sim = round(string_similarity("aabbcc", "aabxcc"), 2)
print(f"CLASS={pred}, SIM={sim}")
""",
                        "solution_code": """import numpy as np

def min_dist_predict(x, means):
    scores = [float(np.dot(x, m) - 0.5 * np.dot(m, m)) for m in means]
    return int(np.argmax(scores))

def string_similarity(a, b):
    m = sum(1 for ca, cb in zip(a, b) if ca == cb)
    den = max(len(a), len(b)) - m
    return float("inf") if den == 0 else m / den

means = [np.array([0.0, 0.0]), np.array([10.0, 10.0])]
pred = min_dist_predict(np.array([8.0, 7.0]), means)
sim = round(string_similarity("aabbcc", "aabxcc"), 2)
print(f"CLASS={pred}, SIM={sim}")
""",
                        "expected_output": "CLASS=1, SIM=5.0",
                    },
                ],
            },
        ],
    },
    "13": {
        "title": "Case 13: Spatiotemporal Flow: Video Sampling & Motion Estimation",
        "episodes": [
            {
                "title": "Module 1: Video Formation, 3-D Sampling & Video Modeling",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "30fps Surveillance Makes Rotating Turbine Blades Spin Backward",
                        "text": "A 30 Hz camera captures a turbine spinning at 28 revolutions/second, creating an apparent slow backward rotation (temporal aliasing!).",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Master 3-D video sampling $(x, y, t)$, interlaced vs. progressive capture, Brightness Constancy, and 2-D/3-D Motion Estimation (Block Matching & Optical Flow).",
                    },
                    {
                        "type": "concept",
                        "title": "Video Formation, Sampling & Brightness Constancy",
                        "content": "A digital video is a 3-D sampled signal $f(x, y, t)$:\n- **Progressive vs. Interlaced:** Progressive scans all lines per frame ($30p$); Interlaced alternates odd/even fields ($60i$) to halve transmission bandwidth at the cost of comb artifacts on fast motion.\n- **Temporal Aliasing:** Occurs when object temporal frequency exceeds $f_s / 2$ (Wagon-Wheel effect).\n- **Optical Flow Equation (Brightness Constancy):** Assuming pixel intensity stays constant over small $(\\Delta x, \\Delta y, \\Delta t)$: $$I_x u + I_y v + I_t = 0$$ where $(u, v)$ is optical flow velocity.",
                    },
                ],
            },
            {
                "title": "Module 2: Aperture Problem & Lucas-Kanade Optical Flow",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Solving 1 Equation with 2 Unknowns (u, v)",
                        "content": "A single pixel gives only **1 constraint** $I_x u + I_y v = -I_t$ for **2 unknowns** $(u, v)$ — only motion normal to an edge is observable locally (**Aperture Problem**).\n- **Lucas-Kanade:** Assumes constant $(u, v)$ inside a local $W\\times W$ patch -> solves an overdetermined least-squares system $(\\mathbf{A}^T \\mathbf{A}) \\mathbf{v} = -\\mathbf{A}^T \\mathbf{b}$ (requires 2-D corners where $\\mathbf{A}^T \\mathbf{A}$ is invertible!).\n- **Horn-Schunck:** Adds a global spatial smoothness penalty $\\lambda(\\|\\nabla u\\|^2 + \\|\\nabla v\\|^2)$.",
                    },
                ],
            },
            {
                "title": "Module 3: 2-D Block Matching (SAD) & 3-D Motion Models",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Block-Matching Motion Estimation & 3-D Camera Motion",
                        "content": "Video encoders divide each frame into $N\\times N$ macroblocks (e.g. $16\\times 16$) and search a reference window $\\pm p$ for the displacement vector $(dx, dy)$ minimizing **Sum of Absolute Differences (SAD)**:\n$$\\text{SAD}(dx, dy) = \\sum_{i=0}^{N-1}\\sum_{j=0}^{N-1} |f_t(x+i, y+j) - f_{t-1}(x+i+dx, y+j+dy)|$$\nFast search algorithms (**Three-Step Search**, **Diamond Search**) cut search points from $(2p+1)^2$ by $>10\\times$. **3-D Motion Estimation** models rigid 6-DOF camera rotation/translation projecting to 2-D affine/perspective flow.",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Full-Search vs. Search Window Complexity",
                        "formula": "$$\\text{Candidates} = (2p + 1)^2$$",
                        "problem": "For a search range of $p = \\pm 7$ pixels around a macroblock, how many candidate positions must **Full Search** evaluate per block?",
                        "answer": "225",
                        "alternatives": ["225.0"],
                        "step_by_step": "$$(2 \\times 7 + 1)^2 = 15^2 = 225\\text{ block SAD comparisons}.$$",
                    },
                ],
            },
            {
                "title": "Module 4: Block-Matching Motion Vector Estimator (Python Lab)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 13: Full-Search SAD Motion Vector Finder",
                        "language": "python",
                        "instructions": "Implement `find_motion_vector(cur_blk, ref_frame, bx, by, search_r)` scanning `dx, dy in range(-search_r, search_r + 1)` within bounds and returning `(best_dx, best_dy, min_sad)`.",
                        "starter_code": """import numpy as np

def find_motion_vector(cur_blk, ref_frame, bx, by, search_r):
    # Return (best_dx, best_dy, min_sad)
    pass

ref = np.zeros((8, 8), dtype=np.int32)
ref[4:6, 5:7] = 100
cur_blk = np.ones((2, 2), dtype=np.int32) * 100
dx, dy, sad = find_motion_vector(cur_blk, ref, bx=3, by=3, search_r=2)
print(f"MV=({dx},{dy}), SAD={sad}")
""",
                        "solution_code": """import numpy as np

def find_motion_vector(cur_blk, ref_frame, bx, by, search_r):
    bh, bw = cur_blk.shape
    H, W = ref_frame.shape
    best_sad = 10**12
    best_mv = (0, 0)
    for dy in range(-search_r, search_r + 1):
        for dx in range(-search_r, search_r + 1):
            ry, rx = by + dy, bx + dx
            if 0 <= ry and ry + bh <= H and 0 <= rx and rx + bw <= W:
                sad = int(np.sum(np.abs(cur_blk - ref_frame[ry:ry+bh, rx:rx+bw])))
                if sad < best_sad:
                    best_sad = sad
                    best_mv = (dx, dy)
    return best_mv[0], best_mv[1], best_sad

ref = np.zeros((8, 8), dtype=np.int32)
ref[4:6, 5:7] = 100
cur_blk = np.ones((2, 2), dtype=np.int32) * 100
dx, dy, sad = find_motion_vector(cur_blk, ref, bx=3, by=3, search_r=2)
print(f"MV=({dx},{dy}), SAD={sad}")
""",
                        "expected_output": "MV=(2,1), SAD=0",
                    },
                ],
            },
        ],
    },
    "14": {
        "title": "Case 14: Temporal Repair: MC Filtering, Deinterlacing & Watermarking",
        "episodes": [
            {
                "title": "Module 1: Motion-Compensated (MC) Temporal Filtering",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Naive Temporal Averaging Leaves Ghost Trails Behind Moving Cars",
                        "text": "Averaging adjacent noisy surveillance frames blurs fast vehicles into transparent ghosts, while interlaced broadcasts show horizontal sawtooth combing.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Design Motion-Compensated (MC) temporal noise filters, Deinterlacing pipelines, Frame-Rate Conversion (FRC), and robust DCT Video Watermarking.",
                    },
                    {
                        "type": "concept",
                        "title": "Filtering Along Motion Trajectories",
                        "content": "**MC Temporal Filtering** warps reference frame $f_{t-1}$ using estimated motion vector $(dx, dy)$ before averaging: $$\\hat{f}_t(x,y) = (1 - \\alpha) f_t(x,y) + \\alpha \\cdot f_{t-1}(x - dx, y - dy)$$\nAdaptive $\\alpha$ drops toward $0$ when MC residual $|f_t - f_{t-1}^{\\text{MC}}|$ is high (occlusion/scene cut), eliminating ghosting!",
                    },
                ],
            },
            {
                "title": "Module 2: Deinterlacing & Frame-Rate Conversion (FRC)",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Bob, Weave, MC Deinterlacing & 3:2 Pulldown",
                        "content": "- **Weave:** Combines odd + even fields directly -> razor-sharp on static scenes, **sawtooth combing** on motion.\n- **Bob:** Interpolates missing lines within a single field -> zero combing, halved vertical detail.\n- **Motion-Adaptive / MC Deinterlacing:** Uses Weave on static blocks and MC interpolation along motion vectors on moving blocks.\n- **Frame-Rate Conversion:** Converting 24fps film to 60i TV uses **3:2 Pulldown** (alternating 3 and 2 field repeats, causing telecine judder); modern 120Hz TVs synthesize intermediate frames via **Bidirectional MC Frame Interpolation**.",
                    },
                ],
            },
            {
                "title": "Module 3: Video Watermarking",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Imperceptible & Recompression-Resilient Ownership Marks",
                        "content": "Video watermarks balance **Imperceptibility**, **Payload**, and **Robustness** against lossy re-encoding, cropping, and temporal frame dropping:\n- **Spatial LSB:** Fragile — wiped out instantly by JPEG/MPEG quantization.\n- **Mid-Band DCT / DWT Spread-Spectrum:** Modulates mid-frequency DCT coefficients $C(u,v) + \\alpha \\cdot w_i$ (low frequencies cause visible flicker; high frequencies get quantized to zero!).",
                    },
                    {
                        "type": "interactive",
                        "question": "Why are mid-band DCT coefficients preferred over high-frequency DCT coefficients for robust video watermarking?",
                        "options": [
                            "Quantization tables in MPEG/H.264 aggressively zero out high frequencies, whereas mid-band coefficients survive lossy compression while remaining visually masked.",
                            "High frequencies cannot be computed with FFT/DCT.",
                            "Mid-band coefficients are stored in the file header outside the video stream.",
                            "High frequencies cause the video frame rate to drop by half.",
                        ],
                        "answer": "Quantization tables in MPEG/H.264 aggressively zero out high frequencies, whereas mid-band coefficients survive lossy compression while remaining visually masked.",
                        "explanation": "Low frequencies risk visible luminance flicker; high frequencies are discarded by quantizers. Mid-band coefficients strike the optimal robustness/imperceptibility balance.",
                    },
                ],
            },
            {
                "title": "Module 4: MC Temporal Filter & DCT Watermark Lab (Python)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 14: Motion-Compensated Denoiser & Correlation Watermark Detector",
                        "language": "python",
                        "instructions": "Implement `mc_temporal_blend(cur_val, ref_mc_val, alpha)` and `embed_extract_watermark(coeffs, wm_bits, alpha)` embedding `+alpha*b` ($b \\in \\{-1, +1\\}$) and recovering sign via correlation.",
                        "starter_code": """import numpy as np

def mc_temporal_blend(cur_val, ref_mc_val, alpha=0.5):
    return (1.0 - alpha) * cur_val + alpha * ref_mc_val

def embed_extract_watermark(coeffs, wm_bits, alpha=5.0):
    # Add alpha * wm_bits to coeffs, simulate quantization noise by rounding, return recovered signs (+1/-1)
    pass

blended = round(mc_temporal_blend(102.0, 98.0, 0.5), 1)
c = np.array([20.0, 15.0, -10.0, 5.0])
wm = np.array([1.0, -1.0, 1.0, -1.0])
rec = embed_extract_watermark(c, wm, alpha=6.0)
print(f"BLEND={blended}, WM_MATCH={bool(np.array_equal(rec, wm))}")
""",
                        "solution_code": """import numpy as np

def mc_temporal_blend(cur_val, ref_mc_val, alpha=0.5):
    return (1.0 - alpha) * cur_val + alpha * ref_mc_val

def embed_extract_watermark(coeffs, wm_bits, alpha=5.0):
    watermarked = np.round(coeffs + alpha * wm_bits)
    diff = watermarked - coeffs
    return np.where(diff >= 0, 1.0, -1.0)

blended = round(mc_temporal_blend(102.0, 98.0, 0.5), 1)
c = np.array([20.0, 15.0, -10.0, 5.0])
wm = np.array([1.0, -1.0, 1.0, -1.0])
rec = embed_extract_watermark(c, wm, alpha=6.0)
print(f"BLEND={blended}, WM_MATCH={bool(np.array_equal(rec, wm))}")
""",
                        "expected_output": "BLEND=100.0, WM_MATCH=True",
                    },
                ],
            },
        ],
    },
    "15": {
        "title": "Case 15: Streaming Wire: MPEG-1/2, SVC, MPEG-4 & Error Control",
        "episodes": [
            {
                "title": "Module 1: Hybrid Video Coding (I, P, B Frames) & MPEG-1/2",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "One Dropped UDP Packet Corrupts 15 Consecutive Live Frames",
                        "text": "During a live sports broadcast over lossy wireless links, losing a single P-frame slices a green smear forward across the entire Group of Pictures (GOP).",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Master I/P/B frame-based compression (MPEG-1/2), Scalable Video Coding (SVC), Object-based MPEG-4 VOPs, and Video Error Control/Concealment.",
                    },
                    {
                        "type": "concept",
                        "title": "Frame-Based Hybrid MC-DCT & MPEG-1/2",
                        "content": "- **I-Frames (Intra):** Coded independently like JPEG; provides random-access seek points and stops temporal error propagation.\n- **P-Frames (Predicted):** Forward motion-compensated prediction from prior I/P frame + DCT of residual error.\n- **B-Frames (Bidirectional):** Interpolated from both past & future I/P frames (highest compression, requires **reordered decode order** before display!).\n- **MPEG-1 vs. MPEG-2:** MPEG-1 targeted progressive VCD (~1.5 Mbps); MPEG-2 added interlaced field/frame DCT, broadcast HDTV profiles, and Transport Streams.",
                    },
                    {
                        "type": "visual",
                        "title": "Closed GOP Prediction Dependencies (I-B-B-P)",
                        "code": """flowchart LR
    I0["I0 (Anchor)"] --> P3["P3 (Forward)"]
    I0 --> B1["B1"]
    P3 --> B1
    I0 --> B2["B2"]
    P3 --> B2""",
                    },
                ],
            },
            {
                "title": "Module 2: Scalable (SVC) & Object-Based (MPEG-4) Compression",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Layered Bitstreams & Video Object Planes (VOPs)",
                        "content": "- **Scalable / Layered Coding (SVC):** Encodes one **Base Layer** (guaranteed minimum quality/resolution/fps) plus **Enhancement Layers** along three axes:\n  1. **Temporal Scalability** (hierarchical B-frames: 15 -> 30 -> 60 fps).\n  2. **Spatial Scalability** (720p base + 1080p/4K residual).\n  3. **SNR / Quality Scalability** (coarse QP base + fine quantization refinement).\n- **Object-Based Compression (MPEG-4):** Decomposes scenes into arbitrary-shaped **Video Object Planes (VOPs)** — separately coding binary shape masks (CAE), texture (shape-adaptive DCT), and background **Sprites**.",
                    },
                ],
            },
            {
                "title": "Module 3: Error Control in Video Communications",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Resilience, Transport FEC/ARQ & Decoder Error Concealment",
                        "content": "1. **Error Resilience (Encoder):** Slice **Resynchronization Markers** limit variable-length code desync; **Data Partitioning** separates critical motion vectors from less-critical DCT textures; **RVLC** decodes both forward and backward.\n2. **Channel Control:** Forward Error Correction (**FEC**) vs. **ARQ** retransmission (bounded by live latency!).\n3. **Error Concealment (Decoder):** Replaces lost macroblocks via **Spatial interpolation** (boundary blending) or **Temporal MV Copy** (copying blocks from the previous frame along neighboring motion vectors).",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "GOP Error Propagation Bound",
                        "formula": "$$\\text{Max Affected Frames in } N\\text{-frame Closed GOP} = N - 1$$",
                        "problem": "A 30fps stream uses a Closed GOP of length $N = 15$ (`I P P ... P`). If the **first P-frame** right after `I0` is corrupted and no Intra refresh occurs until the next GOP, how many **P-frames** (including that first one) suffer drift in this GOP?",
                        "answer": "14",
                        "alternatives": ["14.0"],
                        "step_by_step": "The GOP has $1$ I-frame and $14$ P-frames. Because every subsequent P-frame predicts from the previous one, all $14$ P-frames drift until the next I-frame resets prediction.",
                    },
                ],
            },
            {
                "title": "Module 4: Hybrid P-Frame Residual & Temporal Error Concealment Lab (Python)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 15: P-Frame Motion Residual Coder & Temporal MV Concealment",
                        "language": "python",
                        "instructions": "Implement `p_frame_encode_residual(cur_blk, ref_blk)` returning `cur_blk - ref_blk`, `p_frame_decode(ref_blk, residual)`, and `conceal_lost_block(ref_frame, rx, ry, bw, bh)` copying the displaced block from `ref_frame`.",
                        "starter_code": """import numpy as np

def p_frame_encode_residual(cur_blk, ref_blk):
    return cur_blk - ref_blk

def p_frame_decode(ref_blk, residual):
    return ref_blk + residual

def conceal_lost_block(ref_frame, rx, ry, bw, bh):
    # Return copy of ref_frame[ry:ry+bh, rx:rx+bw]
    pass

ref = np.array([[50, 52, 54], [51, 53, 55], [52, 54, 56]], dtype=np.int32)
cur = np.array([[50, 53], [51, 55]], dtype=np.int32)
res = p_frame_encode_residual(cur, ref[:2, :2])
rec = p_frame_decode(ref[:2, :2], res)
concealed = conceal_lost_block(ref, 1, 1, 2, 2)
print(f"RES_SUM={int(np.sum(np.abs(res)))}, EXACT={bool(np.array_equal(rec, cur))}, CONCEAL_TL={int(concealed[0,0])}")
""",
                        "solution_code": """import numpy as np

def p_frame_encode_residual(cur_blk, ref_blk):
    return cur_blk - ref_blk

def p_frame_decode(ref_blk, residual):
    return ref_blk + residual

def conceal_lost_block(ref_frame, rx, ry, bw, bh):
    return ref_frame[ry:ry+bh, rx:rx+bw].copy()

ref = np.array([[50, 52, 54], [51, 53, 55], [52, 54, 56]], dtype=np.int32)
cur = np.array([[50, 53], [51, 55]], dtype=np.int32)
res = p_frame_encode_residual(cur, ref[:2, :2])
rec = p_frame_decode(ref[:2, :2], res)
concealed = conceal_lost_block(ref, 1, 1, 2, 2)
print(f"RES_SUM={int(np.sum(np.abs(res)))}, EXACT={bool(np.array_equal(rec, cur))}, CONCEAL_TL={int(concealed[0,0])}")
""",
                        "expected_output": "RES_SUM=3, EXACT=True, CONCEAL_TL=53",
                    },
                ],
            },
        ],
    },
}
