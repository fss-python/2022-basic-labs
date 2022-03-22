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
    if type(signal) != list:
        return None
    if len(signal) == 0:
        return None
    for element in signal:
        if type(element) != float:
            return None
    return max(signal) * 0.8

def detect_maximums(signal: list, threshold: float):
    """Labeling RR peaks"""
    final_list = []
    if len(signal) == 0:
        return None
    for index, item in enumerate(signal, start = 0):
        if 0 < index < (len(signal) - 1):
            if type(item) is not str and item >= threshold and signal[index-1] < item and signal[index+1] < item:
                final_list.append(1)
            else:
                final_list.append(0)
        else:
            final_list.append(0)
    '''print (final_list)'''
    return final_list


def calculate_times(signal: list, sample_rate: int):
    final_list = []
    if signal is None:
        return None
    if len(signal) == 0:
        return None
    time_mc = 0
    time_counter = 1000 / sample_rate
    for index, item in enumerate(signal, start=0):
        final_list.append(time_mc)
        time_mc += time_counter
    return final_list

    """Calculating timestamp for each item in ECG"""



def calculate_rr(maximums: list, times: list):
    if maximums is None:
        return []
    if len(maximums) == 0:
        return []

    if times is None:
        return []
    if len(times) == 0:
        return []

    final_list = []
    index_max_prev = -1
    for index_max, item_max in enumerate(maximums, start=0):
        if item_max == 1:
            if index_max_prev != -1:
                time_temp = times[index_max] - times[index_max_prev]
                if time_temp > 400:
                    final_list.append(time_temp)
            index_max_prev = index_max
    '''print(final_list)'''
    return final_list



    """Extract RR intervals"""
    '''pass'''


# Lab 1 demonstration goes below
if __name__ == '__main__':
    print('hello, Kate')
    # signal = ['str', 1.0, 3.0, 'trh']
    # print(calculate_threshold(signal))

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
