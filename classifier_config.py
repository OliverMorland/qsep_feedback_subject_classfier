MODEL_PATH = "feedback_classifier_assets/restaurant_classifier_model"
ENCODED_DATASET_PATH = "feedback_classifier_assets/cache/restaurant_encoded_dataset"
DATASET_PATH = "feedback_classifier_assets/restaurant_feedback_samples.csv"
PRE_TRAINED_DISTILBERT = "distilbert-base-uncased-distilled-squad"

CATEGORIES = {
    "Staff Complaint": [
        "the {staff} were very rude and unhelpful",
        "I had a {terrible} experience with the {staff}",
        "the {staff} did not assist me at all",
        "I felt disrespected by the {staff}",
        "the {staff} were not trained properly",
        "I want to file a complaint against the {staff}",
        "the {staff} ignored my requests",
        "the {staff} were unprofessional",
        "the {staff} were not attentive",
    ],
    "Food Complaint": [
        "the {food} was cold and tasteless",
        "I found a hair in my {food}",
        "the {food} took too long to arrive",
        "I was served the wrong dish",
        "the {food} was undercooked",
        "I want to complain about the {food}",
        "the {food} was not as described",
        "the {food} was overpriced for the quality",
        "the {food} was not fresh",
    ],
    "Price Complaint": [
        "the {prices} are too high",
        "I was overcharged for my meal",
        "the menu {prices} do not match the bill",
        "I want to complain about the {prices}",
        "the {prices} are not justified for the quality",
        "I feel cheated by the {prices}",
        "the {prices} are not competitive",
        "I was not informed about the {prices} beforehand",
        "the {prices} of my {food} were too much",
    ],
    "Location Complaint": [
        "the {location} is inconvenient",
        "I had trouble finding the {location} of the restaurant",
        "the parking situation is {terrible}",
        "the {location} is unsafe at night",
        "I want to complain about the {location}",
        "the {location} does not match the description",
        "the {location} is too noisy",
        "the {location} is not accessible",
        "the {location} is too far from public transport",
    ],
    "Website Complaint": [
        "the restaurant's {website} is not user-friendly",
        "I had trouble placing an order on the {website}",
        "the {website} does not provide accurate information",
        "I want to complain about the {website}",
        "the {website} is slow and unresponsive",
        "the {website} does not have my preferred payment method",
        "the {website} menu is outdated",
        "the {website} does not allow me to leave feedback",
        "the {website} is difficult to navigate",
    ],
}

PLACEHOLDER_OPTIONS = {
    "terrible": ["terrible", "awful", "horrible", "bad", "poor", "unsatisfactory"],
    "staff": ["waitstaff", "servers", "employees", "staff members", "restaurant staff"],
    "prices": ["prices", "costs", "charges", "price", "cost"],
    "food": ["food", "meal", "dish", "roast turkey", "lentil soup", "chicken tikka masala", "pizza", "bean burger"],
    "location": ["location", "place", "address","restaurant location", "restaurant place", "restaurant area"],
    "website": ["website", "site", "webpage", "restaurant website", "restaurant site", "restaurant webpage"],
}

FUNNEL_MAPPING = {
    'Other': ["Location Complaint", "Website Complaint"]
}

QUICK_CLASSIFY_PHRASES = {
    "the food was disgusting": "Food Complaint",
    "zero out of ten for food quality": "Food Complaint",
    "despicable staff": "Staff Complaint",
}