import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Stopwords to exclude common words from the word cloud
stopwords = set([
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", 
    "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", 
    "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's",
    "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", 
    "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought",
    "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than",
    "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll",
    "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "via", "was", "we", "we'd", "we'll", "we're",
    "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's",
    "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "using"
])

# 1. Get the paper list from the user
# papers_input = input("Please provide the list of papers:\n")
papers_input = """


- [Adaptive Non-linear Centroidal MPC with Stability Guarantees for Robust Locomotion of Legged Robots](https://arxiv.org/pdf/2409.01144)
- [ADEPT: Adaptive Diffusion Environment for Policy Transfer Sim-to-Real](https://arxiv.org/pdf/2506.01759)
- [Benchmarking Different QP Formulations and Solvers for Dynamic Quadrupedal Walking](https://arxiv.org/abs/2502.01329)
- [Bipedalism for Quadrupedal Robots: Versatile Loco-Manipulation through Risk-Adaptive Reinforcement Learning](https://arxiv.org/abs/2507.20382)
- [Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation](https://uan.csail.mit.edu/rsc/paper.pdf)
- [CAIMAN: Causal Action Influence Detection for Sample Efficient Loco-manipulation](https://arxiv.org/abs/2502.00835)
- [Disturbance-Aware Adaptive Compensation in Hybrid Force-Position Locomotion Policy for Legged Robots](https://arxiv.org/pdf/2506.00472)
- [FACET: Force-Adaptive Control via Impedance Reference Tracking for Legged Robots](https://arxiv.org/abs/2505.06883)
- [Floating-Base Deep Lagrangian Networks](https://arxiv.org/abs/2510.17270)
- [Generating Diverse Challenging Terrains for Legged Robots Using Quality-Diversity Algorithm](https://arxiv.org/pdf/2506.01362)
- [Learning coordinated badminton skills for legged manipulators](https://arxiv.org/abs/2505.22974)
- [Learning Stable Bipedal Locomotion Skills for Quadrupedal Robots on Challenging Terrains with Automatic Fall Recovery](https://www.nature.com/articles/s44182-025-00043-2)
- [Learning Steerable Imitation Controllers from Unstructured Animal Motions](https://arxiv.org/pdf/2507.00677)
- [Learning Unified Force and Position Control for Legged Loco-Manipulation](https://arxiv.org/abs/2505.20829)
- [LEVA: A high-mobility logistic vehicle with legged suspension](https://arxiv.org/pdf/2503.10028)
- [Load-bearing Assessment for Safe Locomotion of Quadruped Robots on Collapsing Terrain](https://arxiv.org/abs/2510.21369)
- [LocoTouch: Learning Dexterous Quadrupedal Transport with Tactile Sensing](https://arxiv.org/abs/2505.23175)
- [Long-horizon Locomotion and Manipulation on a Quadrupedal Robot with Large Language Models](https://arxiv.org/abs/2404.05291)
- [MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models](https://arxiv.org/abs/2503.08007)
- [MuJoCo Playground](https://www.arxiv.org/abs/2502.08844)
- [Multi-Quadruped Cooperative Object Transport: Learning Decentralized Pinch-Lift-Move](https://arxiv.org/abs/2509.14342)
- [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](https://arxiv.org/abs/2412.04453)
- [NIL: No-data Imitation Learning by Leveraging Pre-trained Video Diffusion Models](https://arxiv.org/abs/2503.10626)
- [Obstacle-Avoidant Leader Following with a Quadruped Robot](https://arxiv.org/pdf/2410.00572)
- [Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments](https://arxiv.org/abs/2505.19214)
- [Parkour in the Wild: Learning a General and Extensible Agile Locomotion Policy Using Multi-expert Distillation and RL Fine-tuning](https://arxiv.org/abs/2505.11164)
- [Physics-Based Motion Imitation with Adversarial Differential Discriminators](https://arxiv.org/abs/2505.04961)
- [Primal-Dual iLQR for GPU-Accelerated Learning and Control in Legged Robots](https://arxiv.org/abs/2506.07823)
- [QUART-Online: Latency-Free Large Multimodal Language Model for Quadruped Robot Learning](https://arxiv.org/abs/2412.15576)
- [RAMBO: RL-augmented Model-based Whole-body Control for Loco-manipulation](https://arxiv.org/abs/2504.06662)
- [Real-Time Out-of-Distribution Failure Prevention via Multi-Modal Reasoning](https://arxiv.org/abs/2505.10547)
- [Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning](https://arxiv.org/abs/2505.14266)
- [Spatio-Temporal Motion Retargeting for Quadruped Robots](https://arxiv.org/abs/2404.11557)
- [TAR: Teacher-Aligned Representations via Contrastive Learning for Quadrupedal Locomotion](https://arxiv.org/abs/2503.20839)
- [Towards Quadrupedal Jumping and Walking for Dynamic Locomotion using Reinforcement Learning](https://arxiv.org/abs/2510.24584)
- [Unsupervised Skill Discovery as Exploration for Learning Agile Locomotion](https://arxiv.org/abs/2508.08982)
- [Variable Stiffness for Robust Locomotion through Reinforcement Learning](https://arxiv.org/abs/2502.09436)
- [Versatile Legged Locomotion Adaptation through Vision-Language Grounding](https://openreview.net/forum?id=xz1Uu8Yb7w)
- [Versatile Loco-Manipulation through Flexible Interlimb Coordination](https://arxiv.org/abs/2506.07876)
- [VR-Robo: A Real-to-Sim-to-Real Framework for Visual Robot Navigation and Locomotion](https://arxiv.org/abs/2502.01536)
- [Whole-Body End-Effector Pose Tracking](https://arxiv.org/pdf/2409.16048)

"""

# 2. Ask the user for the title of the picture
# picture_title = input("Please provide the title for the picture (without the .png extension): ")
picture_title = "2025"

# 3. Extract the words from the titles (excluding the links)
titles = re.findall(r"\[(.*?)\]\(.*?\)", papers_input)

keywords = []
for title in titles:
    for word in title.split():
        cleaned_word = re.sub(r'[^a-zA-Z]', '', word).lower()  # Removing non-alphabetic characters and converting to lowercase
        if cleaned_word not in stopwords:
            keywords.append(cleaned_word)

# Counting keyword frequencies
keyword_freq = Counter(keywords)

# 4. Create the word cloud with landscape ratio and save it
wordcloud = WordCloud(width=2000,
                      height=500,
                      colormap="Blues",
                      background_color="rgba(255, 255, 255, 0)",
                      mode="RGBA").generate_from_frequencies(keyword_freq)
plt.figure(figsize=(20,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()

# Save the image in the same location as the code
file_name = f"{picture_title}.png"
plt.savefig(file_name, bbox_inches="tight", pad_inches=0, transparent=True)
print(f"Word cloud saved as {file_name}")
