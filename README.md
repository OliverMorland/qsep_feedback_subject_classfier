# QSEP Feedback Categorizer

## Description

This tool takes in tables which record user feedback for the QSEP website and outputs a spreadsheet with compressed tables by categorizing subjects into broader categories.

## Installation

### Prerequisites
- Python 3.7 or higher
- Git

### Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd qsep_feedback_subject_classfier
```

2. Run auto setup to automatically install dependencies to a virtual environment.
```bash
# Windows
scripts\setup.bat
```

## Usage
1. Copy the path of the excel file you wish to have categorized.
2. Run the *categorize.bat* script.
```bash
scripts\categorize.bat
```
3. Your new file should've been created and open automatically.

### Configuration
The program decides how to categorize subjects based on the words they use. You can overwrite some of this by adding the particular words you want over-ridden to the desired columns in *@category_Labeler.xlsx.*


## Authors

- Oliver Morland: omorland@swingtech.com
- Joshua Ramthun: jramthun@swingtech.com