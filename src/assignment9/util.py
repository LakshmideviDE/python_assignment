from datetime import datetime, timezone


def time_diff(timestamp1, timestamp2):
    # Parse the timestamps
    time_format = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(timestamp1, time_format)
    time2 = datetime.strptime(timestamp2, time_format)

    # Convert timestamps to a common timezone (UTC)
    time1_utc = time1.astimezone(tz=timezone.utc)
    time2_utc = time2.astimezone(tz=timezone.utc)

    # Calculate the time difference in seconds
    difference_seconds = abs(int((time1_utc - time2_utc).total_seconds()))

    return difference_seconds