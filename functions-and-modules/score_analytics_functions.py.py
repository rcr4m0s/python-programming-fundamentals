def get_score_stats(scores):
    highest = max(scores)
    average = sum(scores) / len(scores)
    return highest, round(average, 2)

test_scores = [88, 65, 92, 70, 95]

# Pwede mong i-unpack ang dalawang returned values sa dalawang variables
top_score, avg_score = get_score_stats(test_scores)

print(f"Top Score: {top_score}")
print(f"Average: {avg_score}")