# AI-Powered Resume Screening System
import pandas as pd

# Load dataset
df = pd.read_csv("AI-Powered Resume Screening System/AI_Resume_Screening.csv")

# --- 1️⃣ Define Job Requirements ---
required_skills = {"Python", "Machine Learning", "Deep Learning", "TensorFlow"}

# Function to calculate skill match %
def skill_match(skills_text):
    candidate_skills = set([s.strip().lower() for s in skills_text.split(",")])
    match_count = sum(1 for s in required_skills if s.lower() in candidate_skills)
    return (match_count / len(required_skills)) * 100

df["Skill_Match (%)"] = df["Skills"].apply(skill_match)

# --- 2️⃣ Create Composite Ranking Score ---
# Weighting: 40% AI Score, 25% Skill Match, 20% Experience, 15% Projects
df["Ranking_Score"] = (
    df["AI Score (0-100)"] * 0.4 +
    df["Skill_Match (%)"] * 0.25 +
    df["Experience (Years)"] * 0.20 +
    df["Projects Count"] * 0.15
)

# --- 3️⃣ Sort Candidates ---
df_ranked = df.sort_values(by="Ranking_Score", ascending=False)

# Display Top Candidates
print("Top Candidates Based on Ranking Score:")
print(df_ranked[["Name", "Job Role", "Skills", "Skill_Match (%)",
                 "Experience (Years)", "Projects Count",
                 "AI Score (0-100)", "Ranking_Score"]].head(10))

# --- 4️⃣ Save Results ---
df_ranked.to_csv("Ranked_Candidates.csv", index=False)
print("\n✅ Ranked_Candidates.csv saved with full ranking.")
