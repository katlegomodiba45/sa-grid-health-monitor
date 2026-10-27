def calculate_stress_score(stage, temperature_c, hour=None):
    score = 0
    if stage is not None:
        try:
            score += int(stage) * 12
        except:
            score += 15
    if temperature_c is not None:
        if temperature_c >= 32:
            score += 25
        elif temperature_c >= 28:
            score += 15
        elif temperature_c >= 25:
            score += 8
    if hour is not None:
        if 17 <= hour <= 21:
            score += 15
        elif 6 <= hour <= 9:
            score += 10
    return min(score, 100)

def stress_label(score):
    if score >= 70:
        return "High"
    elif score >= 40:
        return "Moderate"
    else:
        return "Low"