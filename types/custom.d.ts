import { ChartOptions, SeriesDataItemTypeMap, SeriesOptions, SeriesOptionsMap, TimeScaleOptions, PriceScaleOptions } from 'lightweight-charts'
import { MessageApiInjection, LoadingBarApiInjection } from 'naive-ui'
declare global {
  interface Window {
    $message: MessageApiInjection
    $loading: LoadingBarApiInjection
  }
  type DeepPartial<T> = Partial<{ [P in keyof T]: DeepPartial<T[P]> }>

  namespace ChartOption {
    type Base = DeepPartial<ChartOptions>
    type Data = SeriesDataItemTypeMap[keyof SeriesDataItemTypeMap][]
    type Marker = SeriesMarker<Time>
    type Series = DeepPartial<SeriesOptions<SeriesOptionsMap[keyof SeriesOptionsMap]>>
    type TimeScale = DeepPartial<TimeScaleOptions>
    type PriceScale = DeepPartial<PriceScaleOptions>
  }

  type AnyObj = { [key: string]: string }
}
