import json

FILE_NAME = "policies.json"


def create_policy():
    policy = {
        "id": int(input("Enter Policy ID: ")),
        "name": input("Enter Customer Name: "),
        "type": input("Enter Policy Type: "),
        "premium": float(input("Enter Premium: "))
    }

    with open(FILE_NAME, "r") as file:
        policies = json.load(file)

    policies.append(policy)

    with open(FILE_NAME, "w") as file:
        json.dump(policies, file, indent=4)

    print("Policy created successfully.")


def get_all_policies():
    with open(FILE_NAME, "r") as file:
        policies = json.load(file)

    for policy in policies:
        print(policy)


def find_policy():
    policy_id = int(input("Enter Policy ID: "))

    with open(FILE_NAME, "r") as file:
        policies = json.load(file)

    for policy in policies:
        if policy["id"] == policy_id:
            print("Policy Found:")
            print(policy)
            return

    print("Policy not found.")


def update_policy():
    policy_id = int(input("Enter Policy ID: "))

    with open(FILE_NAME, "r") as file:
        policies = json.load(file)

    for policy in policies:
        if policy["id"] == policy_id:
            policy["name"] = input("Enter new customer name: ")
            policy["type"] = input("Enter new policy type: ")
            policy["premium"] = float(input("Enter new premium: "))

            with open(FILE_NAME, "w") as file:
                json.dump(policies, file, indent=4)

            print("Policy updated successfully.")
            return

    print("Policy not found.")


def delete_policy():
    policy_id = int(input("Enter Policy ID: "))

    with open(FILE_NAME, "r") as file:
        policies = json.load(file)

    for policy in policies:
        if policy["id"] == policy_id:
            policies.remove(policy)

            with open(FILE_NAME, "w") as file:
                json.dump(policies, file, indent=4)

            print("Policy deleted successfully.")
            return

    print("Policy not found.")