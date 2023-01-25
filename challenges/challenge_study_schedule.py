def study_schedule(permanence_period, target_time):
    if not target_time and target_time != 0:
        return None

    students_studying = 0

    for start, end in permanence_period:
        if not isinstance(start, int) or not isinstance(end, int):
            return None
        if start <= target_time <= end:
            students_studying += 1

    return students_studying


# print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 1))