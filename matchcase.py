def get_day_name(day):
    match day:
        case 1:
            return "monday"
        case 2:
            return "tuesday"
        case 3:
            return "wednesday"
        case 4:
            return "thursday"
        case 5:
            return "friday"
        case 6:
            return "saturday"
        case 7:
            return "sunday"
        case 8:
            return "invalid day "
        
print(get_day_name(6))   