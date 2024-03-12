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
- [ManyQuadrupeds: Learning a Single Locomotion Policy for Diverse Quadruped Robots](https://arxiv.org/abs/2310.10486)
- [Accessorizing Quadrupedal Robots with Wearable Electronics](https://onlinelibrary.wiley.com/doi/full/10.1002/aisy.202300633)
- [Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion](https://arxiv.org/abs/2401.17583)
- [Deep Compliant Control for Legged Robots](TBD)
- [DTC: Deep Tracking Control](https://www.science.org/doi/10.1126/scirobotics.adh5401)
- [Learning Quadrupedal High-Speed Running on Uneven Terrain](https://www.mdpi.com/2313-7673/9/1/37)
- [Learning Risk-Aware Quadrupedal Locomotion using Distributional Reinforcement Learning](https://arxiv.org/abs/2309.14246)
- [Learning to walk in confined spaces using 3D representation](https://arxiv.org/abs/2403.00187)
- [Legged Robot State Estimation With Invariant Extended Kalman Filter Using Neural Measurement Network](https://arxiv.org/abs/2402.00366)
- [OptiState: State Estimation of Legged Robots using Gated Networks with Transformer-based Vision and Kalman Filtering](https://arxiv.org/abs/2401.16719)
- [Pedipulate: Enabling Manipulation Skills using a Quadruped Robot's Leg](https://arxiv.org/abs/2402.10837)
- [ProNav: Proprioceptive Traversability Estimation for Legged Robot Navigation in Outdoor Environments](https://arxiv.org/abs/2307.09754)
- [Reduced Model Predictive Control Toward Highly Dynamic Quadruped Locomotion](https://ieeexplore.ieee.org/document/10418132/)
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
