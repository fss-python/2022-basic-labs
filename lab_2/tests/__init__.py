from pathlib import Path

test_data_path = Path(__file__).parent / 'test_data'
non_numerical = [100, -200, "c", "d", "e", 400]
non_positive = [100, -200, 10, -5, 10, 400]