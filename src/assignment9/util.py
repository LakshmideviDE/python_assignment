from datetime import datetime, timedelta
def time_diff():
    # Read the number of test cases
    test_cases = int(input().strip())
    for _ in range(test_cases):
        timestamp1 = input().strip()
        timestamp2 = input().strip()
        format_str = '%a %d %b %Y %H:%M:%S %z'
        time1 = datetime.strptime(timestamp1, format_str)
        time2 = datetime.strptime(timestamp2, format_str)
        time_difference = abs(int((time1 - time2).total_seconds()))
    return (time_difference)





