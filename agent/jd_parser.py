class JDParser:
    def extract_requirements(self, jd_text):
        lines = jd_text.split("\n")
        return [line.strip() for line in lines if "-" in line]
