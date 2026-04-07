# python-daily-challenges

Repo for Python daily challenge

## Running a Day

Standard: run a day from the repo root with the workspace virtual environment.

Example:
./.venv/bin/python day_6_trip_calculator/trip_calculator.py

For interactive days, run the script and follow the prompts.

## Running Tests

Standard: run tests from the repo root.

Run all current tests:
./run_all_tests.sh

The shared test convention is:

- Put each test file in the same day folder as the code it covers.
- Name every test file test_<module>.py.
- Run the full suite from the repo root with `./.venv/bin/python -m pytest -q` or `./run_all_tests.sh`.

Current repo-wide test coverage includes day 1, day 2, day 6, day 8, day 10, day 12, day 13, day 15, day 16, day 17, and day 19.

Run only day 15 tests:
./run_day_15_tests.sh

Run pytest directly for a specific test file:
./.venv/bin/python -m pytest -q day_15_library_system/test_day_15_library_system.py

## Naming And Style

Standard:

- Each challenge lives in its own day folder named day*<number>*<topic>.
- Python files use snake_case names that match the folder and challenge where practical.
- Functions use snake_case.
- Classes use CapWords.
- Modules should be import-safe: definitions at the top, pure logic/helpers in the middle, and CLI or demo code in main() behind a main guard.
- Printing, input, and file I/O belong in the runner layer, not inside reusable logic unless the exercise is specifically about I/O.

This keeps each exercise runnable on its own while making the repo easier to test and reuse.
