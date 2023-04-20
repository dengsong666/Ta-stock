import { defineConfig, presetAttributify, presetIcons, presetUno, presetMini } from 'unocss'

export default defineConfig({
  presets: [
    presetUno(),
    presetAttributify(),
    presetMini(),
    presetIcons({
      extraProperties: {
        display: 'inline-block',
        'vertical-align': 'middle',
        width: '24px',
        height: '24px'
      },
      collections: {
        my: {
          'full-screen':
            '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M5 6a1 1 0 0 1 1-1h2a1 1 0 0 0 0-2H6a3 3 0 0 0-3 3v2a1 1 0 0 0 2 0V6Zm0 12a1 1 0 0 0 1 1h2a1 1 0 1 1 0 2H6a3 3 0 0 1-3-3v-2a1 1 0 1 1 2 0v2ZM18 5a1 1 0 0 1 1 1v2a1 1 0 1 0 2 0V6a3 3 0 0 0-3-3h-2a1 1 0 1 0 0 2h2Zm1 13a1 1 0 0 1-1 1h-2a1 1 0 1 0 0 2h2a3 3 0 0 0 3-3v-2a1 1 0 1 0-2 0v2Z"/></svg>',
          'full-screen-exit':
            '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M9 4a1 1 0 0 0-2 0v2.5a.5.5 0 0 1-.5.5H4a1 1 0 0 0 0 2h2.5A2.5 2.5 0 0 0 9 6.5V4Zm0 16a1 1 0 1 1-2 0v-2.5a.5.5 0 0 0-.5-.5H4a1 1 0 1 1 0-2h2.5A2.5 2.5 0 0 1 9 17.5V20Zm7-17a1 1 0 0 0-1 1v2.5A2.5 2.5 0 0 0 17.5 9H20a1 1 0 1 0 0-2h-2.5a.5.5 0 0 1-.5-.5V4a1 1 0 0 0-1-1Zm-1 17a1 1 0 1 0 2 0v-2.5a.5.5 0 0 1 .5-.5H20a1 1 0 1 0 0-2h-2.5a2.5 2.5 0 0 0-2.5 2.5V20Z"/></svg>'
        }
        // antd: () => import("@iconify-json/ant-design/icons.json").then((i) => i.default),
      },
      customizations: {
        transform(svg) {
          return svg.replace(/#ffffff/, 'currentColor')
        }
      }
    })
  ],
  safelist: ['setting', 'dashboard', 'notification', 'menu', 'apartment', 'key', 'usergroup-add', 'user', 'info-circle', 'like'].map((icon) => `i-ant-design-${icon}-outlined`),
  theme: {
    colors: {
      default: '#4700FF',
      success: '#67C23A',
      warning: '#E6A23C',
      danger: '#F56C6C',
      info: '#909399'
    }
  },
  shortcuts: [
    ['flex-row', 'flex flex-row'],
    ['flex-col', 'flex flex-col'],
    ['flex-center', 'flex justify-center items-center'],
    ['e-auto', 'pointer-events-auto'],
    ['operate', 'm8px c-default cursor-pointer'],
    ['add-btn', 'flex-center bg-#363b64 p8px rd-10px ml-auto']
  ],
  rules: [
    ['absolute-center', { position: 'absolute', left: '50%', top: '50%', transform: 'translate(-50%,-50%)' }],
    ['nowrap', { 'white-space': 'nowrap' }],
    ['pointer-events', { 'white-space': 'nowrap' }],
    [/^pointer-(\w+)$/, ([, w]) => ({ 'pointer-events': w })],
    [/^wh-(\d+)(\w+|%)$/, ([, d, w]) => ({ width: `${d + w}`, height: `${d + w}` })],
    [/^bd-(\d+)-(#\w+)$/, ([, d, w]) => ({ border: `${d}px solid ${w}` })],
    [/^grid-(\d)-(\d)-(\d+)$/, ([, d1, d2, d3]) => ({ display: 'grid', 'grid-template-rows': `repeat(${d1}, 1fr)`, 'grid-template-columns': `repeat(${d2}, 1fr)`, gap: `${d3}px` })]
  ]
})
