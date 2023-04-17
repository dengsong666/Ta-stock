import { SeriesMarker, Time } from 'lightweight-charts'

export const test_data = [
  {
    time: '2023-03-20',
    open: 3966.7,
    high: 4081.23,
    low: 3917.4,
    close: 4029.38
  },
  {
    time: '2023-03-21',
    open: 4026.16,
    high: 4061.19,
    low: 3980.06,
    close: 4054.54
  },
  {
    time: '2023-03-22',
    open: 4080.68,
    high: 4112.23,
    low: 4023.26,
    close: 4045.01
  },
  {
    time: '2023-03-23',
    open: 4027.6,
    high: 4049.8,
    low: 4002.56,
    close: 4017.81
  },
  {
    time: '2023-03-24',
    open: 4016.25,
    high: 4084.94,
    low: 3969.01,
    close: 4049.63
  },
  {
    time: '2023-03-27',
    open: 4039.22,
    high: 4136.3,
    low: 4019.41,
    close: 4118.62
  },
  {
    time: '2023-03-28',
    open: 4112.76,
    high: 4131.17,
    low: 4060.36,
    close: 4065.79
  },
  {
    time: '2023-03-29',
    open: 4084.61,
    high: 4125.46,
    low: 4048.8,
    close: 4072.96
  },
  {
    time: '2023-03-30',
    open: 4067.63,
    high: 4128.99,
    low: 4035.5,
    close: 4128.99
  },
  {
    time: '2023-03-31',
    open: 4135.87,
    high: 4191.36,
    low: 4117.71,
    close: 4127.28
  },
  {
    time: '2023-04-03',
    open: 4126.63,
    high: 4206.18,
    low: 4109.6,
    close: 4170.7
  },
  {
    time: '2023-04-04',
    open: 4168.76,
    high: 4168.76,
    low: 4036.56,
    close: 4077.72
  },
  {
    time: '2023-04-06',
    open: 4069.47,
    high: 4113.12,
    low: 4040.87,
    close: 4103.73
  },
  {
    time: '2023-04-07',
    open: 4100.4,
    high: 4136.61,
    low: 4082.24,
    close: 4085.92
  },
  {
    time: '2023-04-10',
    open: 4111.47,
    high: 4152.45,
    low: 4080.65,
    close: 4150.89
  },
  {
    time: '2023-04-11',
    open: 4149.95,
    high: 4166.89,
    low: 4107.48,
    close: 4137.16
  },
  {
    time: '2023-04-12',
    open: 4124.71,
    high: 4142.41,
    low: 4045.82,
    close: 4055.26
  },
  {
    time: '2023-04-13',
    open: 4068.34,
    high: 4095.45,
    low: 4028.15,
    close: 4030.66
  },
  {
    time: '2023-04-14',
    open: 4009.03,
    high: 4075.2,
    low: 3989.45,
    close: 4052.58
  }
]
export const test_markers: SeriesMarker<Time>[] = [{ time: '2023-04-02', position: 'belowBar', color: '#2196F3', shape: 'arrowUp', text: 'Buy @ ' }]
