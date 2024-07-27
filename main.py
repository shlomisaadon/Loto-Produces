import random
from collections import Counter
import time


# פונקציה להגרלת 6 מספרים
def roll_six_numbers():
    return sorted(random.sample(range(1, 38), 6))


# ציין את ההתחלה של מדידת הזמן
start_time = time.time()

# הגרל 2000 פעמים
results = [roll_six_numbers() for _ in range(3600000)]

# ספור את מספר ההופעות של כל צירוף
combination_counts = Counter(tuple(combination) for combination in results)

# מצא את 10 הצירופים הכי נפוצים
top_10_combinations = [list(combination) for combination, count in combination_counts.most_common(14)]

# הדפס את התוצאות
for i, combination in enumerate(top_10_combinations):
    print(f"מערך מספר {i + 1}: {combination}, מספר הופעות: {combination_counts[tuple(combination)]}")

###############
###############
###############
# סיים את מדידת הזמן

end_time = time.time()

# הצג את הזמן שעבר
elapsed_time = end_time - start_time
print(f"זמן הרצת ה-{len(results)} הגרלות: {elapsed_time} שניות")
