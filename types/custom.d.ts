declare global {}
type DeepPartial<T> = Partial<{ [P in keyof T]: DeepPartial<T[P]> }>
type AnyObj = { [key: string]: string }
