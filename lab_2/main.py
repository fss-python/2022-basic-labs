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


# Lab 2 implementation goes below

def is_input_correct(signal):
    if type(signal) != list or len(signal) == 0:
        return False
    for s in signal:
        if type(s) != float and type(s) != int:
            return False
        if s <= 0:
            return False
    return True


def calculate_rrd(signal):
    if not is_input_correct(signal):
        return None
    rrd_list = []
    for i in range(len(signal) - 1):
        rrd_list.append(signal[i] - signal[i + 1])
    return rrd_list


def calculate_sdnn(signal: list):
    """Calculating SDNN for RR-intervals from the list"""
    if not is_input_correct(signal):
        return None
    rr_mean = sum(signal) / len(signal)
    sum_f = 0
    for rr in signal:
        sum_f += (rr - rr_mean) ** 2
    return round((sum_f / len(signal)) ** 0.5, 2)


def calculate_rmssd(signal: list):
    """Calculating RMSSD for RR-intervals from the list"""
    if not is_input_correct(signal):
        return None
    rrd_sq_sum = 0
    for i in range(len(signal) - 1):
        rrd_sq_sum += (signal[i] - signal[i + 1]) ** 2
    return round((rrd_sq_sum / (len(signal) - 1)) ** 0.5, 2)


def calculate_sdsd(signal: list):
    """Calculating SDSD for RR-intervals from the list"""
    if not is_input_correct(signal):
        return None
    rrd_list = calculate_rrd(signal)
    rrd_mean = sum(rrd_list) / len(rrd_list)
    sq_sum = 0
    for rrd_item in rrd_list:
        sq_sum += (rrd_item - rrd_mean) ** 2
    return round((sq_sum / (len(rrd_list) - 1)) ** 0.5, 2)


def calculate_nn_pnn(signal: list, threshold: int):
    """Calculating NN and pNN for RR-intervals from the list"""
    if not is_input_correct(signal):
        return None
    if type(threshold) != float and type(threshold) != int:
        return None
    rrd_list = calculate_rrd(signal)
    nn = 0
    for rrd_item in rrd_list:
        if abs(rrd_item) <= threshold:
            nn += 1
    pnn = nn / len(rrd_list)
    return [nn, round(pnn, 2)]


def save_hrv_in_file(hrv_characteristics: dict, path: str):
    """Calculating HRV time-scale metrics for RR-intervals from the list"""
    if type(hrv_characteristics) != dict or type(path) != str:
        return -1
    with open(path, 'w') as file:
        for index, key in enumerate(hrv_characteristics):
            value = hrv_characteristics.get(key)
            if index < len(hrv_characteristics):
                file.write(f'{key}\t{value}\n')
            else:
                file.write(f'{key}\t{value}')


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
