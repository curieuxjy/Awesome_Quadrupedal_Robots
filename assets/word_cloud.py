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

- [A Study of Lightweight, Low-cost Quadrupedal Robot Body Based on a Coaxial Deformation Mechanism](https://ieeexplore.ieee.org/abstract/document/10632940)
- [Accessorizing Quadrupedal Robots with Wearable Electronics](https://onlinelibrary.wiley.com/doi/full/10.1002/aisy.202300633)
- [Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion](https://arxiv.org/abs/2401.17583)
- [Arm-Constrained Curriculum Learning for Loco-Manipulation of the Wheel-Legged Robot](https://arxiv.org/abs/2403.16535)
- [Body Transformer: Leveraging Robot Embodiment for Policy Learning](https://arxiv.org/abs/2408.06316)
- [Cafe-Mpc: A Cascaded-Fidelity Model Predictive Control Framework with Tuning-Free Whole-Body Control](https://arxiv.org/abs/2403.03995)
- [Contrastive Initial State Buffer for Reinforcement Learning](https://rpg.ifi.uzh.ch/docs/ICRA24_Messikommer.pdf)
- [Convergent iLQR for Safe Trajectory Planning and Control of Legged Robots](https://arxiv.org/abs/2304.00346)
- [Deep Compliant Control for Legged Robots](TBD)
- [DiffuseLoco: Real-Time Legged Locomotion Control with Diffusion from Offline Datasets](https://arxiv.org/abs/2404.19264)
- [DrEureka: Language Model Guided Sim-To-Real Transfer](https://eureka-research.github.io/dr-eureka/assets/dreureka-paper.pdf)
- [DTC: Deep Tracking Control](https://www.science.org/doi/10.1126/scirobotics.adh5401)
- [Dynamic Fall Recovery Control for Legged Robots via Reinforcement Learning](https://www.mdpi.com/2313-7673/9/4/193)
- [Enhancing Quadruped Robot Locomotion on Deformable Terrains Through Contact Perception and Terrain Classification](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4682648)
- [Expert Composer Policy: Scalable Skill Repertoire for Quadruped Robots](https://arxiv.org/abs/2403.11412)
- [Fast Traversability Estimation for Wild Visual Navigation](https://arxiv.org/abs/2305.08510)
- [GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot](https://arxiv.org/abs/2403.13358)
- [H2- and H∞-Optimal Model Predictive Controllers for Robust Legged Locomotion](https://ieeexplore.ieee.org/document/10543084)
- [Hierarchical Open-Vocabulary 3D Scene Graphs for Language-Grounded Robot Navigation](https://arxiv.org/pdf/2403.17846.pdf)
- [Identifying Terrain Physical Parameters from Vision - Towards Physical-Parameter-Aware Locomotion and Navigation](https://arxiv.org/abs/2408.16567)
- [Jumping Locomotion of Quadruped Robot During Running Based on Multiple Model Fusion](https://ieeexplore.ieee.org/abstract/document/10633053)
- [Learning Advanced Locomotion for Quadrupedal Robots: A Distributed Multi-Agent Reinforcement Learning Framework with Riemannian Motion Policies](https://www.mdpi.com/2218-6581/13/6/86)
- [Learning Bipedal Walking on a Quadruped Robot via Adversarial Motion Priors](https://arxiv.org/abs/2407.02282)
- [Learning Force Control for Legged Manipulation](https://arxiv.org/abs/2405.01402)
- [Learning Quadrupedal High-Speed Running on Uneven Terrain](https://www.mdpi.com/2313-7673/9/1/37)
- [Learning Risk-Aware Quadrupedal Locomotion using Distributional Reinforcement Learning](https://arxiv.org/abs/2309.14246)
- [Learning robust autonomous navigation and locomotion for wheeled-legged robots](https://www.science.org/doi/10.1126/scirobotics.adi9641)
- [Learning to walk in confined spaces using 3D representation](https://arxiv.org/abs/2403.00187)
- [Learning-Based Locomotion Controllers for Quadruped Robots in Indoor Stair Climbing via Deep Reinforcement Learning](https://ieeexplore.ieee.org/abstract/document/10594976)
- [Legged Robot State Estimation With Invariant Extended Kalman Filter Using Neural Measurement Network](https://arxiv.org/abs/2402.00366)
- [ManyQuadrupeds: Learning a Single Locomotion Policy for Diverse Quadruped Robots](https://arxiv.org/abs/2310.10486)
- [MQE: Unleashing the Power of Interaction with Multi-agent Quadruped Environment](https://arxiv.org/abs/2403.16015)
- [Online Hierarchical Planning for Multicontact Locomotion Control of Quadruped Robots](https://ieeexplore.ieee.org/abstract/document/10614673)
- [OptiState: State Estimation of Legged Robots using Gated Networks with Transformer-based Vision and Kalman Filtering](https://arxiv.org/abs/2401.16719)
- [Oscillating latent dynamics in robot systems during walking and reaching](https://www.nature.com/articles/s41598-024-61610-5)
- [Pedipulate: Enabling Manipulation Skills using a Quadruped Robot's Leg](https://arxiv.org/abs/2402.10837)
- [Pegasus: a Novel Bio-inspired Quadruped Robot with Underactuated Wheeled-Legged Mechanism *](https://ieeexplore.ieee.org/document/10611633)
- [ProNav: Proprioceptive Traversability Estimation for Legged Robot Navigation in Outdoor Environments](https://arxiv.org/abs/2307.09754)
- [Reduced Model Predictive Control Toward Highly Dynamic Quadruped Locomotion](https://ieeexplore.ieee.org/document/10418132/)
- [Rethinking Robustness Assessment: Adversarial Attacks on Learning-based Quadrupedal Locomotion Controllers](https://arxiv.org/abs/2405.12424)
- [Sim-to-Real: A Performance Comparison of PPO, TD3, and SAC Reinforcement Learning Algorithms for Quadruped Walking Gait Generation](https://www.scirp.org/journal/paperinformation?paperid=131938)
- [Similar but Different: A Survey of Ground Segmentation and Traversability Estimation for Terrestrial Robots](https://arxiv.org/abs/2312.16839)
- [Skill Latent Space Based Multigait Learning for a Legged Robot](https://ieeexplore.ieee.org/abstract/document/10612828)
- [SYNLOCO‐VE: Synthesizing central pattern generator with reinforcement learning and velocity estimator for quadruped locomotion](https://onlinelibrary.wiley.com/doi/abs/10.1002/oca.3181)
- [Track2Act: Predicting Point Tracks from Internet Videos enables Diverse Zero-shot Robot Manipulation](https://arxiv.org/abs/2405.01527)
- [UMI on Legs: Making Manipulation Policies Mobile with Manipulation-Centric Whole-body Controllers](https://arxiv.org/abs/2407.10353)
- [Understanding URDF: A Dataset and Analysis](https://ieeexplore.ieee.org/abstract/document/10478618)
- [Viability leads to the emergence of gait transitions in learning agile quadrupedal locomotion on challenging terrains](https://www.nature.com/articles/s41467-024-47443-w)
- [ViPlanner: Visual Semantic Imperative Learning for Local Navigation](https://arxiv.org/abs/2310.00982)
- [Visual Whole-Body Control for Legged Loco-Manipulation](https://arxiv.org/abs/2403.16967)
- [VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](https://arxiv.org/abs/2312.03275)
"""

# 2. Ask the user for the title of the picture
# picture_title = input("Please provide the title for the picture (without the .png extension): ")
picture_title = "2024"

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
