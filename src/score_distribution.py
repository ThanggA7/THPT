import matplotlib.pyplot as plt
import mplcursors

def plot_score_distribution(scores, title):
    subjects = list(scores.keys())
    values = list(scores.values())

    plt.figure(figsize=(10, 5))
    plt.bar(subjects, values, color='steelblue')
    plt.xlabel('Điểm')
    plt.ylabel('Số lượng')
    plt.title(title)
    mplcursors.cursor().connect("add", lambda sel: sel.annotation.set_text(f"Số lượng: {sel.target[1]}"))
    plt.show()

def calculate_average_score(scores):
    total_scores = sum(scores.values())
    total_students = sum(scores.values())

    average_score = total_scores / total_students

    return average_score, total_students
