import pandas as pd
import pytest
from qsep_feedback_subject_classifier.row_collapser import collapse_rows
from qsep_feedback_subject_classifier.row_collapser import SUBJECT_COLUMN, COLUMN_TO_COLLAPSE


def test_collapse_rows_basic_functionality():
    """
    Test that collapse_rows correctly collapses rows by Subject and sums numerical values.
    """
    # Create test input data
    test_data = {
        COLUMN_TO_COLLAPSE: ['Account', 'Account', 'FAQ Inquiry', 'Login', 'Login', 'Login'],
        'Identity': [1, 3, 5, 3, 3, 1],
        'Password': [None, None, 1, None, None, 2],
        'Profile': [1, 1, None, None, None, 1],
        'Count': [2, None, 1, None, 2, 2]
    }
    
    input_df = pd.DataFrame(test_data)
    
    # Call the function under test
    result_df = collapse_rows(input_df)
    
    # Verify the basic structure
    assert len(result_df) == 3, f"Expected 3 rows, got {len(result_df)}"
    assert COLUMN_TO_COLLAPSE in result_df.columns, "Subject column should be present"

    # Get unique subjects and sort for consistent testing
    expected_subjects = ['Account', 'FAQ Inquiry', 'Login']
    actual_subjects = sorted(result_df[COLUMN_TO_COLLAPSE].tolist())
    expected_subjects_sorted = sorted(expected_subjects)
    
    assert actual_subjects == expected_subjects_sorted, f"Expected subjects {expected_subjects_sorted}, got {actual_subjects}"


def test_collapse_rows_summed_values():
    """
    Test that collapse_rows correctly sums numerical values for each subject group.
    """
    # Create test input data
    test_data = {
        COLUMN_TO_COLLAPSE: ['Account', 'Account', 'FAQ Inquiry', 'Login', 'Login', 'Login'],
        'Identity': [1, 3, 5, 3, 3, 1],
        'Password': [None, None, 1, None, None, 2],
        'Profile': [1, 1, None, None, None, 1],
        'Count': [2, None, 1, None, 2, 2]
    }
    
    input_df = pd.DataFrame(test_data)
    
    # Call the function under test
    result_df = collapse_rows(input_df)
    
    # Create a dictionary for easier verification
    result_dict = {}
    for index, row in result_df.iterrows():
        subject = row[COLUMN_TO_COLLAPSE]
        result_dict[subject] = row.to_dict()
    
    # Verify Account row (rows 0 and 1 combined: Identity 1+3=4, Profile 1+1=2, Count 2+0=2)
    account_row = result_dict['Account']
    assert account_row['Identity'] == 4, f"Account Identity should be 4, got {account_row['Identity']}"
    assert account_row['Password'] == 0, f"Account Password should be 0, got {account_row['Password']}"  # Both were None
    assert account_row['Profile'] == 2, f"Account Profile should be 2, got {account_row['Profile']}"
    assert account_row['Count'] == 2, f"Account Count should be 2, got {account_row['Count']}"  # 2 + None(0) = 2
    
    # Verify FAQ Inquiry row (row 2: no summing needed)
    faq_row = result_dict['FAQ Inquiry']
    assert faq_row['Identity'] == 5, f"FAQ Identity should be 5, got {faq_row['Identity']}"
    assert faq_row['Password'] == 1, f"FAQ Password should be 1, got {faq_row['Password']}"
    assert faq_row['Profile'] == 0, f"FAQ Profile should be 0, got {faq_row['Profile']}"  # Was None
    assert faq_row['Count'] == 1, f"FAQ Count should be 1, got {faq_row['Count']}"
    
    # Verify Login row (rows 3, 4, and 5 combined: Identity 3+3+1=7, Password 0+0+2=2, Profile 0+0+1=1, Count 0+2+2=4)
    login_row = result_dict['Login']
    assert login_row['Identity'] == 7, f"Login Identity should be 7, got {login_row['Identity']}"
    assert login_row['Password'] == 2, f"Login Password should be 2, got {login_row['Password']}"  # None + None + 2 = 2
    assert login_row['Profile'] == 1, f"Login Profile should be 1, got {login_row['Profile']}"  # None + None + 1 = 1
    assert login_row['Count'] == 4, f"Login Count should be 4, got {login_row['Count']}"  # None + 2 + 2 = 4


def test_collapse_rows_empty_dataframe():
    """
    Test that collapse_rows handles empty DataFrame correctly.
    """
    empty_df = pd.DataFrame()
    
    # This should not crash and should return an empty DataFrame
    result_df = collapse_rows(empty_df)
    
    assert len(result_df) == 0, "Empty DataFrame should return empty result"


def test_collapse_rows_single_row():
    """
    Test that collapse_rows handles a single row DataFrame correctly.
    """
    test_data = {
        COLUMN_TO_COLLAPSE: ['Single'],
        'Identity': [1],
        'Count': [5]
    }
    
    input_df = pd.DataFrame(test_data)
    result_df = collapse_rows(input_df)
    
    assert len(result_df) == 1, "Single row should return single row"
    assert result_df.iloc[0][COLUMN_TO_COLLAPSE] == 'Single', "Subject should be preserved"
    assert result_df.iloc[0]['Identity'] == 1, "Identity should be 1"
    assert result_df.iloc[0]['Count'] == 5, "Count should be 5"