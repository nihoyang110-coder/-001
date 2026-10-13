// Grok Bot 模型路由（新粗野主义模板）。数字均在 事实对照.md 有卡片；改内容只改这里
window.CONTENT = {
  handle: '@你的账号',
  video: { lines: ['马斯克的AI', '要请对手', '来打工'], sub: 'Grok Bot 要调用 Claude', tag: '新闻拆解 · 以小见大' },
  cover: {
    tag: '新闻拆解 · 以小见大',
    lines: ['对手', '也是', '大客户'],
    big: '12.5',
    bigNote: '亿美元/月',
    sub: 'Anthropic 每月付 SpaceX 约 12.5 亿美元买算力；现在马斯克说 Grok Bot 要调用 Claude',
    src: '依据：马斯克 X 帖（10-07）· SpaceX 招股书报道 · 第三方价格表',
    icon: 'handshake',
    pills: [
      { label: 'SpaceX 收', value: '租金', icon: 'money_with_wings', color: 'b' },
      { label: 'Grok 要调用', value: '对手', icon: 'robot', color: 'y' }
    ]
  },
  facts: {
    tag: '先看事实', title: '发生了什么',
    rows: [
      { k: '谁说的', v: '马斯克 10 月 7 日在 X 发帖', hi: 'Grok Bot' },
      { k: '说了什么', v: '以后按任务挑选后端模型', hi: 'Claude/MJ/Suno' },
      { k: 'Grok Bot 是啥', v: '8 月上线的测试版智能体，每个 Bot 一台云电脑', hi: '多Bot协作' },
      { k: '还没有', v: '路由细节、官方文档、Anthropic 回应', hi: '都没公布' }
    ],
    src: '来源：马斯克 X 帖（经 The Next Web、Infobae 等引用）；xAI、Cursor 帮助页'
  },
  chart: {
    tag: '小切口', title: '同一件活交给 Claude', titleHi: '按牌价贵 2–3 倍', unit: '',
    groups: [
      { label: '输入', dine: 4, take: 2, gapLabel: '约贵', gapNum: '2倍' },
      { label: '输出', dine: 20, take: 6, gapLabel: '约贵', gapNum: '3.3倍' }
    ],
    legend: { dine: 'Claude Opus 5.5', take: 'Grok 4.7' },
    src: '单位：美元/每百万 token。来源：第三方价格汇总（10-11）；官方价与实际折扣可能不同'
  },
  gain: {
    tag: '谁得利', title: '对手之间', titleHi: '先是一笔大生意',
    stats: [
      { label: 'Anthropic 每月付 SpaceX', n: '12.5', unit: '亿美元（算力租金）' },
      { label: '约定期限到', n: '2029', unit: '年 5 月（可提前 90 天终止）' }
    ],
    points: ['SpaceX：把算力租给对手，月入约 12.5 亿美元', 'Anthropic：如果真被调用，多一个大客户', '用户：理论上每件事交给更合适的模型'],
    src: '来源：SpaceX 招股书相关报道；马斯克称是 180 天租约，与招股书说法不一'
  },
  loss: {
    tag: '代价', title: '还没说清的账',
    rows: [
      { who: '用户', icon: 'magnifying_glass_tilted_left', what: '这次答案是哪家模型给的、数据经过了谁，都还没公布' },
      { who: 'xAI', icon: 'receipt', what: '每把活转给 Claude，按牌价成本更高，谁来付没说' },
      { who: 'Suno', icon: 'warning', what: '没有公开 API，“调用 Suno”怎么接还没法验证' }
    ],
    kicker: '“平台替你挑模型”很诱人，但账单和数据去向都还是黑箱。',
    src: '来源：aiweekly、implicator；价格见上一页'
  },
  chain: {
    tag: '放大看', title: '从一帧截图到入口之争',
    steps: [
      { t: '一个Bot问另一个Bot', d: '博主截图里能看到的：多 Bot 互相转发' },
      { t: '平台替你挑模型', d: '马斯克：按任务选后端模型' },
      { t: '对手互为供应商', d: '算力从 SpaceX 买，模型可能找 Claude 用' },
      { t: '比拼“谁来派活”', d: '模型可互换后，分配任务的那一层更值钱', pred: true }
    ],
    compare: '对照：OpenAI 9-29 说要把 ChatGPT 做成 AI 应用商店，10-07 又让回答里直接生成小工具。路线不同，都想当“派活的那一层”。这是趋势判断，不是定论。',
    src: '来源：马斯克 X 帖；SpaceX 招股书报道；AFP；OpenAI 公告'
  },
  block: {
    tag: '卡在哪', title: '能不能落地，还不一定',
    hero: { label: 'Anthropic', big: '未表态', icon: 'balance_scale' },
    fillerIcon: 'hourglass_not_done',
    items: [
      { t: 'Anthropic 未表态', d: '条款限制用 Claude 做竞品；2025 年曾切断 xAI 权限' },
      { t: '细节没公布', d: '哪些任务走哪个模型、费用怎么算都没说' },
      { t: 'Suno 没公开 API', d: '这一项如何接入暂时无法验证' },
      { t: '还是测试版', d: 'Grok Bot 只开放给部分付费套餐' }
    ],
    src: '来源：The Rundown、VentureBeat、aiweekly；截至 10-13 未见 Anthropic 回应'
  },
  end: {
    tag: '以小见大',
    quote: ['模型越来越像', '水和电；', '更值钱的，可能是', '替你决定用哪家的人。'],
    highlightFrom: 2,
    watchTitle: '接下来盯这三件事',
    watch: [['近期', 'Anthropic 是否回应'], ['2027-01 前', '官方文档是否列出 Claude'], ['持续', 'Grok Bot 是否开放更多套餐']],
    src: '内容为个人观点，AI 辅助生成；涉及 Anthropic 部分仅依据公开报道。'
  }
};
