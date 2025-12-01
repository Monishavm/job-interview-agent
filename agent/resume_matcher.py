from adk import Agent
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(resume, jd):
    e1 = model.encode(resume, convert_to_tensor=True)
    e2 = model.encode(jd, convert_to_tensor=True)
    score = util.cos_sim(e1, e2).item()
    return round(score * 100, 2)

class ResumeMatcher(Agent):
    def match(self, resume, jd):
        return compute_similarity(resume, jd)
