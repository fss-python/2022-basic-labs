from pathlib import Path


def read_ecg_rr_file(file_path: Path):
    try:
        with open(file_path) as f:
            ecg_rr = f.readlines()
    except FileNotFoundError:
        print(f'This file "{file_path}" does not exist!')
    except Exception as e:
        print(f'This file "{file_path}" does not look like a file!')
        print(e)
        raise ValueError('Incorrect data file') from e

    # first line is meta-information (title - the name of the signal - "RR")
    # and not an RR item, therefore ignoring it
    only_number_lines = ecg_rr[1:]

    # creating intermediate variable for storing rr_signal
    rr_signal = []
    # each line is a number with a next line escape sequence
    for line in only_number_lines:
        # removing '\n' from line before casting to float
        numeric_value = float(line.strip())

        # adding element to a rr-signal
        rr_signal.append(numeric_value)
    return rr_signal


def is_input_correct (input: list):
    if type(input) != list or len(input) == 0:
        return False
    for i in input:
        if type(i) != float and type(i) != int or i<0:
            return False
    return True

def calculate_rrd(signal: list):
    rrd = []
    for i in range(len(signal) - 1):
        rrd_i = signal[i] - signal[i + 1]
        rrd.append(rrd_i)
    return rrd


# Lab 2 implementation goes below
def calculate_sdnn(signal: list):
    """Calculating SDNN for RR-intervals from the list"""
    if not is_input_correct (signal):
        return None
    mean_rr = sum(signal) / len(signal)
    sum_diff = 0
    for i in signal:
        rri_rrmean = (i - mean_rr) ** 2
        sum_diff += rri_rrmean
    return round((sum_diff / len(signal)) ** 0.5, 2)


def calculate_rmssd(signal: list):
    """Calculating RMSSD for RR-intervals from the list"""
    if not is_input_correct(signal):
        return None
    sum_of_brackets = 0
    rrd = calculate_rrd(signal)
    for i in rrd:
        brackets = i ** 2
        sum_of_brackets += brackets
    return round((sum_of_brackets / (len(signal) - 1)) ** 0.5, 2)


def calculate_sdsd(signal: list):
    """Calculating SDSD for RR-intervals from the list"""
    if not is_input_correct(signal):
        return None
    rrd = calculate_rrd(signal)
    mean_rrd = sum(rrd) / len(rrd)
    brackets_sum = 0
    for i in rrd:
        brackets_sum += (i - mean_rrd) ** 2
    return round((brackets_sum / (len(rrd) - 1)) ** 0.5, 2)


def calculate_nn_pnn(signal: list, threshold: int):
    """Calculating NN and pNN for RR-intervals from the list"""
    if not is_input_correct(signal):
        return None
    if type(threshold) != int:
        return None
    rrd_list = calculate_rrd(signal)
    result = []
    nn = []
    for i in rrd_list:
        if abs(i) <= threshold:
            nn.append(i)
    # result.append(len(nn))
    # result.append(round(len(nn)/len(rrd_list), 2))
    return len(nn), round(len(nn) / len(rrd_list), 2)


def save_hrv_in_file(hrv_characteristics: dict, path: str):
    """Calculating HRV time-scale metrics for RR-intervals from the list"""
    if type(hrv_characteristics) != dict:
        return -1
    if type(path) != str:
        return -1
    with open(path, 'w') as f:
        for index, key in enumerate(hrv_characteristics):
            value = hrv_characteristics.get(key)
            if index < len(hrv_characteristics) - 1:
                f.write(f'{key}\t{value}\n')
            else:
                f.write(f'{key}\t{value}')


# Lab 2 demonstration goes below
if __name__ == '__main__':
    DATA_PATH = Path(__file__).parent / 'data' / 'participant_28_baseline_rr.txt'

    print(f'Opening {DATA_PATH} with RR signal')

    ecg_rr = read_ecg_rr_file(DATA_PATH)

    print(f'Read RR file. It has {len(ecg_rr)} values!')

    print('Calculating SDNN')
    SDNN = calculate_sdnn(signal=ecg_rr)
    print(f'SDNN is {round(SDNN, 2)}')

    print('Calculating RMSSD')
    RMSSD = calculate_rmssd(signal=ecg_rr)
    print(f'RMSSD is {round(RMSSD, 2)}')

    print('Calculating SDSD')
    SDSD = calculate_sdsd(signal=ecg_rr)
    print(f'SDSD is {round(SDSD, 2)}')

    print('Calculating NN and pNN for 50 and 20')
    nn_50, pnn_50 = calculate_nn_pnn(signal=ecg_rr, threshold=50)
    nn_20, pnn_20 = calculate_nn_pnn(signal=ecg_rr, threshold=20)

    print(f'NN_50 is {nn_50}')
    print(f'pNN_50 is {round(pnn_50, 2)}')
    print(f'NN_20 is {nn_20}')
    print(f'pNN_20 is {round(pnn_20, 2)}')

    hrv_characteristics = {
        'SDNN': SDNN,
        'RMSSD': RMSSD,
        'SDSD': SDSD,
        'NN50': nn_50,
        'pNN50': pnn_50,
        'NN20': nn_20,
        'pNN20': pnn_20
    }
    save_hrv_in_file(hrv_characteristics, './data/participant_28_baseline_hrv.txt')
