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
    for s in signal:
        if type(s) != float:
            return None
    thrh = max(signal) * 0.8
    return (thrh)
    #pass


def detect_maximums(signal: list, threshold: float):
    """Labeling RR peaks"""
    if type(signal) != list or type(threshold) != float:
        return None
    for s in signal:
        if type(s) != float:
            return None
    mxms = [0]
    i = 1
    for s in signal[1:-1]:
        if signal[i] >= threshold and signal[i - 1] < signal[i] and signal[i + 1] < signal[i]:
            mxms.append(1)
            i+=1
        else:
            mxms.append(0)
            i+=1
    mxms.append(0)
    return mxms
    #pass


def calculate_times(signal: list, sample_rate: int):
    """Calculating timestamp for each item in ECG"""
    if type(signal) != list or type(sample_rate) != int:
        return None
    for s in signal:
        if type(s) != float:
            return None
    tms = []
    i = 1000 / sample_rate
    ms = 0.0
    for s in range(len(signal)):
        tms.append(ms)
        ms += i
    return tms
    #pass


def calculate_rr(maximums: list, times: list):
    """Extract RR intervals"""
    if type(maximums) != list or type(times) != list:
        return None
    for m in maximums:
        if type(m) != int:
            return None
    if len(maximums) == 0:
        return None
    for t in times:
        if type(t) != float:
            return None
    ms_list = []
    for i in range(len(maximums)):
        if maximums[i] == 1:
            ms_list.append(times[i])

    prev = ms_list[0]
    rr = [0, ]
    for j in ms_list[1:]:
        rr.append(j - prev)
        prev = j
    #print(rr)
    rr_clean = []
    for r in rr:
        if r > 400:
            rr_clean.append(r)
    #print(rr_clean)
    return rr_clean
    #pass

'''
if type(maximums) != list or type(times) != list:
    return None
i = maximums.index(1)
rr_list = []
for m in maximums[i:]:
    if type(m) != bool:
        return None
    if m == 1:
        rr = times[maximums.index(1, i + 1)] - times[i]
        print(rr)
        rr_list.append(rr)
        i += 1
    else:
        i += 1

return rr_list
'''


# Lab 1 demonstration goes below
if __name__ == '__main__':

    SAMPLE_RATE = 1000
    DATA_PATH = Path(__file__).parent / 'data' / 'participant_28_baseline_raw.txt'

    print(f'Opening {DATA_PATH} with ECG signal')

    ecg_raw = read_ecg_raw_file(DATA_PATH)

    print(f'Read ECG file. It has {len(ecg_raw)} values!')
    #signal=[1.3,5.7,6.7,4.7]
    print('Detecting threshold')
    threshold = calculate_threshold(signal=ecg_raw)
    print(f'ECG maximum threshold is {threshold}')


    print('Detecting maximums')
    ecg_maximums = detect_maximums(signal=ecg_raw, threshold=threshold)

    #print(ecg_maximums)
    #print(ecg_maximums.count(1))
    #print(len(ecg_raw))
    #print(len(ecg_maximums))
    #SAMPLE_RATE = 1500

    print('Calculating times for each ECG signal entry')
    ecg_times = calculate_times(signal=ecg_raw, sample_rate=SAMPLE_RATE)

    #print(ecg_times)
    #print(ecg_times[0:10],ecg_times[-10:-1])
    #print(len(ecg_times))

    print('Calculating RR intervals')
    ecg_rr = calculate_rr(maximums=ecg_maximums, times=ecg_times)

    #print(ecg_rr)
    #print(type(ecg_rr))

    if not ecg_rr:
        print('Something went wrong. Unable to extract RR intervals from ECG signal')
    else:
        print(f'Extracted {len(ecg_rr)} RR intervals from ECG raw signal')
