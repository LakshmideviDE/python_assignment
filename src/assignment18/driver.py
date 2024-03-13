from python_assignments.src.assignment18.util import filter_valid_emails
if __name__ == "__main__":
    n = int(input())
    email_list = [input().strip() for _ in range(n)]

    result = filter_valid_emails(n, email_list)
    for email in result:
        print(email)