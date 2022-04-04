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

def calculate_sdnn(signal: list):
    """Calculating SDNN for RR-intervals from the list"""
    pass


def calculate_rmssd(signal: list):
    """Calculating RMSSD for RR-intervals from the list"""
    pass


def calculate_sdsd(signal: list):
    """Calculating SDSD for RR-intervals from the list"""
    pass


def calculate_nn_pnn(signal: list, threshold: int):
    """Calculating NN and pNN for RR-intervals from the list"""
    pass


def save_hrv_in_file(hrv_characteristics: dict, path: str):
    """Calculating HRV time-scale metrics for RR-intervals from the list"""
    pass



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
        'RMSSD': RMSSD,
        'SDSD': SDSD,
        'NN50': nn_50,
        'pNN50': pnn_50,
        'NN20': nn_20,
        'pNN20': pnn_20
    }
    save_hrv_in_file(hrv_characteristics, './data/participant_28_baseline_hrv.txt')
