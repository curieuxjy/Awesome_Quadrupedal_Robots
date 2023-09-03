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
    "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"
])

# 1. Get the paper list from the user
# papers_input = input("Please provide the list of papers:\n")
papers_input = """
- [ANYmal - a highly mobile and dynamic quadrupedal robot](https://doi.org/10.1109/IROS.2016.7758092)
- [Design of HyQ – a hydraulically and electrically actuated quadruped robot](https://doi.org/10.1177/0959651811402275)
- [High-slope terrain locomotion for torque-controlled quadruped robots](https://link.springer.com/article/10.1007/s10514-016-9573-1)
- [Meta Learning Shared Hierarchies](https://doi.org/10.48550/arXiv.1710.09767)
- [Robot-Centric Elevation Mapping with Uncertainty Estimates](https://doi.org/10.1142/9789814623353_0051)
- [Slip Detection and Recovery for Quadruped Robots](https://doi.org/10.1016/j.robot.2005.07.002)
- [State Estimation for Legged Robots - Consistent Fusion of Leg Kinematics and IMU](https://doi.org/10.7551/mitpress/9816.001.0001)
- [Survey of Numerical Methods for Trajectory Optimization](https://arc.aiaa.org/doi/10.2514/2.4231)
- [Terrain-adaptive locomotion skills using deep reinforcement learning](https://dl.acm.org/doi/10.1145/2897824.2925881)
- [Wholebody trajectory optimization for non-periodic dynamic motions on quadrupedal systems](https://ieeexplore.ieee.org/document/7989623)
"""

# 2. Ask the user for the title of the picture
# picture_title = input("Please provide the title for the picture (without the .png extension): ")
picture_title = "2017"

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
