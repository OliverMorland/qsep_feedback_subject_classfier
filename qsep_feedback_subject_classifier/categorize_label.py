import pandas as pd


# support_categories = {
#         "Account Activation": [],
#         "Account Review": [],
#         "Account Role Review": [],
#         "Add/Remove": [],
#         "Approve/Reject": [],
#         "Certificate": [],
#         "Customize Training Plan": [],
#         "Email Confirmation": [],
#         "Evaluation": [],
#         "Facility Search": [],
#         "FAQ Inquiry": [],
#         "Feedback": [],
#         "HARP": [],
#         "Incorrect Help Desk": [],
#         "Issue": [],
#         "Language Services": [],
#         "Login": [],
#         "LSC Attestation": [],
#         "Merge": [],
#         "MFA": [],
#         "Navigation": [],
#         "Other": [],
#         "Pre/Post Test": [],
#         "Prerequisites": [],
#         "Primary/Secondary States": [],
#         "Question": [],
#         "Request": [],
#         "SCO Error": ["Corrupt SCO/Won't Advance"],
#         "SMQT": [],
#         "SSR - General Inquiries": [
#                                     "SSR Change",
#                                     "SSR Change, FAQ Inquiry",
#                                     "SSR Change, Question",
#                                     "SSR Change, Voicemail message",
#                                     "SSR-EP",
#                                     "SSR-EP, Question",
#                                     "SSR-EP, Voicemail message",
#                                     "SSR-LSC, Voicemail message"
#                                 ],
#         "Suspended Account": [],
#         "Tracking": [],
#         "Training Plan Progress Bar": [],
#         "Transcript": [],
#         "Update Facility Information": [],
#         "Update Profile Information": [],
#         "Update Record": [],
#         "Voicemail message": []
#         }


def categorize(input_text):
    input_text = str(input_text).strip()
    support_categories = extract_mapping_from_excel()


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
        
    return "Other"

def extract_mapping_from_excel():
    df = pd.read_excel("docs\input\Category_Labeler.xlsx")

    # Convert DataFrame to dict of lists (column-wise)
    data_dict = df.to_dict(orient='list')

    return data_dict

# max_len = max(len(lst) for lst in support_categories.values())

# # Step 2: Pad each list with empty strings to match max_len
# padded_data = {
#     key: value + [""] * (max_len - len(value))
#     for key, value in support_categories.items()
# }

# # Step 3: Convert to DataFrame and write to Excel
# df = pd.DataFrame(padded_data)
# df.to_excel("Category_Labeler.xlsx", index=False)