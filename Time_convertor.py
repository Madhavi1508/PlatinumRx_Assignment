def convert_minutes(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60

    if hours > 0:
        if hours == 1:
            return f"{hours} hr {remaining_minutes} minutes"
        else:
            return f"{hours} hrs {remaining_minutes} minutes"
    else:
        return f"{remaining_minutes} minutes"
t=int(input())
print(convert_minutes(t))
