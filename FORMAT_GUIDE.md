# Output Format Consistency Guide

## Problem Solved

Previously, the AI would sometimes return inconsistent formats:
- ❌ `**Total Score: 20 / 25**` (wrong - missing colon, extra asterisks)
- ❌ `**Total Score:**20 / 25` (wrong - missing space)
- ✅ `**Total Score:** 20 / 25` (correct)

## Solution Implemented

### 1. **Explicit Format Instructions**
The evaluation prompt now includes:
- Clear example showing the exact format
- Specific rules about colon placement
- Warning against adding extra asterisks

### 2. **Robust Parser**
The parser (`automate_scoring.py`) now:
- Handles multiple format variations
- Calculates total score from breakdown if missing
- Provides warnings when format issues are detected

### 3. **Validation**
Automatic validation ensures:
- Total score is always present
- All 5 category scores are captured
- Feedback sections are properly extracted

## Expected Output Format

```
**Total Score:** X / 25

**Category Breakdown:**
- Prompt Clarity: X/5
- Real-World Relevance: X/5
- Reflection Quality: X/5
- Responsible Use: X/5
- Writing Clarity: X/5

**Summary Feedback:**
2-4 encouraging sentences about the student's work...

**Improvement Suggestion:**
1-2 specific, actionable suggestions for improvement...
```

## Format Rules

1. **Total Score Line**
   - Format: `**Total Score:** X / 25`
   - Colon after "Score", space before number
   - No extra asterisks at the end

2. **Category Breakdown**
   - Format: `- Category Name: X/5`
   - Space after colon
   - No extra spaces around numbers

3. **Section Headers**
   - Use double asterisks: `**Header:**`
   - Include colon at the end
   - No extra formatting

## Testing Format Consistency

To test if the format is working correctly:

```bash
source .venv/bin/activate
python -c "
from automate_scoring import AssignmentScorer
scorer = AssignmentScorer()
evaluation = scorer.score_assignment('student-assignments/stu_no_2949.docx')
print(evaluation['raw_response'][:300])
"
```

## Troubleshooting

### Issue: Total score is blank in JSON

**Cause:** Parser couldn't find the total score line

**Solution:** The parser now automatically calculates from category breakdown

**Check:** Run `python view_results.py` - if scores show correctly, the fallback worked

### Issue: Category scores missing

**Cause:** Format variation in category lines

**Solution:** Parser uses flexible splitting on last colon

**Check:** Look at `raw_response` field in JSON to see actual AI output

## Files Modified

1. **automate_scoring.py** (lines 104-136)
   - Added explicit format example
   - Added format rules section
   - Enhanced parser with fallback calculation

2. **Parser improvements** (lines 235-287)
   - Flexible total score extraction
   - Automatic total score calculation
   - Better error handling

## Verification

Run this command to verify all scores are properly formatted:

```bash
python view_results.py
```

Expected output should show all scores in format: `XX / 25` and `X/5`

## Future Improvements

If format issues persist:
1. Consider using structured output (JSON mode) if available
2. Add pre-validation of AI response
3. Implement retry logic for malformed responses
