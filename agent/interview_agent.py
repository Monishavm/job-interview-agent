from adk import Agent

class InterviewAgent(Agent):
    def ask_question(self, role):
        return f"What makes you a strong candidate for the role of {role}?"

    def evaluate_answer(self, answer):
        if len(answer.split()) < 20:
            return "Your answer is too short. Try adding more detail."
        return "Good answer! You explained your strengths well."

