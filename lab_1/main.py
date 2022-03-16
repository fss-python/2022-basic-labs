from pathlib import Path


def read_ecg_raw_file(file_path: Path):
    try:
        with open(file_path) as f:
            ecg_raw = f.readlines()
    except FileNotFoundError:
        print(f'This file "{file_path}" does not exist!')
    except Exception as e:
        print(f'This file "{file_path}" does not look like a file!')
        print(e)
        raise ValueError('Incorrect data file') from e

    # first line is meta-information and not an ECG item, therefore ignoring it
    only_number_lines = ecg_raw[1:]

    # creating intermediate variable for storing raw_signal
    raw_signal = []
    # each line is a number with a next line escape sequence
    for line in only_number_lines:
        # removing '\n' from line before casting to float
        numeric_value = float(line.strip())

        # adding element to a raw signal
        raw_signal.append(numeric_value)
    return raw_signal


# Lab 1 implementation goes below
def calculate_threshold(signal: list):
    """Calculating threshold for RR peaks detection"""
    threshold=max(signal) * 0.8
    return threshold

def detect_maximums(signal: list, threshold: int):
    """Labeling RR peaks"""
    ecg_maximums=[]
    for i in range (len(signal)):
        if signal [i] <= threshold:
            ecg_maximums.append(0)
        elif signal[i+1]<signal[i] and signal[i-1]<signal[i]:
            ecg_maximums.append(1)
        else:
            ecg_maximums.append(0)

    return ecg_maximums

def calculate_times(signal: list, sample_rate: int):
    """Calculating timestamp for each item in ECG"""
    ecg_times=[]
    ecg_times.append(0)
    for i in range (len(signal)):
        ecg_times.append(ecg_times[i]+1000/sample_rate)
    return ecg_times


def calculate_rr(maximums: list, times: list):
    """Extract RR intervals"""
    high_markers_ms=[0]
    rr_without_threshold = [0]
    ecg_rr=[]
    for i in range(len(maximums)):
        if maximums[i] == 1:
            high_markers_ms.append(times[i])
    for i in  range(len(high_markers_ms)):
        rr_without_threshold.append (high_markers_ms[i]-high_markers_ms[i-1])
    for i in range(len(rr_without_threshold)):
        if rr_without_threshold[i] > 400:
            ecg_rr.append(rr_without_threshold[i])
        else:
             continue


    return ecg_rr


# Lab 1 demonstration goes below
if __name__ == '__main__':

    SAMPLE_RATE = 1000
    DATA_PATH = Path(__file__).parent / 'data' / 'participant_28_baseline_raw.txt'

    print(f'Opening {DATA_PATH} with ECG signal')

    ecg_raw = read_ecg_raw_file(DATA_PATH)

    print(f'Read ECG file. It has {len(ecg_raw)} values!')

    print('Detecting threshold')
    threshold = calculate_threshold(signal=ecg_raw)
    print(f'ECG maximum threshold is {threshold}')

    print('Detecting maximums')
    ecg_maximums = detect_maximums(signal=ecg_raw, threshold=threshold)

    print('Calculating times for each ECG signal entry')
    ecg_times = calculate_times(signal=ecg_raw, sample_rate=SAMPLE_RATE)

    print('Calculating RR intervals')
    ecg_rr = calculate_rr(maximums=ecg_maximums, times=ecg_times)
    if not ecg_rr:
        print('Something went wrong. Unable to extract RR intervals from ECG signal')
    else:
        print(f'Extracted {len(ecg_rr)} RR intervals from ECG raw signal')
