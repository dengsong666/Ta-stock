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
            '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M9 4a1 1 0 0 0-2 0v2.5a.5.5 0 0 1-.5.5H4a1 1 0 0 0 0 2h2.5A2.5 2.5 0 0 0 9 6.5V4Zm0 16a1 1 0 1 1-2 0v-2.5a.5.5 0 0 0-.5-.5H4a1 1 0 1 1 0-2h2.5A2.5 2.5 0 0 1 9 17.5V20Zm7-17a1 1 0 0 0-1 1v2.5A2.5 2.5 0 0 0 17.5 9H20a1 1 0 1 0 0-2h-2.5a.5.5 0 0 1-.5-.5V4a1 1 0 0 0-1-1Zm-1 17a1 1 0 1 0 2 0v-2.5a.5.5 0 0 1 .5-.5H20a1 1 0 1 0 0-2h-2.5a2.5 2.5 0 0 0-2.5 2.5V20Z"/></svg>',
          filter:
            '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 36 36"><path fill="currentColor" d="M33 4H3a1 1 0 0 0-1 1v1.67a1.79 1.79 0 0 0 .53 1.27L14 19.58v10.2l2 .76V19a1 1 0 0 0-.29-.71L4 6.59V6h28v.61L20.33 18.29A1 1 0 0 0 20 19v13.21l2 .79V19.5L33.47 8A1.81 1.81 0 0 0 34 6.7V5a1 1 0 0 0-1-1Z" class="clr-i-outline clr-i-outline-path-1"/><path fill="none" d="M0 0h36v36H0z"/></svg>',
          stock:
            '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 512 512"><path fill="#DCE2E2" d="M478.685 36H32a4.5 4.5 0 0 0 0 9h107v101H32a4.5 4.5 0 0 0 0 9h107v102H32a4.5 4.5 0 0 0 0 9h107v101H32a4.5 4.5 0 0 0 0 9h107v110.685a4.5 4.5 0 0 0 9 0V376h103v110.685a4.5 4.5 0 0 0 9 0V376h103v110.685a4.5 4.5 0 0 0 9 0V376h102v110.685a4.5 4.5 0 0 0 9 0V40c0-2.485-1.83-4-4.315-4zM363 146H260V45h103v101zm9-101h102v101H372V45zm-9 110v102H260V155h103zm9 0h102v102H372V155zM148 45h103v101H148V45zm0 110h103v102H148V155zm0 212V266h103v101H148zm112 0V266h103v101H260zm112 0V266h102v101H372z"/><path fill="#FF473E" d="M279.047 441.203a12.002 12.002 0 0 1-10.679-6.524L166.973 237.004L49.25 379.458c-4.222 5.108-11.786 5.828-16.894 1.605c-5.109-4.222-5.828-11.785-1.606-16.895l129.332-156.501a12 12 0 0 1 19.927 2.167l99.766 194.497L468.347 84.379c3.365-5.708 10.721-7.611 16.431-4.245c5.71 3.365 7.61 10.721 4.245 16.431L289.384 435.296a12 12 0 0 1-10.337 5.907z"/><path fill="#B9C5C6" d="M478.685 489.418H32a7 7 0 0 1-7-7V40a7 7 0 1 1 14 0v435.418h439.685a7 7 0 1 1 0 14z"/></svg>',
          select:
            '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path fill="currentColor" d="M18.438 20.938H5.563a2.5 2.5 0 0 1-2.5-2.5V5.564a2.5 2.5 0 0 1 2.5-2.5h12.875a2.5 2.5 0 0 1 2.5 2.5v12.874a2.5 2.5 0 0 1-2.5 2.5ZM5.563 4.064a1.5 1.5 0 0 0-1.5 1.5v12.874a1.5 1.5 0 0 0 1.5 1.5h12.875a1.5 1.5 0 0 0 1.5-1.5V5.564a1.5 1.5 0 0 0-1.5-1.5Z"/><path fill="currentColor" d="M15 12.5h-2.5V15a.5.5 0 0 1-1 0v-2.5H9a.5.5 0 0 1 0-1h2.5V9a.5.5 0 0 1 1 0v2.5H15a.5.5 0 0 1 0 1Z"/></svg>',
          selected:
            '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"><path d="M20.496 5.627A2.25 2.25 0 0 1 22 7.75v10A4.25 4.25 0 0 1 17.75 22h-10a2.25 2.25 0 0 1-2.123-1.504l2.097.004H17.75a2.75 2.75 0 0 0 2.75-2.75v-10l-.004-.051V5.627zM17.246 2a2.25 2.25 0 0 1 2.25 2.25v12.997a2.25 2.25 0 0 1-2.25 2.25H4.25A2.25 2.25 0 0 1 2 17.247V4.25A2.25 2.25 0 0 1 4.25 2h12.997zm0 1.5H4.25a.75.75 0 0 0-.75.75v12.997c0 .414.336.75.75.75h12.997a.75.75 0 0 0 .75-.75V4.25a.75.75 0 0 0-.75-.75zm-7.665 7.858L13.47 7.47a.75.75 0 0 1 1.133.976l-.073.084l-4.5 4.5a.75.75 0 0 1-1.056.004L8.9 12.95l-1.5-2a.75.75 0 0 1 1.127-.984l.073.084l.981 1.308L13.47 7.47L9.58 11.358z" fill="currentColor" fill-rule="nonzero"/></svg>'
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
    ['elp', { 'white-space': 'nowrap', overflow: 'hidden', 'text-overflow': 'ellipsis' }],
    [/^pointer-(\w+)$/, ([, w]) => ({ 'pointer-events': w })],
    [/^wh-(\d+)(\w+|%)$/, ([, d, w]) => ({ width: `${d + w}`, height: `${d + w}` })],
    [/^bd-(\d+)-(#\w+)$/, ([, d, w]) => ({ border: `${d}px solid ${w}` })],
    [/^grid-(\d)-(\d)-(\d+)$/, ([, d1, d2, d3]) => ({ display: 'grid', 'grid-template-rows': `repeat(${d1}, 1fr)`, 'grid-template-columns': `repeat(${d2}, 1fr)`, gap: `${d3}px` })]
  ]
})
