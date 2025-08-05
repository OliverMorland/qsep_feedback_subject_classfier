support_categories = {
        "Account Activation": ["Account Activation, Certificate"],
        "Account Review": [],
        "Account Role Review": [],
        "Add/Remove": [],
        "Approve/Reject": [],
        "Certificate": [],
        "Customize Training Plan": [],
        "Email Confirmation": [],
        "Evaluation": [],
        "Facility Search": [],
        "FAQ Inquiry": [],
        "Feedback": [],
        "HARP": ["Login, HARP", "Sign-Up, HARP"],
        "Incorrect Help Desk": [],
        "Issue": [],
        "Language Services": [],
        "Login": [],
        "LSC Attestation": [],
        "Merge": [],
        "MFA": [],
        "Navigation": [],
        "Other": [],
        "Pre/Post Test": [],
        "Prerequisites": [],
        "Primary/Secondary States": [],
        "Question": [],
        "Request": [],
        "SCO Error": ["Corrupt SCO/Won't Advance"],
        "SMQT": [],
        "SSR - General Inquiries": [
                                    "SSR Change",
                                    "SSR Change, FAQ Inquiry",
                                    "SSR Change, Question",
                                    "SSR Change, Voicemail message",
                                    "SSR-EP",
                                    "SSR-EP, Question",
                                    "SSR-EP, Voicemail message",
                                    "SSR-LSC, Voicemail message"
                                ],
        "Suspended Account": [],
        "Tracking": [],
        "Training Plan Progress Bar": [],
        "Transcript": [],
        "Update Facility Information": [],
        "Update Profile Information": [],
        "Update Record": [],
        "Voicemail message": []
        }


def categorize(input_text):
    if input_text == "Count":
        return None
    for key, list in support_categories.items():
        if input_text in list:
            return key
        
    for key in support_categories.keys():
        if key in input_text:
            return key
        
    for key in support_categories.keys():
        if input_text in key:
            return key
        
    return "NO CATEGORY FOUND"