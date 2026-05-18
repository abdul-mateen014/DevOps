# Test Cases Documentation

## Test 1: Homepage Loads
- Navigate to http://localhost
- Verify page title is "Semester Notes App"
- Verify heading "Notes App" is visible
- ✅ PASSED

## Test 2: Form Elements Visible
- Verify input field is visible
- Verify Add button is visible
- ✅ PASSED

## Test 3: Add Note
- Enter note text
- Click Add button
- Verify note appears in list
- ✅ PASSED

## Test 4: Form Validation
- Try to submit empty form
- Verify error message appears
- ✅ PASSED

## Test 5: Delete Note
- Click delete button on note
- Verify note is removed from list
- ✅ PASSED

## Test 6: API Health
- Make request to http://localhost:3000/api/health
- Verify status code 200
- Verify response contains "ok"
- ✅ PASSED

All 6 tests completed successfully!
