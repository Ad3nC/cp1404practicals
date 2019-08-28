"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))

    print(score_calculator(score))


def score_calculator(score):
    if score < 0 or score > 100:
        return "invalid score"

    elif score >= 90:
        score = "Excellent"
        return score
    elif score >= 50:
        score = "Pass"
        return score
    else:
        score = "bad"
        return score



main()
