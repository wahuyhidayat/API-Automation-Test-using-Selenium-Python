BASE_URL = "https://gorest.co.in/public/v2"
TOKEN = "acc8cdda6f855e4f7ba51268ffdc48aefa012b31271f0a6d350da176f43f2472"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

INVALID_TOKEN = "9a7aac15f814107fce40b2af065ea1f13bb1146a0f7db731418ab4adda461e65"
INVALID_HEADERS = {
    "Authorization": f"Bearer {INVALID_TOKEN}",
    "Content-Type": "application/json"
}

INVALID_ID = 688888