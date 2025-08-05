# Claude Code Project Context

## Project Overview
QSEP Feedback Subject Classifier - A tool to categorize large lists of feedback descriptions using a distilbert based categorizer.

## Development Commands

### Testing
```bash
python -m pytest "tests/unit/ritual_unit_test.py" -v
```

## Project Structure
- `tests/unit/` - Unit tests
- `qsep_feedback_subject_classifier/` - Main package directory

## Dependencies
- phrase_classifier (from GitHub: stussc/phrase_classifier.git)
- pytest (dev dependency)

## Authors
- Oliver Morland: omorland@swingtech.com
- Joshua Ramthun: jramthun@swingtech.com