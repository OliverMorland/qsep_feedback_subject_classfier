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

## Coding Style Preferences

### Code Structure
- **Avoid inline loops and list comprehensions** - Always expand to explicit for loops for better readability and debugging
- **Avoid chaining function calls** - Use intermediate variables instead of calling functions within function parameters
- **Prefer multiple small functions** over large complex functions - Break down functionality into focused, single-responsibility functions
- **No nested functions** - Keep all functions at module level for clarity

### Code Clarity
- **Use descriptive variable names** - Prefer clarity over brevity
- **Add clear documentation** for each function with proper docstrings
- **Explicit is better than implicit** - Make operations clear and easy to follow
- **One operation per line** - Avoid complex multi-step operations on single lines

### Debugging Considerations
- **Make code step-through friendly** - Structure code so it's easy to debug line by line
- **Use intermediate variables** for complex operations to enable inspection during debugging
- **Avoid lambda functions** - Use named functions instead for better stack traces

## Authors
- Oliver Morland: omorland@swingtech.com
- Joshua Ramthun: jramthun@swingtech.com