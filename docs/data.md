# Структура используемых данных

В лабораторных работах курса используются данные реального психофизиологического эксперимента, 
опубликованного в статье:

```
Behnke, M., Buchwald, M., Bykowski, A. et al. Psychophysiology of positive and negative 
emotions, dataset of 1157 cases and 8 biosignals. Sci Data 9, 10 (2022). 
https://doi.org/10.1038/s41597-021-01117-0
```

Полные данные этого исследования доступны по 
[ссылке](https://data.psychosensing.psnc.pl/popane/index.html)

В лабораторных работах курса используется только сигнал ЭКГ участников исследования за период 
фона (Baseline) и период решения задачи с эмоциональной окраской (Emotion). 

В процессе решения лабораторных работ проводится анализ вариабельности сердечного ритма с 
помощью индексов временной области для оценки функционального состояния человека.

```
participant_N_baseline_raw.txt  <-- input file, raw ECG signal, 
                                    baseline results (before experiment), 
                                    Nth participant
participant_N_emotion_raw.txt   <-- input file, raw ECG signal, 
                                    test results (after experiment), 
                                    Nth participant


participant_N_baseline_rr.txt   <-- Lab 1 output file, 
                                    extracted rr intervals from baseline signal, 
                                    Nth participant
participant_N_emotion_rr.txt    <-- Lab 1 output file, 
                                    extracted rr intervals from test signal, 
                                    Nth participant

participant_N_baseline_hrv.txt  <-- Lab 2 output file, 
                                    calculated HRV statistics for a baseline signal, 
                                    Nth participant
participant_N_emotion_hrv.txt   <-- Lab 2 output file, 
                                    calculated HRV statistics for a test signal, 
                                    Nth participant

wilcoxon_report.csv             <-- Lab 3 output file, 
                                    calculated Wilcoxon signed-rank test for each statistics
```
