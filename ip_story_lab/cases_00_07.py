"""Image & Video Processing Curriculum: Cases 00 through 07 (Fundamentals -> Lossless Coding)."""

CASES_00_07 = {
    "0": {
        "title": "Case 00: The Aliasing Artifact: Pixels, Sampling & Image Topology",
        "episodes": [
            {
                "title": "Module 1: Image Formation, Sampling & Quantization",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Satellite Urban Survey Shows Phantom Zebra Stripes",
                        "text": "An Earth-observation satellite captures a high-frequency solar-panel array, but the reconstructed ground preview shows wide, wavy diagonal stripes that do not exist on the roof, alongside staircase contours across smooth ocean gradients.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Understand digital image representation $f(x, y)$, the fundamental steps & elements of a DIP system, and how spatial sampling vs. intensity quantization govern resolution and artifacts.",
                    },
                    {
                        "type": "concept",
                        "title": "Digital Representation & System Pipeline",
                        "content": "A monochrome digital image is a 2-D discrete matrix $f(x, y)$ of $M$ rows and $N$ columns, where each coordinate $(x, y)$ stores a quantized intensity level $z \\in [0, L-1]$ with $L = 2^k$ ($k$ bits per pixel).\n\n- **Elements of a DIP System:** Image sensors (CCD/CMOS) & digitizer, specialized hardware/ALU, mass storage, image processing software, and display/hardcopy devices.\n- **Sampling** discretizes spatial coordinates $(x, y)$: undersampling frequencies above the Nyquist limit ($f_s < 2 f_{\\max}$) causes **spatial aliasing** (moire patterns).\n- **Quantization** discretizes amplitude $f(x, y)$ into $2^k$ levels: reducing $k$ below 5–6 bits causes **false contouring** across smooth ramps.",
                    },
                    {
                        "type": "visual",
                        "title": "Fundamental Steps in Digital Image Processing",
                        "code": """flowchart LR
    A["Image Acquisition"] --> B["Spatial Filtering & Enhancement"]
    B --> C["Restoration & Deblurring"]
    C --> D["Color & Wavelets"]
    D --> E["Compression"]
    E --> F["Morphology & Segmentation"]
    F --> G["Representation & Object Recognition"]""",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Uncompressed Frame Storage Sizing",
                        "formula": "$$\\text{Bits} = M \\times N \\times k \\quad \\text{(for } 2^k \\text{ gray levels)}$$",
                        "problem": "A sensor captures a $1024 \\times 1024$ grayscale frame with $256$ intensity levels ($k = 8$ bits). How many **Megabytes (MB, using $1\\text{ MB} = 1024^2\\text{ bytes}$)** does one uncompressed frame require?\n\nEnter numeric value:",
                        "answer": "1",
                        "alternatives": ["1.0", "1 MB"],
                        "step_by_step": "1. $L = 256 = 2^8 \\implies k = 8\\text{ bits} = 1\\text{ byte/pixel}$.\n2. Total bytes $= 1024 \\times 1024 \\times 1 = 1,048,576\\text{ bytes} = 1\\text{ MB}$.",
                    },
                ],
            },
            {
                "title": "Module 2: Pixel Neighbors, Adjacency & Connectivity",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "N4, ND, N8 and m-Adjacency",
                        "content": "Given a pixel $p$ at coordinates $(x, y)$:\n- **4-neighbors $N_4(p)$:** $(x\\pm 1, y)$ and $(x, y\\pm 1)$.\n- **Diagonal neighbors $N_D(p)$:** $(x\\pm 1, y\\pm 1)$.\n- **8-neighbors $N_8(p)$:** $N_4(p) \\cup N_D(p)$.\n\nLet $V$ be the set of intensity values used to define adjacency (e.g., $V = \\{1\\}$ in a binary mask):\n- **4-adjacency:** $p, q \\in V$ and $q \\in N_4(p)$.\n- **8-adjacency:** $p, q \\in V$ and $q \\in N_8(p)$ (can create ambiguous diagonal crossings!).\n- **m-adjacency (mixed):** $p, q \\in V$ and either (i) $q \\in N_4(p)$, or (ii) $q \\in N_D(p)$ AND $N_4(p) \\cap N_4(q)$ has **no pixels with values from $V$**.",
                    },
                    {
                        "type": "worked_example",
                        "title": "Resolving Path Ambiguity with m-Adjacency",
                        "steps": [
                            "Consider $V=\\{1\\}$ on a $2\\times 2$ block where $(0,0)=1$, $(0,1)=1$, $(1,1)=1$, and $(1,0)=0$.",
                            "Under 8-adjacency, $(0,0)$ connects directly to $(1,1)$ diagonally AND via $(0,1)$, creating redundant loops.",
                            "Check m-adjacency between $p=(0,0)$ and $q=(1,1)$: $N_4(p) \\cap N_4(q) = \\{(0,1), (1,0)\\}$. Since $(0,1)=1 \\in V$, the intersection is NOT empty!",
                            "Therefore, the direct diagonal link is pruned; the unique m-path is $(0,0) \\to (0,1) \\to (1,1)$.",
                        ],
                    },
                    {
                        "type": "interactive",
                        "question": "Why do boundary-tracing and thinning algorithms prefer m-adjacency over pure 8-adjacency?",
                        "options": [
                            "m-adjacency eliminates ambiguous diagonal shortcut loops when a 4-connected corner pixel already bridges the two pixels.",
                            "m-adjacency reduces the number of pixels in an image by half.",
                            "m-adjacency only works on RGB images, making grayscale processing obsolete.",
                            "m-adjacency replaces Fourier transforms in spatial sampling.",
                        ],
                        "answer": "m-adjacency eliminates ambiguous diagonal shortcut loops when a 4-connected corner pixel already bridges the two pixels.",
                        "explanation": "By pruning diagonal connections whenever $N_4(p) \\cap N_4(q)$ contains an active pixel in $V$, m-adjacency preserves topological uniqueness of digital paths and boundaries.",
                    },
                ],
            },
            {
                "title": "Module 3: Distance Measures, Regions & Boundaries",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Digital Metrics: Euclidean, City-Block (D4) & Chessboard (D8)",
                        "content": "For pixels $p=(x,y)$ and $q=(s,t)$, a valid distance metric satisfies non-negativity, symmetry, and the triangle inequality:\n- **Euclidean Distance:** $D_E(p, q) = \\sqrt{(x-s)^2 + (y-t)^2}$\n- **City-Block ($D_4$) Distance:** $D_4(p, q) = |x-s| + |y-t|$ (diamond-shaped contour; $D_4 = 1$ equals $N_4$).\n- **Chessboard ($D_8$) Distance:** $D_8(p, q) = \\max(|x-s|, |y-t|)$ (square-shaped contour; $D_8 = 1$ equals $N_8$).\n\nA **Region** $R$ is a connected set of pixels; its **Boundary** (border) is the set of pixels in $R$ having at least one neighbor outside $R$ (careful: 8-connected region requires a 4-connected background to avoid boundary leaks, and vice versa).",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Compute City-Block (D4) Distance",
                        "formula": "$$D_4(p, q) = |x - s| + |y - t|$$",
                        "problem": "Given pixel $p = (2, 5)$ and pixel $q = (7, 1)$, what is the **City-Block ($D_4$)** distance between them?",
                        "answer": "9",
                        "alternatives": ["9.0"],
                        "step_by_step": "$$D_4 = |2 - 7| + |5 - 1| = 5 + 4 = 9.$$",
                    },
                ],
            },
            {
                "title": "Module 4: Linear vs. Nonlinear Pixel Operators (Python Lab)",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Superposition Test: Linear vs. Nonlinear Image Operators",
                        "content": "An image operator $\\mathcal{H}$ is **linear** if and only if for any two images $f_1, f_2$ and scalars $a, b$:\n$$\\mathcal{H}\\{a f_1 + b f_2\\} = a \\mathcal{H}\\{f_1\\} + b \\mathcal{H}\\{f_2\\}$$\n- **Linear examples:** Sum, average, 2-D convolution, Sobel/Laplacian derivatives, DFT.\n- **Nonlinear examples:** $\\max$/$\\min$, Median filter, logarithmic transform, thresholding.",
                    },
                    {
                        "type": "code_lab",
                        "title": "Lab 00: Distance Metrics, 4-Connected Components & Linearity Probe",
                        "language": "python",
                        "instructions": "Implement `compute_distances(p, q)` returning `(d4, d8, round(de, 4))` and `is_linear_operator(op, img1, img2)` testing superposition ($a=2, b=3$).",
                        "starter_code": """import numpy as np
import math

def compute_distances(p, q):
    # Return (D4, D8, round(DE, 4))
    pass

def is_linear_operator(op, img1, img2):
    # Test op(2*img1 + 3*img2) == 2*op(img1) + 3*op(img2)
    pass

p, q = (1, 2), (4, 6)
d4, d8, de = compute_distances(p, q)
a = np.array([[1.0, 4.0], [2.0, 8.0]])
b = np.array([[3.0, 1.0], [5.0, 2.0]])
lin_sum = is_linear_operator(lambda x: x * 0.5, a, b)
lin_max = is_linear_operator(lambda x: np.max(x), a, b)
print(f"D4={d4}, D8={d8}, DE={de}, scale_lin={lin_sum}, max_lin={lin_max}")
""",
                        "solution_code": """import numpy as np
import math

def compute_distances(p, q):
    dx = abs(p[0] - q[0])
    dy = abs(p[1] - q[1])
    d4 = dx + dy
    d8 = max(dx, dy)
    de = round(math.hypot(dx, dy), 4)
    return d4, d8, de

def is_linear_operator(op, img1, img2):
    lhs = op(2.0 * img1 + 3.0 * img2)
    rhs = 2.0 * op(img1) + 3.0 * op(img2)
    return bool(np.allclose(lhs, rhs))

p, q = (1, 2), (4, 6)
d4, d8, de = compute_distances(p, q)
a = np.array([[1.0, 4.0], [2.0, 8.0]])
b = np.array([[3.0, 1.0], [5.0, 2.0]])
lin_sum = is_linear_operator(lambda x: x * 0.5, a, b)
lin_max = is_linear_operator(lambda x: np.max(x), a, b)
print(f"D4={d4}, D8={d8}, DE={de}, scale_lin={lin_sum}, max_lin={lin_max}")
""",
                        "expected_output": "D4=7, D8=4, DE=5.0, scale_lin=True, max_lin=False",
                    },
                ],
            },
        ],
    },
    "1": {
        "title": "Case 01: Shadow Recovery: Spatial Point Transforms & Logic Ops",
        "episodes": [
            {
                "title": "Module 1: Gray-Level Intensity Transformations",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Underexposed Radiograph Hides Hairline Stress Fracture",
                        "text": "An emergency dental X-ray sensor outputs dark pixels clustered in $[0, 45]$ out of $[0, 255]$. Bone trabeculae are invisible on standard monitors.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Apply point-wise spatial transforms $s = T(r)$: Image Negatives, Log Transforms, Power-Law (Gamma) Correction, and Piecewise Contrast Stretching.",
                    },
                    {
                        "type": "concept",
                        "title": "Canonical Point Mapping Functions",
                        "content": "Operating solely on pixel intensity $r \\in [0, L-1]$:\n- **Negative:** $s = (L - 1) - r$ — enhances white/gray details embedded in dark regions.\n- **Log Transform:** $s = c \\log(1 + r)$ — expands dark values while compressing extreme bright peaks (ideal for FFT magnitude spectra!).\n- **Power-Law (Gamma):** $s = c \\cdot r^\\gamma$ (on normalized $r \\in [0,1]$): $\\gamma < 1$ brightens shadows (lifts low intensities); $\\gamma > 1$ darkens midtones and boosts highlight contrast.",
                    },
                    {
                        "type": "interactive",
                        "question": "To brighten details hidden in dark shadows of a normalized image $r \\in [0, 1]$ using gamma transformation $s = r^\\gamma$, which $\\gamma$ should you choose?",
                        "options": [
                            "gamma < 1 (e.g., gamma = 0.4)",
                            "gamma > 1 (e.g., gamma = 2.5)",
                            "gamma = 1.0",
                            "gamma = 0.0",
                        ],
                        "answer": "gamma < 1 (e.g., gamma = 0.4)",
                        "explanation": "For $r \\in (0, 1)$, raising $r$ to a power $\\gamma < 1$ maps dark inputs upward ($0.1^{0.4} \\approx 0.398$), expanding shadow dynamic range.",
                    },
                ],
            },
            {
                "title": "Module 2: Bit-Plane Slicing & Piecewise Contrast Stretching",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Decomposing 8-Bit Pixels into Structural Bit Planes",
                        "content": "Every 8-bit pixel is a binary sum $\\sum_{b=0}^{7} a_b 2^b$:\n- **Higher-order planes (Bits 7, 6, 5):** Carry the majority of visually significant structural geometry.\n- **Lower-order planes (Bits 0, 1, 2):** Contribute subtle shading and **random sensor noise** (and are prime targets for LSB steganography/watermarking).\n\n**Piecewise Contrast Stretching** maps an input range $[r_1, r_2]$ linearly onto $[s_1, s_2]$ with steep slope $> 1$ to expand narrow dynamic ranges.",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Bit-Plane Weight Dominance",
                        "formula": "$$\\text{Weight}(b) = \\frac{2^b}{255}$$",
                        "problem": "In an 8-bit grayscale image ($0..255$), what integer value does setting **only Bit 7 (MSB)** to 1 contribute to a pixel?",
                        "answer": "128",
                        "alternatives": ["128.0"],
                        "step_by_step": "Bit indices run $0..7$. MSB is $2^7 = 128$.",
                    },
                ],
            },
            {
                "title": "Module 3: Arithmetic & Logic Pixel Operations",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Image Subtraction, Averaging & Bitwise Masking",
                        "content": "1. **Image Subtraction:** $d(x, y) = f(x, y) - h(x, y)$ isolates motion, PCB missing components, or angiogram dye vessels.\n2. **Image Averaging:** Averaging $K$ noisy frames $g_i(x,y) = f(x,y) + \\eta_i(x,y)$ with uncorrelated zero-mean noise $\\sigma_\\eta^2$ keeps the signal intact while cutting noise variance by $K$: $$\\sigma_{\\bar{g}}^2 = \\frac{\\sigma_\\eta^2}{K}$$\n3. **Logic Ops (AND / OR / XOR):** Masking out regions of interest (ROI) using binary bitmasks.",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Multi-Frame Noise Variance Reduction",
                        "formula": "$$\\sigma_{\\bar{g}} = \\frac{\\sigma_\\eta}{\\sqrt{K}}$$",
                        "problem": "A low-light astronomy camera averages $K = 16$ consecutive stationary frames to suppress zero-mean Gaussian sensor noise. By what **factor** is the noise **standard deviation** $\\sigma$ reduced?",
                        "answer": "4",
                        "alternatives": ["4x", "4.0"],
                        "step_by_step": "Variance drops by $K = 16$, so standard deviation drops by $\\sqrt{16} = 4$.",
                    },
                ],
            },
            {
                "title": "Module 4: Gamma & Bit-Plane Lab (Python)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 01: Gamma Correction, Log Transform & MSB Reconstruction",
                        "language": "python",
                        "instructions": "Implement `gamma_transform(img_u8, gamma)` and `reconstruct_top_bits(img_u8, num_bits)` keeping only the top `num_bits` MSBs (e.g. bits 7 and 6 for `num_bits=2`).",
                        "starter_code": """import numpy as np

def gamma_transform(img_u8, gamma):
    # Normalize to [0,1], apply r**gamma, scale to 255 and round to uint8
    pass

def reconstruct_top_bits(img_u8, num_bits):
    # Keep only the top num_bits of an 8-bit array
    pass

arr = np.array([0, 64, 128, 255], dtype=np.uint8)
g_out = gamma_transform(arr, 0.5)
msb_out = reconstruct_top_bits(np.array([255, 191, 127, 63], dtype=np.uint8), 2)
print("GAMMA:", g_out.tolist(), "MSB2:", msb_out.tolist())
""",
                        "solution_code": """import numpy as np

def gamma_transform(img_u8, gamma):
    norm = img_u8.astype(np.float64) / 255.0
    out = np.clip((norm ** gamma) * 255.0, 0, 255)
    return np.round(out).astype(np.uint8)

def reconstruct_top_bits(img_u8, num_bits):
    shift = 8 - num_bits
    mask = ((0xFF >> shift) << shift) & 0xFF
    return (img_u8 & mask).astype(np.uint8)

arr = np.array([0, 64, 128, 255], dtype=np.uint8)
g_out = gamma_transform(arr, 0.5)
msb_out = reconstruct_top_bits(np.array([255, 191, 127, 63], dtype=np.uint8), 2)
print("GAMMA:", g_out.tolist(), "MSB2:", msb_out.tolist())
""",
                        "expected_output": "GAMMA: [0, 128, 181, 255] MSB2: [192, 128, 64, 0]",
                    },
                ],
            },
        ],
    },
    "2": {
        "title": "Case 02: The Washed-Out Microscope: Histograms & Spatial Filters",
        "episodes": [
            {
                "title": "Module 1: Histogram Equalization & Specification",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Low-Contrast Pathology Slide Defeats Automated Counters",
                        "text": "Fluorescence microscope images cluster between intensities $90$ and $130$, hiding nuclear membranes.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Derive discrete Histogram Equalization via the cumulative distribution function (CDF), contrast it with Histogram Matching, and understand local histogram enhancement.",
                    },
                    {
                        "type": "concept",
                        "title": "Discrete CDF Mapping",
                        "content": "Let $p_r(r_k) = n_k / MN$ be the normalized histogram of an $M \\times N$ image with $L$ levels. Histogram Equalization maps each gray level $r_k$ via:\n$$s_k = (L - 1) \\sum_{j=0}^{k} p_r(r_j)$$\n- **Histogram Matching (Specification):** Equalizes input $r \\to s$, then inverts a desired target distribution $G(z) = s$ to shape histograms to an exact profile.\n- **Local Histogram Processing:** Computes local CDFs inside a sliding neighborhood window (e.g., CLAHE) when global contrast varies strongly across regions.",
                    },
                    {
                        "type": "worked_example",
                        "title": "Manual 3-Bit (L=8) Histogram Equalization",
                        "steps": [
                            "Given $64$ total pixels with counts: $n_0=8, n_1=16, n_2=24, n_3=16, n_{4..7}=0$.",
                            "Compute CDF probabilities: $c_0=8/64=0.125$, $c_1=24/64=0.375$, $c_2=48/64=0.75$, $c_3=1.0$.",
                            "Scale by $L-1 = 7$ and round: $s_0 = \\text{round}(0.875) = 1$, $s_1 = \\text{round}(2.625) = 3$, $s_2 = \\text{round}(5.25) = 5$, $s_3 = 7$.",
                            "Input levels $[0, 1, 2, 3]$ spread cleanly across $[1, 3, 5, 7]$!",
                        ],
                    },
                ],
            },
            {
                "title": "Module 2: Spatial Smoothing — Linear vs. Order-Statistic Filters",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Convolution vs. Correlation & Impulse Noise",
                        "content": "Spatial filtering slides a $m \\times n$ kernel $w(s,t)$ across the image:\n- **Correlation:** Direct weighted sum $\\sum w(s,t)f(x+s, y+t)$.\n- **Convolution:** Rotates kernel $w$ by $180^\\circ$ before summing (important for asymmetric derivative masks!).\n\n**Smoothing Filters:**\n- **Box / Gaussian LPF:** Linear weighted average; blurs Gaussian noise **but also blurs sharp edges** and smears salt-and-pepper spikes.\n- **Median Filter (Order-Statistic):** Nonlinear; replaces center pixel with the median of its neighborhood. Eliminates isolated impulse spikes while **preserving crisp step edges**.",
                    },
                    {
                        "type": "debugger",
                        "title": "Gaussian Blur Fails on Salt-and-Pepper Dead Pixels",
                        "scenario": "A technician applies a $5\\times 5$ Gaussian filter to remove isolated white ($255$) and black ($0$) dead-pixel spikes, but turns every tiny spike into a fuzzy gray smudge.",
                        "options": [
                            "Replace the linear Gaussian filter with a nonlinear 3x3 Median filter, which rejects extreme outlier intensities cleanly.",
                            "Increase the Gaussian kernel size to 15x15 to average out the smudges.",
                            "Apply Histogram Equalization before the Gaussian filter.",
                            "Use a Laplacian sharpening kernel to erase the white spikes.",
                        ],
                        "answer": "Replace the linear Gaussian filter with a nonlinear 3x3 Median filter, which rejects extreme outlier intensities cleanly.",
                        "explanation": "Linear averaging spreads extreme $0/255$ outliers into neighboring pixels. The Median filter sorts neighborhood values and selects the middle value, discarding outliers completely.",
                    },
                ],
            },
            {
                "title": "Module 3: Sharpening — Gradients, Laplacian & Unsharp Masking",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "1st-Order vs. 2nd-Order Spatial Derivatives",
                        "content": "- **1st-Order Gradient (Sobel / Prewitt):** $\\nabla f = [g_x, g_y]^T$, magnitude $\\|\\nabla f\\| \\approx |g_x| + |g_y|$. Produces thick responses across intensity ramps.\n- **2nd-Order Laplacian:** $\\nabla^2 f = \\frac{\\partial^2 f}{\\partial x^2} + \\frac{\\partial^2 f}{\\partial y^2}$ (isotropic kernel `[0,1,0; 1,-4,1; 0,1,0]`). Zero on flat regions & constant ramps, sharp zero-crossing on fine lines/edges.\n- **Unsharp Masking & High-Boost:** Subtract smoothed image $g_{\\text{mask}} = f - \\bar{f}$, then add back: $g = f + k \\cdot g_{\\text{mask}}$ ($k=1$: unsharp masking; $k>1$: high-boost).",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Compute 1-D Discrete Laplacian Response",
                        "formula": "$$\\nabla^2 f(x) = f(x+1) + f(x-1) - 2f(x)$$",
                        "problem": "Along a 1-D intensity ramp $[10, 20, 30, 40]$, what is the **2nd-order Laplacian** value at the pixel $f(x) = 20$?",
                        "answer": "0",
                        "alternatives": ["0.0"],
                        "step_by_step": "$$\\nabla^2 f = 30 + 10 - 2(20) = 0.$$ Constant ramps always have zero 2nd derivative.",
                    },
                ],
            },
            {
                "title": "Module 4: Histogram Equalization & Median Filter Lab (Python)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 02: Exact Histogram Equalization & 3x3 Median Denoiser",
                        "language": "python",
                        "instructions": "Implement `hist_equalize_u8(img)` using discrete CDF mapping and `median_filter_3x3(img)` with zero-padding (`np.pad(..., 1, mode='edge')`).",
                        "starter_code": """import numpy as np

def hist_equalize_u8(img):
    # Return equalized uint8 array
    pass

def median_filter_3x3(img):
    # Pad edges by 1 with mode='edge' and take 3x3 median
    pass

sample = np.array([[10, 10, 20], [10, 255, 20], [20, 20, 30]], dtype=np.uint8)
med = median_filter_3x3(sample)
eq = hist_equalize_u8(np.array([[0, 0, 1], [1, 2, 2], [2, 3, 3]], dtype=np.uint8))
print("MED_CENTER:", int(med[1, 1]), "EQ_LAST:", int(eq[2, 2]))
""",
                        "solution_code": """import numpy as np

def hist_equalize_u8(img):
    hist = np.bincount(img.ravel(), minlength=256)
    cdf = hist.cumsum() / img.size
    lut = np.round(cdf * 255.0).astype(np.uint8)
    return lut[img]

def median_filter_3x3(img):
    padded = np.pad(img, 1, mode="edge")
    h, w = img.shape
    out = np.zeros_like(img)
    for i in range(h):
        for j in range(w):
            out[i, j] = np.median(padded[i:i+3, j:j+3])
    return out.astype(img.dtype)

sample = np.array([[10, 10, 20], [10, 255, 20], [20, 20, 30]], dtype=np.uint8)
med = median_filter_3x3(sample)
eq = hist_equalize_u8(np.array([[0, 0, 1], [1, 2, 2], [2, 3, 3]], dtype=np.uint8))
print("MED_CENTER:", int(med[1, 1]), "EQ_LAST:", int(eq[2, 2]))
""",
                        "expected_output": "MED_CENTER: 20 EQ_LAST: 255",
                    },
                ],
            },
        ],
    },
    "3": {
        "title": "Case 03: Into the Spectrum: 1-D/2-D DFT & Homomorphic Filtering",
        "episodes": [
            {
                "title": "Module 1: 1-D & 2-D Fourier Transform Foundations",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Factory Conveyor Floodlight Creates Severe Vignette",
                        "text": "Overhead floodlights illuminate one side of a metal sheet 4x brighter than the far corner, breaking global defect detectors.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Master 1-D/2-D DFT & IDFT pairs, spectrum centering, the Convolution Theorem, and why frequency separation beats spatial brute force.",
                    },
                    {
                        "type": "concept",
                        "title": "2-D DFT, Centering & Convolution Theorem",
                        "content": "The 2-D DFT of an $M \\times N$ image $f(x, y)$ is:\n$$F(u, v) = \\sum_{x=0}^{M-1} \\sum_{y=0}^{N-1} f(x, y) e^{-j 2\\pi (ux/M + vy/N)}$$\n- **Centering:** Multiplying $f(x, y)$ by $(-1)^{x+y}$ shifts the DC origin $F(0,0)$ to the center $(M/2, N/2)$.\n- **Convolution Theorem:** Spatial convolution is frequency-domain multiplication: $f(x, y) * h(x, y) \\Longleftrightarrow F(u, v) H(u, v)$.\n- **Magnitude vs. Phase:** Magnitude $|F(u,v)|$ encodes contrast/energy; **Phase $\\phi(u,v)$ encodes spatial structure & edge locations**.",
                    },
                    {
                        "type": "interactive",
                        "question": "If you swap the Fourier Magnitude of Image A with the Fourier Phase of Image B and take the Inverse 2-D DFT, which image's objects/edges remain visually recognizable?",
                        "options": [
                            "Image B, because phase governs where edges and structural features sit in space.",
                            "Image A, because magnitude stores all edge positions.",
                            "Neither, because phase carries zero visual information.",
                            "A 50/50 ghost overlay of both images.",
                        ],
                        "answer": "Image B, because phase governs where edges and structural features sit in space.",
                        "explanation": "In classic Oppenheim-Lim experiments, phase retains structural edge alignment while magnitude mostly scales contrast.",
                    },
                ],
            },
            {
                "title": "Module 2: Frequency Smoothing & Sharpening Filters",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Ideal, Butterworth & Gaussian Spectral Filters",
                        "content": "Let $D(u,v)$ be the Euclidean distance from the centered origin:\n- **Ideal LPF (ILPF):** Hard cutoff $D \\le D_0$. Sharp brick-wall causes severe **ringing (Gibbs phenomenon)** due to its $\\text{sinc}$ spatial impulse.\n- **Butterworth LPF (BLPF):** $H(u,v) = \\frac{1}{1 + [D(u,v)/D_0]^{2n}}$. Order $n$ tunes ringing vs. sharpness.\n- **Gaussian LPF (GLPF):** $H(u,v) = e^{-D^2(u,v) / (2 D_0^2)}$. The inverse of a Gaussian is a Gaussian — **zero ringing guaranteed**!\n\nCorresponding **High-Pass Filters (HPF)** equal $H_{\\text{HP}}(u,v) = 1 - H_{\\text{LP}}(u,v)$.",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Butterworth Filter Attenuation at Cutoff",
                        "formula": "$$H(u, v) = \\frac{1}{1 + [D(u, v) / D_0]^{2n}}$$",
                        "problem": "For any Butterworth Low-Pass Filter of order $n = 2$, what is the filter gain $H(u, v)$ right on the cutoff circle $D(u, v) = D_0$?",
                        "answer": "0.5",
                        "alternatives": ["0.50", "1/2"],
                        "step_by_step": "When $D(u,v) = D_0$, $[D/D_0]^{2n} = 1^{4} = 1$, so $H = 1 / (1 + 1) = 0.5$.",
                    },
                ],
            },
            {
                "title": "Module 3: Homomorphic Filtering",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Separating Illumination & Reflectance via Logarithm",
                        "content": "An image is formed multiplicatively as illumination times reflectance: $f(x,y) = i(x,y) \\cdot r(x,y)$.\nBecause multiplication is not separable linearly in Fourier space, **Homomorphic Filtering** applies $\\ln$ first:\n$$z(x,y) = \\ln i(x,y) + \\ln r(x,y)$$\n- Slow spatial illumination $i(x,y)$ concentrates at **low frequencies** -> attenuated by $\\gamma_L < 1$.\n- Fine surface reflectance $r(x,y)$ concentrates at **high frequencies** -> boosted by $\\gamma_H > 1$.\n- Taking $\\exp$ after IDFT yields balanced dynamic range and crisp local contrast simultaneously!",
                    },
                    {
                        "type": "visual",
                        "title": "Homomorphic Filtering Pipeline",
                        "code": """flowchart LR
    A["Input f(x,y) = i * r"] --> B["ln(f + 1)"]
    B --> C["2-D FFT"]
    C --> D["Homomorphic Filter H(u,v)"]
    D --> E["2-D IFFT"]
    E --> F["exp(.) Output"]""",
                    },
                ],
            },
            {
                "title": "Module 4: 2-D FFT Filtering & Homomorphic Lab (Python)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 03: Centered Gaussian LPF & Homomorphic Illumination Normalizer",
                        "language": "python",
                        "instructions": "Implement `gaussian_lpf_fft(img, d0)` returning the real filtered array and `homomorphic_gain(d, d0, gamma_l=0.4, gamma_h=1.8, c=1.0)` evaluating the homomorphic transfer function.",
                        "starter_code": """import numpy as np

def gaussian_lpf_fft(img, d0):
    # Compute centered FFT, multiply by Gaussian exp(-D^2 / (2*d0^2)), inverse FFT real
    pass

def homomorphic_gain(d, d0, gamma_l=0.4, gamma_h=1.8, c=1.0):
    # Return (gamma_h - gamma_l) * (1 - exp(-c * (d^2 / d0^2))) + gamma_l
    pass

grid = np.ones((8, 8), dtype=np.float64) * 100.0
grid[0, 0] = 200.0
out = gaussian_lpf_fft(grid, d0=2.0)
g0 = round(homomorphic_gain(0.0, 10.0), 3)
ginf = round(homomorphic_gain(1000.0, 10.0), 3)
print(f"DC_MEAN={round(float(out.mean()), 2)}, G0={g0}, GINF={ginf}")
""",
                        "solution_code": """import numpy as np

def gaussian_lpf_fft(img, d0):
    M, N = img.shape
    F = np.fft.fftshift(np.fft.fft2(img))
    u = np.arange(M) - M / 2.0
    v = np.arange(N) - N / 2.0
    V, U = np.meshgrid(v, u)
    D2 = U ** 2 + V ** 2
    H = np.exp(-D2 / (2.0 * (d0 ** 2)))
    g = np.fft.ifft2(np.fft.ifftshift(F * H))
    return np.real(g)

def homomorphic_gain(d, d0, gamma_l=0.4, gamma_h=1.8, c=1.0):
    return float((gamma_h - gamma_l) * (1.0 - np.exp(-c * ((d ** 2) / (d0 ** 2)))) + gamma_l)

grid = np.ones((8, 8), dtype=np.float64) * 100.0
grid[0, 0] = 200.0
out = gaussian_lpf_fft(grid, d0=2.0)
g0 = round(homomorphic_gain(0.0, 10.0), 3)
ginf = round(homomorphic_gain(1000.0, 10.0), 3)
print(f"DC_MEAN={round(float(out.mean()), 2)}, G0={g0}, GINF={ginf}")
""",
                        "expected_output": "DC_MEAN=101.56, G0=0.4, GINF=1.8",
                    },
                ],
            },
        ],
    },
    "4": {
        "title": "Case 04: Motion Blur & Periodic Hum: Degradation & Wiener Restoration",
        "episodes": [
            {
                "title": "Module 1: Degradation Model & Noise PDFs",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Telescope Frame Corrupted by Powerline Stripes and Tracking Blur",
                        "text": "A planetary image suffers from diagonal tracking blur AND a sinusoidal 60Hz diagonal stripe pattern.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Contrast Enhancement vs. objective Restoration, identify statistical noise PDFs, and choose optimal spatial noise-only filters.",
                    },
                    {
                        "type": "concept",
                        "title": "Linear Degradation & Noise-Only Spatial Filters",
                        "content": "In the spatial/frequency degradation model: $$G(u,v) = H(u,v)F(u,v) + N(u,v)$$\n- **Noise PDFs:** Gaussian (electronic thermal), Rayleigh (range imaging), Erlang/Gamma (laser speckle), Exponential, Uniform, and **Impulse (Salt-and-Pepper)**.\n- **Contraharmonic Mean Filter:** $\\hat{f}(x,y) = \\frac{\\sum g(s,t)^{Q+1}}{\\sum g(s,t)^Q}$. Positive $Q$ removes **pepper** (black) noise; negative $Q$ removes **salt** (white) noise; $Q=0$ is Arithmetic Mean; $Q=-1$ is Harmonic Mean.\n- **Alpha-Trimmed Mean:** Drops $d/2$ lowest & $d/2$ highest values, averaging the middle — ideal for mixed Gaussian + impulse noise.",
                    },
                    {
                        "type": "interactive",
                        "question": "Which parameter sign in a Contraharmonic Mean Filter removes dark 'pepper' spikes ($g \\approx 0$), and what happens if you pick the wrong sign?",
                        "options": [
                            "Positive Q (> 0) removes pepper noise; negative Q amplifies pepper noise toward zero.",
                            "Negative Q (< 0) removes pepper noise; positive Q removes salt noise.",
                            "Q = 0 removes both salt and pepper completely.",
                            "Contraharmonic mean only works on frequency spectra.",
                        ],
                        "answer": "Positive Q (> 0) removes pepper noise; negative Q amplifies pepper noise toward zero.",
                        "explanation": "With $Q > 0$, near-zero pixels contribute almost nothing to both numerator ($g^{Q+1}$) and denominator ($g^Q$), eliminating dark pepper spikes cleanly.",
                    },
                ],
            },
            {
                "title": "Module 2: Periodic Noise Reduction & Estimating H(u,v)",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Notch Filtering & Degradation Estimation",
                        "content": "Sinusoidal periodic interference appears as **symmetric impulse pairs** $(u_0, v_0)$ and $(-u_0, -v_0)$ in the 2-D FFT magnitude.\n- **Notch Reject Filter:** Zeros out small neighborhoods around conjugate spike coordinates while leaving the rest of the spectrum untouched.\n- **Estimating $H(u,v)$:** (1) Observation on sharp edges/points, (2) Experimentation via impulse PSF response, (3) Mathematical modeling — e.g. uniform linear motion blur $H(u,v) = \\frac{T}{\\pi(ua + vb)} \\sin[\\pi(ua + vb)] e^{-j\\pi(ua + vb)}$ or atmospheric turbulence $e^{-k(u^2+v^2)^{5/6}}$.",
                    },
                ],
            },
            {
                "title": "Module 3: Direct Inverse vs. Wiener (MMSE) Restoration",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Avoiding Division-by-Zero Noise Explosion",
                        "content": "Direct Inverse Filtering computes $\\hat{F}(u,v) = G(u,v) / H(u,v) = F(u,v) + N(u,v)/H(u,v)$. Whenever $H(u,v) \\to 0$ at high frequencies, noise $N/H$ explodes!\n\n**Wiener (Minimum Mean-Square Error) Filter** regularizes zeros using noise-to-signal ratio $K \\approx S_\\eta / S_f$:\n$$\\hat{F}(u,v) = \\left[ \\frac{H^*(u,v)}{|H(u,v)|^2 + K} \\right] G(u,v)$$",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Wiener Gain with Zero Blur Attenuation",
                        "formula": "$$W(u,v) = \\frac{H^*(u,v)}{|H(u,v)|^2 + K}$$",
                        "problem": "If a frequency has $H(u,v) = 1.0$ and the regularization constant is $K = 0.25$, what is the Wiener filter gain $W(u,v)$?",
                        "answer": "0.8",
                        "alternatives": ["0.80", "4/5"],
                        "step_by_step": "$$W = \\frac{1}{1^2 + 0.25} = \\frac{1}{1.25} = 0.8.$$",
                    },
                ],
            },
            {
                "title": "Module 4: Wiener Deconvolution & Contraharmonic Lab (Python)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 04: 2-D Wiener Deconvolution & Contraharmonic Filter",
                        "language": "python",
                        "instructions": "Implement `wiener_restore(G, H, K)` applying the frequency-domain Wiener filter and `contraharmonic_patch(patch, Q)`.",
                        "starter_code": """import numpy as np

def wiener_restore(G, H, K):
    # Return spatial real restored array using Wiener equation
    pass

def contraharmonic_patch(patch, Q):
    p = patch.astype(np.float64)
    # Return sum(p**(Q+1)) / sum(p**Q)
    pass

img = np.array([[10, 50, 80, 20], [30, 90, 60, 10], [20, 40, 70, 30], [10, 20, 30, 40]], dtype=np.float64)
H = np.ones_like(img, dtype=np.complex128) * 0.5
G = np.fft.fft2(img) * H
rec = wiener_restore(G, H, K=0.0)
ch = contraharmonic_patch(np.array([0.0, 100.0, 100.0, 100.0]), Q=2.0)
print(f"WIENER_ERR={round(float(np.max(np.abs(rec - img))), 6)}, CH_PEPPER={round(float(ch), 2)}")
""",
                        "solution_code": """import numpy as np

def wiener_restore(G, H, K):
    W = np.conj(H) / ((np.abs(H) ** 2) + K)
    return np.real(np.fft.ifft2(G * W))

def contraharmonic_patch(patch, Q):
    p = patch.astype(np.float64)
    num = np.sum(p ** (Q + 1.0))
    den = np.sum(p ** Q)
    return num / den if den != 0 else 0.0

img = np.array([[10, 50, 80, 20], [30, 90, 60, 10], [20, 40, 70, 30], [10, 20, 30, 40]], dtype=np.float64)
H = np.ones_like(img, dtype=np.complex128) * 0.5
G = np.fft.fft2(img) * H
rec = wiener_restore(G, H, K=0.0)
ch = contraharmonic_patch(np.array([0.0, 100.0, 100.0, 100.0]), Q=2.0)
print(f"WIENER_ERR={round(float(np.max(np.abs(rec - img))), 6)}, CH_PEPPER={round(float(ch), 2)}")
""",
                        "expected_output": "WIENER_ERR=0.0, CH_PEPPER=100.0",
                    },
                ],
            },
        ],
    },
    "5": {
        "title": "Case 05: Chromatic Shift: Color Models, HSI & Pseudocolor",
        "episodes": [
            {
                "title": "Module 1: RGB, CMYK, YCbCr & HSI Color Models",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Equalizing R, G, and B Independently Ruins Broadcast Skin Tones",
                        "text": "Applying per-channel histogram equalization on RGB images shifts skin tones green/magenta because RGB couples luminance with chromaticity.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Master hardware-oriented models (RGB, CMY/CMYK, YCbCr) vs. perceptual HSI decoupling, plus Pseudocolor intensity slicing.",
                    },
                    {
                        "type": "concept",
                        "title": "Subtractive vs. Additive & Perceptual Decoupling",
                        "content": "- **RGB (Additive):** Display hardware primaries; highly correlated.\n- **CMY / CMYK (Subtractive):** $C = 1-R, M = 1-G, Y = 1-B$, plus Black ($K$) for print ink efficiency.\n- **HSI (Hue, Saturation, Intensity):** Decouples achromatic Intensity $I = (R+G+B)/3$ from pure color Hue $H$ and purity Saturation $S = 1 - \\frac{3}{R+G+B}\\min(R,G,B)$.\n- **YCbCr:** Separates luma $Y$ from blue/red chroma differences $(C_b, C_r)$ — foundation of JPEG & MPEG chroma subsampling.",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Compute HSI Intensity & Saturation",
                        "formula": "$$I = \\frac{R+G+B}{3}, \\quad S = 1 - \\frac{3}{R+G+B}\\min(R,G,B)$$",
                        "problem": "For a normalized RGB pixel $(R, G, B) = (0.6, 0.3, 0.3)$, what is the **Saturation $S$**?",
                        "answer": "0.25",
                        "alternatives": ["1/4", "0.250"],
                        "step_by_step": "$R+G+B = 1.2$, $\\min = 0.3$, so $S = 1 - \\frac{3 \\times 0.3}{1.2} = 1 - 0.75 = 0.25$.",
                    },
                ],
            },
            {
                "title": "Module 2: Pseudocolor Image Processing",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Intensity Slicing & Gray-to-Color LUT Mapping",
                        "content": "Humans distinguish **thousands of color shades** vs. only ~40 shades of gray. **Pseudocolor Processing** assigns colors to monochrome intensities (e.g. airport baggage X-rays, thermal IR):\n- **Intensity Slicing:** Partitions $[0, L-1]$ into slabs using planes; each slab maps to a distinct RGB triplet.\n- **Continuous Gray-to-Color Transforms:** Feeds gray level $f(x,y)$ through three independent phase-shifted transfer functions $f_R(z), f_G(z), f_B(z)$ (e.g. shifted sinusoids).",
                    },
                ],
            },
            {
                "title": "Module 3: Color Transforms, Smoothing & Sharpening",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Channel-Wise vs. Intensity-Only Filtering",
                        "content": "- **Color Complements:** $s_i = 1 - r_i$ maps red $\\leftrightarrow$ cyan, green $\\leftrightarrow$ magenta, blue $\\leftrightarrow$ yellow.\n- **Color Smoothing & Sharpening:** Smooth/sharpen **only the $I$ component in HSI** to preserve hue integrity — smoothing $H$ directly causes rainbow wrap-around artifacts at $0^\\circ / 360^\\circ$!",
                    },
                    {
                        "type": "interactive",
                        "question": "Why should color histogram equalization be applied to the Intensity (I) channel of HSI rather than independently to R, G, and B?",
                        "options": [
                            "Modifying I alone stretches brightness while preserving original Hue and Saturation ratios, preventing unnatural color shifts.",
                            "RGB values cannot be sorted into histograms.",
                            "HSI images require 1/3rd the RAM of RGB images.",
                            "Hue must always be quantized to 2 bits.",
                        ],
                        "answer": "Modifying I alone stretches brightness while preserving original Hue and Saturation ratios, preventing unnatural color shifts.",
                        "explanation": "Independent RGB equalization scales channels non-proportionally, altering chromaticity ratios and shifting hues.",
                    },
                ],
            },
            {
                "title": "Module 4: Exact RGB ↔ HSI Intensity Enhancer (Python Lab)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 05: RGB to HSI Conversion & Saturation Calculator",
                        "language": "python",
                        "instructions": "Implement `rgb_to_hsi_pixel(r, g, b)` for normalized floats in `[0, 1]`, returning `(round(H_deg, 2), round(S, 4), round(I, 4))`.",
                        "starter_code": """import math

def rgb_to_hsi_pixel(r, g, b):
    # Compute I, S, and Hue in degrees [0, 360)
    pass

h, s, i = rgb_to_hsi_pixel(0.8, 0.2, 0.2)
h2, s2, i2 = rgb_to_hsi_pixel(0.5, 0.5, 0.5)
print(f"RED=({h},{s},{i}) GRAY=({h2},{s2},{i2})")
""",
                        "solution_code": """import math

def rgb_to_hsi_pixel(r, g, b):
    I = (r + g + b) / 3.0
    if r + g + b == 0 or (r == g == b):
        return 0.0, 0.0, round(I, 4)
    S = 1.0 - (3.0 / (r + g + b)) * min(r, g, b)
    num = 0.5 * ((r - g) + (r - b))
    den = math.sqrt((r - g) ** 2 + (r - b) * (g - b)) + 1e-12
    theta = math.degrees(math.acos(max(-1.0, min(1.0, num / den))))
    H = theta if b <= g else 360.0 - theta
    return round(H, 2), round(S, 4), round(I, 4)

h, s, i = rgb_to_hsi_pixel(0.8, 0.2, 0.2)
h2, s2, i2 = rgb_to_hsi_pixel(0.5, 0.5, 0.5)
print(f"RED=({h},{s},{i}) GRAY=({h2},{s2},{i2})")
""",
                        "expected_output": "RED=(0.0,0.5,0.4) GRAY=(0.0,0.0,0.5)",
                    },
                ],
            },
        ],
    },
    "6": {
        "title": "Case 06: Chroma Isolation: Color Segmentation, Noise & Compression",
        "episodes": [
            {
                "title": "Module 1: Color Slicing & 3-D Color Segmentation",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Warehouse Lighting Breaks Simple RGB Thresholds",
                        "text": "An automated produce sorter tries to isolate ripe red tomatoes using $R > 180$, failing whenever overhead clouds dim the skylight.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Segment color targets robustly in HSI and 3-D RGB space via Euclidean/Mahalanobis spheres, handle color noise, and apply chroma subsampling compression.",
                    },
                    {
                        "type": "concept",
                        "title": "Color Segmentation: HSI vs. RGB Mahalanobis",
                        "content": "- **HSI Segmentation:** Masks pixels where Hue lies within $[H_0 - \\Delta H, H_0 + \\Delta H]$ AND Saturation exceeds a minimum threshold $S > S_{\\min}$ (rejecting desaturated grays regardless of brightness $I$!).\n- **RGB Vector Segmentation:** Measures Euclidean distance $\\|\\mathbf{z} - \\mathbf{a}\\|_2 \\le D_0$ or covariance-weighted **Mahalanobis distance** $D(\\mathbf{z}, \\mathbf{a}) = \\sqrt{(\\mathbf{z}-\\mathbf{a})^T \\mathbf{C}^{-1} (\\mathbf{z}-\\mathbf{a})}$ around prototype color vector $\\mathbf{a}$.",
                    },
                ],
            },
            {
                "title": "Module 2: Noise in Color Images",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Correlated vs. Single-Channel Color Impulse Noise",
                        "content": "Color noise can corrupt channels independently (creating vivid magenta/cyan/yellow sparkles) or uniformly across R, G, B.\n- Filtering RGB channels separately with scalar median can create **false color pixels** not present in the original vector set.\n- **Vector Median Filter (VMF)** selects the existing color vector inside the window that minimizes the sum of Euclidean distances to all neighbors, preventing synthetic false colors.",
                    },
                ],
            },
            {
                "title": "Module 3: Color Image Compression & Chroma Subsampling",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Exploiting Human Chromatic Acuity (YCbCr 4:2:0)",
                        "content": "The human visual system has high spatial acuity for luminance ($Y$) but significantly lower acuity for chrominance ($C_b, C_r$).\n- **4:4:4:** Full resolution for $Y, C_b, C_r$.\n- **4:2:2:** $C_b, C_r$ subsampled $2\\times$ horizontally (33% fewer samples).\n- **4:2:0:** $C_b, C_r$ subsampled $2\\times$ horizontally AND $2\\times$ vertically (each $2\\times 2$ block shares 1 $C_b$ and 1 $C_r$ sample -> **50% raw data reduction before any entropy coding!**).",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "4:2:0 Chroma Subsampling Bandwidth Savings",
                        "formula": "$$\\text{Samples per } 2\\times 2\\text{ block} = 4_Y + 1_{C_b} + 1_{C_r} = 6$$",
                        "problem": "Compared to 4:4:4 ($4_Y + 4_{C_b} + 4_{C_r} = 12$ samples per $2\\times 2$ block), what **percentage (%)** of total color samples are retained in **4:2:0** subsampling?",
                        "answer": "50",
                        "alternatives": ["50%", "50.0"],
                        "step_by_step": "$$\\frac{6}{12} = 0.50 = 50\\%.$$",
                    },
                ],
            },
            {
                "title": "Module 4: RGB Color Sphere Segmenter & Subsampler (Python Lab)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 06: 3-D Color Distance Segmentation & 4:2:0 Chroma Downsampling",
                        "language": "python",
                        "instructions": "Implement `segment_color_sphere(rgb_img, target_rgb, radius)` returning a binary boolean mask and `subsample_420_size(h, w)` returning total sample count for a $H\\times W$ frame.",
                        "starter_code": """import numpy as np

def segment_color_sphere(rgb_img, target_rgb, radius):
    # Euclidean distance in 3D RGB <= radius
    pass

def subsample_420_size(h, w):
    # Return h*w (Y) + (h//2)*(w//2) (Cb) + (h//2)*(w//2) (Cr)
    pass

img = np.array([[[200, 20, 20], [190, 30, 25]], [[10, 200, 10], [50, 50, 50]]], dtype=np.float64)
mask = segment_color_sphere(img, np.array([195, 25, 22], dtype=np.float64), 20.0)
print(f"MASK_TRUE={int(mask.sum())}, SAMPLES_420={subsample_420_size(100, 100)}")
""",
                        "solution_code": """import numpy as np

def segment_color_sphere(rgb_img, target_rgb, radius):
    dist = np.linalg.norm(rgb_img - target_rgb, axis=-1)
    return dist <= radius

def subsample_420_size(h, w):
    return int(h * w + 2 * (h // 2) * (w // 2))

img = np.array([[[200, 20, 20], [190, 30, 25]], [[10, 200, 10], [50, 50, 50]]], dtype=np.float64)
mask = segment_color_sphere(img, np.array([195, 25, 22], dtype=np.float64), 20.0)
print(f"MASK_TRUE={int(mask.sum())}, SAMPLES_420={subsample_420_size(100, 100)}")
""",
                        "expected_output": "MASK_TRUE=2, SAMPLES_420=15000",
                    },
                ],
            },
        ],
    },
    "7": {
        "title": "Case 07: Zero-Loss Archive: Entropy & Error-Free Compression",
        "episodes": [
            {
                "title": "Module 1: Redundancy Types & Compression Models",
                "blocks": [
                    {
                        "type": "problem",
                        "title": "Hospital PACS Radiology Archive Hits 98% Capacity",
                        "text": "Diagnostic CT slices cannot discard a single pixel bit for legal compliance, yet raw scans consume terabytes weekly.",
                    },
                    {
                        "type": "objective",
                        "title": "Module Objective",
                        "content": "Quantify data vs. information redundancy, apply Shannon's Source Coding limit, and master error-free encoders (Huffman, Arithmetic, LZW, RLE).",
                    },
                    {
                        "type": "concept",
                        "title": "Three Redundancies & Compression Ratio",
                        "content": "Digital images exhibit three exploitable redundancies:\n1. **Coding Redundancy:** Using fixed-length $k$-bit codes when gray-level probabilities are skewed.\n2. **Spatial/Temporal Interpixel Redundancy:** Neighboring pixels are strongly correlated ($x \\approx x-1$).\n3. **Irrelevant (Psychovisual) Information:** Details invisible to the eye (exploited only by *lossy* compression).\n\nGiven $b$ compressed bits vs. $b_0$ original bits, **Compression Ratio** $C = b_0 / b$, **Relative Redundancy** $R = 1 - 1/C$, and Shannon's lower bound on lossless average bits/symbol is: $$H = -\\sum_{i} p_i \\log_2 p_i$$",
                    },
                    {
                        "type": "calculation_challenge",
                        "title": "Shannon Entropy Bound",
                        "formula": "$$H = -\\sum_{i} p_i \\log_2(p_i)$$",
                        "problem": "A 4-symbol image source emits symbols with probabilities $[0.5, 0.25, 0.125, 0.125]$. What is the exact **Shannon Entropy $H$** in bits/symbol?",
                        "answer": "1.75",
                        "alternatives": ["1.750", "7/4"],
                        "step_by_step": "$$H = -(0.5\\log_2 0.5 + 0.25\\log_2 0.25 + 2 \\times 0.125\\log_2 0.125) = 0.5 + 0.5 + 0.75 = 1.75\\text{ bits}.$$",
                    },
                ],
            },
            {
                "title": "Module 2: Huffman & Arithmetic Coding",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Prefix-Free Trees vs. Fractional Interval Coding",
                        "content": "- **Huffman Coding:** Builds an optimal prefix-free binary tree bottom-up by merging the two lowest-probability symbols. Achieves minimum average length among **integer-bit-per-symbol** codes, approaching $H$ when probabilities are negative powers of 2.\n- **Arithmetic Coding:** Maps an *entire message* onto a single sub-interval inside $[0, 1)$, bypassing the 1-bit-per-symbol floor! Essential when one symbol dominates ($p > 0.5$, e.g. binary fax/JBIG2).",
                    },
                ],
            },
            {
                "title": "Module 3: LZW Dictionary & Bit-Plane RLE",
                "blocks": [
                    {
                        "type": "concept",
                        "title": "Eliminating Interpixel Runs Without Prior Probabilities",
                        "content": "- **LZW Coding (GIF / TIFF):** Dynamically builds a string-phrase dictionary on the fly during a single pass — both encoder and decoder reconstruct the identical dictionary without transmitting it!\n- **Run-Length Encoding (RLE) & Bit-Plane Coding:** Encodes runs of identical values `(value, count)` across scanlines or Gray-coded bit planes (Gray code ensures adjacent intensities differ in only 1 bit, creating longer smooth runs!).",
                    },
                ],
            },
            {
                "title": "Module 4: Lossless RLE & Huffman Length Lab (Python)",
                "blocks": [
                    {
                        "type": "code_lab",
                        "title": "Lab 07: Exact Run-Length Codec & Average Codeword Length",
                        "language": "python",
                        "instructions": "Implement `rle_encode(seq)` returning list of `(val, count)` tuples, `rle_decode(pairs)`, and `avg_code_length(probs, lengths)`.",
                        "starter_code": """def rle_encode(seq):
    # Return [(val, count), ...]
    pass

def rle_decode(pairs):
    # Reconstruct exact original sequence
    pass

def avg_code_length(probs, lengths):
    return round(sum(p * l for p, l in zip(probs, lengths)), 4)

raw = [0, 0, 0, 0, 255, 255, 128, 128, 128]
enc = rle_encode(raw)
dec = rle_decode(enc)
avg_l = avg_code_length([0.5, 0.25, 0.125, 0.125], [1, 2, 3, 3])
print(f"PAIRS={len(enc)}, LOSSLESS={dec == raw}, AVG_BITS={avg_l}")
""",
                        "solution_code": """def rle_encode(seq):
    if not seq:
        return []
    out = []
    cur, cnt = seq[0], 1
    for x in seq[1:]:
        if x == cur:
            cnt += 1
        else:
            out.append((cur, cnt))
            cur, cnt = x, 1
    out.append((cur, cnt))
    return out

def rle_decode(pairs):
    out = []
    for val, cnt in pairs:
        out.extend([val] * cnt)
    return out

def avg_code_length(probs, lengths):
    return round(sum(p * l for p, l in zip(probs, lengths)), 4)

raw = [0, 0, 0, 0, 255, 255, 128, 128, 128]
enc = rle_encode(raw)
dec = rle_decode(enc)
avg_l = avg_code_length([0.5, 0.25, 0.125, 0.125], [1, 2, 3, 3])
print(f"PAIRS={len(enc)}, LOSSLESS={dec == raw}, AVG_BITS={avg_l}")
""",
                        "expected_output": "PAIRS=3, LOSSLESS=True, AVG_BITS=1.75",
                    },
                ],
            },
        ],
    },
}
