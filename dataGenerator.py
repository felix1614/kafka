import random
import string

user_ids = list(range(1, 100))
recipient_ids = list(range(1, 101))


def generateMessage() -> dict:
    random_user_ids = random.choice(user_ids)
    recipients_ids_copy = recipient_ids.copy()
    recipients_ids_copy.remove(random_user_ids)
    random_recipient_ids = random.choice(recipients_ids_copy)

    message = "".join(random.choice(string.ascii_lowercase) for i in range(32))

    return {
        "user_id": random_user_ids,
        "recipient_id": random_recipient_ids,
        "message": message
    }
