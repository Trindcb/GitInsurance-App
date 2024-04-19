policies = []

def add_policy(policy_name):
    policies.append(policy_name)

def remove_policy(policy_name):
    if policy_name in policies:
        policies.remove(policy_name)
    else:
        print("Policy not found.")

def list_policies():
    return policies
