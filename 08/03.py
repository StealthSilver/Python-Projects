def life_in_weeks(age):
    total_weeks = 90 * 52
    weeks_lived = age * 52
    weeks_left = total_weeks - weeks_lived
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(21)