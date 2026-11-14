# 产品知识手册：专业定义、作用、依赖、实操与证据

> 2026-11-14 V3 / INDEXED / NOT_RUN。**知识覆盖≠本人成绩；requires 是概念依赖，不是学习日历。** 按需要从任一节点开始，回溯不会的前置。机器唯一索引为 [知识卡](knowledge-catalog.json)。

入门建议：[产品经理专业术语×大白话](product-manager-primer.md) → [流程关系图](product-lifecycle-mermaid.md) → [按需路由](../learning/demand-router.md)。来源可继续查看 [上游资料映射](../../resources/upstream-pm-knowledge-index.md)，**私仓链接需要授权**。

## 产品发现/策略（23 个知识点）

| 节点 | 内容 | 在产品中解决什么 | 逻辑关联/前置 | 官方/原作者资料 | 动手任务 | 留下什么证据 |
|---|---|---|---|---|---|---|
| `PM01` | 角色分工与生命周期 | 识别问题-决策-交付-复盘的责任 | 无 | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S02](https://www.atlassian.com/agile/product-management/requirements) | 画出 PM/PE/设计/研发/销售的责任图并指出灰区 | 一份冲突决策表和验收责任人 |
| `PM02` | 问题定义与 JTBD | 把功能需求翻译成用户待完成任务 | `PM01` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S04](https://pair.withgoogle.com/guidebook-v2/) | 从三条功能请求提炼任务/触发场景/成功行为 | 包含不做条件和失败反例的问题卡 |
| `PM03` | 访谈与行为证据 | 获得可以推翻假设的真实/合成事实 | `PM02` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S04](https://pair.withgoogle.com/guidebook-v2/) | 写非诱导访谈脚本并对照行为/陈述 | 事实/推断/假设台账及证据等级 |
| `PM04` | 竞品与替代方案 | 人工/旧系统/不用 AI 都是竞争 | `PM02` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 比较人工、规则、搜索、AI 并列反证 | 替代方案矩阵与停止门槛 |
| `PM05` | 价值主张与市场细分 | 确认谁痛、频率、可触达性及买方 | `PM03`、`PM04` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 区分用户/买方/采购责任，分场景估算触达 | 一张证据标注的细分/价值卡 |
| `PM06` | 优先级与路线图 | 确定先解决哪个风险而非堆功能 | `PM04`、`PM05` | [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 以 RICE 与明确约束各排一次同一需求，说明差异 | Now/Next/Later 决策与资源 Stop Rule |
| `PM07` | PRD/用户故事/验收 | 把模糊目标变可测试行为 | `PM02` | [S02](https://www.atlassian.com/agile/product-management/requirements) | 完成一页 PRD + Given/When/Then 正负场景 | 可供他人不猜测地写测试的需求文档 |
| `PM08` | 信息架构/原型/UI 状态 | 从任务流设计空态/失败/等待/恢复 | `PM07` | [S04](https://pair.withgoogle.com/guidebook-v2/) / [S09](https://www.w3.org/WAI/WCAG22/quickref/) | 做两版低保真任务流和错误态原型 | 用户可观察任务结果与无障碍检查表 |
| `PM09` | AI 信任与可控 UX | 解释来源、错误、能力边界与人工控制 | `PM08`、`AI01` | [S04](https://pair.withgoogle.com/guidebook-v2/) / [S22](https://pair.withgoogle.com/guidebook-v2/chapters) | 设计引用/拒答/反馈/人工接管的三条流程 | 失败提示及真实/合成可用性测试记录 |
| `PM10` | 交付协作/范围与变更 | 定义变更责任、发布门禁与冲突处理 | `PM07` | [S02](https://www.atlassian.com/agile/product-management/requirements) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 模拟需求变更影响排期、权限、成本并作 ADR | 变更前后 UAT 与审批记录 |
| `PM11` | 客户成功/支持运营 | 将故障/投诉转成可重现事实与服务闭环 | `PM09`、`OPS02` | [S04](https://pair.withgoogle.com/guidebook-v2/) / [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 构建合成支持工单分级/升级/闭环规则 | 优先级、响应预案、重复故障分析 |
| `PM12` | 产品策略与 Portfolio 决策 | 判断多个产品/渠道哪个该停 | `PM06`、`BIZ01` | [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) / [S01](https://www.atlassian.com/agile/product-management/discovery) | 三候选预算减半时选唯一试验并解释淘汰项 | 资源配置和机会成本记录 |
| `PM13` | 机会解决方案树 OST | Opportunity Solution Tree 用可衡量成果 Outcome 组织用户机会、候选方案和待验证假设之间的因果关系。 | `PM02`、`PM03`、`PM06` | [S27](https://www.producttalk.org/glossary-discovery-product-discovery/) / [S28](https://www.producttalk.org/getting-started-with-discovery/) / [S37](https://www.atlassian.com/agile/product-management/discovery) | 画一棵 1 结果→3 机会→各2方案→关键假设的树，并提出反证 | 可追溯 Outcome/Opportunity/Solution/Assumption，三种不是同一层 |
| `PM14` | 研究方法选型与三角验证 | 按探索/评估目标，组合定性行为研究、可用性研究和定量实验，并识别抽样与观察偏差。 | `PM03` | [S29](https://www.nngroup.com/articles/which-ux-research-methods/) / [S38](https://www.nngroup.com/articles/ux-research-cheat-sheet/) | 同一合成现象提出访谈、观察、日志分析各能/不能回答的问题 | 方法决策表、证据缺口和至少一项相反解释 |
| `PM15` | OKR/Outcome/北极星对齐 | OKR 将目标与关键结果建立可观察的对齐关系；北极星表达长期核心用户价值，关键结果不应等同任务清单。 | `PM06`、`DATA01` | [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 把十条功能需求转换成目标、结果与可证伪指标 | 结果指标、领先输入和守门指标齐全，不以工作量充成果 |
| `PM16` | Stakeholder 利益相关者与决策权 | Stakeholder 管理识别使用者、买方、技术、设计、法务、运营、审批者的目标与决策权，建立可沟通的责任分工。 | `PM07` | [S32](https://scrumguides.org/scrum-guide.html?lang=en) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 绘制 6 角色影响-兴趣矩阵与可升级的责任表 | 决策/执行/咨询/知会与冲突升级说明 |
| `PM17` | 产品交付与项目控制 | 产品交付管理通过范围、依赖、风险、验收、沟通和发布计划将持续发现转为可靠增量。 | `PM10` | [S32](https://scrumguides.org/scrum-guide.html?lang=en) / [S33](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) / [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) | 为模拟 2 周 Release 列 WBS/依赖/风险、UAT 与风险预警 | 明确范围、风险责任、变更处理和实际复盘 |
| `PM18` | Product Operating Model / 产品组织运作 | 产品运营模式规定产品目标、团队授权、决策权、发现-交付流程与反馈治理的协作系统。 | `PM16`、`PM06` | [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 绘制产品三人组或单人多角色职责、决策与审查节奏 | 发现与交付双向信息流和决策责任表 |
| `PM19` | 市场定位和竞争差异化 | 定位通过目标细分、竞争参照和价值差异解释为何特定用户应选择此产品。 | `PM05`、`PM04` | [S31](https://www.strategyzer.com/library/the-value-proposition-canvas) / [S25](https://www.svpg.com/product-management-an-introduction/) | 选择 2 类买方，做替代方案/差异对比与反证 | 一句可验证定位 + 数据/访问证据分层 |
| `PM20` | 用户旅程/服务蓝图 | Customer Journey Map 描述跨触点用户体验，Service Blueprint 同时揭示前台和后台流程/交接。 | `PM08`、`PM03` | [S29](https://www.nngroup.com/articles/which-ux-research-methods/) / [S40](https://pair.withgoogle.com/guidebook-v2/chapters) | 绘制前台动作、后台 API/人员、跨触点失败与恢复 | 服务蓝图、可观察触点和错误恢复用例 |
| `PM21` | 平台型产品/API 产品思维 | 平台产品把内部能力以 API/组件/权限及 SLA 形式交给其他团队或第三方消费，需同时关注开发者体验和兼容成本。 | `ENG03`、`PM07` | [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 写 API 消费者故事、版本契约、配额、失败响应与支持范围 | 兼容变更、租户隔离与文档演练 |
| `PM22` | Pre-mortem 预演失败和产品风险矩阵 | Premortem 在投入前假设项目已失败，逆向列举原因、概率/影响、应对、可检测信号和责任。 | `PM06`、`PM07` | [S25](https://www.svpg.com/product-management-an-introduction/) / [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) | 模拟产品上线失败，列 8 个失败假设并按四大风险分类 | 风险登记、观测信号、Stop/降级门槛 |
| `PM23` | 产品生命周期/停用与迁移 | Product Lifecycle Management 关注验证、增长、成熟、衰退或停用阶段的产品投资、用户迁移与支持义务。 | `PM12`、`PM11` | [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) / [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) | 制定产品停用公告、数据导出/删除、用户迁移、合同边界 | 停用清单与用户影响/回滚方案 |

## AI 技术与产品取舍（14 个知识点）

| 节点 | 内容 | 在产品中解决什么 | 逻辑关联/前置 | 官方/原作者资料 | 动手任务 | 留下什么证据 |
|---|---|---|---|---|---|---|
| `AI01` | LLM 基础与上下文/Token | 理解生成不确定性、输入预算和限制 | `PM02` | [S19](https://developers.google.com/machine-learning/crash-course) / [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | 同题短/长上下文比较结构化输出与 Token/成本 | 输入-输出-成本与失败报告 |
| `AI02` | Prompt/结构化输出 | 实现可校验输出而非靠自然语言猜测 | `AI01` | [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) / [S19](https://developers.google.com/machine-learning/crash-course) | 为合成分类任务比较规则/Prompt + JSON schema 校验 | 字段校验通过率和坏例日志 |
| `AI03` | Embedding/检索与 RAG | 区分索引、召回、排序、生成和证据 | `AI01`、`ENG04` | [S19](https://developers.google.com/machine-learning/crash-course) / [S17](https://docs.langchain.com/oss/python/learn) | 在公开小语料比较 BM25/向量/混检并分层评测 | 检索金标、引用支持、拒答与版本失败 |
| `AI04` | RAG 数据治理/文档生命周期 | 处理来源许可、权限、更新、删除与版本 | `AI03`、`ENG06` | [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S17](https://docs.langchain.com/oss/python/learn) | 模拟文档撤销权限、版本更新、删除后不可检索 | 越权/旧版/删除负例 |
| `AI05` | 工具调用/Workflow/单 Agent | 知道什么时候让模型决策、什么时候固定流程 | `AI02`、`ENG03` | [S06](https://www.anthropic.com/engineering/building-effective-agents) / [S17](https://docs.langchain.com/oss/python/learn) | Mock 工单比较规则链与工具 Agent 的正确率/成本 | 审批前无写入、超时与错误恢复 |
| `AI06` | MCP/工具权限与副作用 | 工具连接不代表可以越权执行 | `AI05`、`ENG06` | [S18](https://blog.modelcontextprotocol.io/posts/2026-07-28/) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 在隔离工具沙箱检查 schema、租户权限、审批、审计 | 未授权拒绝、无副作用、版本兼容性记录 |
| `AI07` | Context Engineering/Memory | 在正确时机给模型正确的上下文与工具 | `AI01`、`AI05` | [S17](https://docs.langchain.com/oss/python/learn) / [S06](https://www.anthropic.com/engineering/building-effective-agents) | 对比上下文裁剪、版本过滤、checkpoint 恢复 | 同测试集效果/Token/恢复负例 |
| `AI08` | Harness/Agent 执行治理 | 任务边界、预算、重试、停止、人工介入与恢复 | `AI05`、`AI07`、`OPS02` | [S06](https://www.anthropic.com/engineering/building-effective-agents) / [S17](https://docs.langchain.com/oss/python/learn) | 强制工具失败/循环上限/断点重启，证明 fail-closed | 可重复 Trace、停止与恢复断言 |
| `AI09` | 多 Agent 编排与人机协作 | 只有单 Agent 证据不足才增加角色协作 | `AI08` | [S06](https://www.anthropic.com/engineering/building-effective-agents) / [S17](https://docs.langchain.com/oss/python/learn) | 比较单/多 Agent 的成功率与维护成本，回放交接失败 | 消融报告与责任边界 |
| `AI10` | 多模态/OCR/语音/图片 | 处理上游识别错误与人工纠错 | `AI01` | [S19](https://developers.google.com/machine-learning/crash-course) / [S04](https://pair.withgoogle.com/guidebook-v2/) | 用公开/合成样本比较 OCR 错误如何影响最终任务 | 端到端分母与人工纠错数据 |
| `AI11` | AI Eval/金标/回归 | 把效果变成可复算的质量门禁 | `AI01`、`PM07` | [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) / [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | 建立正常/边界/对抗/拒答集并审计 LLM judge 偏差 | 金标版本/分母/标注与回归报告 |
| `AI12` | AI 安全/Prompt Injection/模型治理 | 隔离不可信上下文与高风险工具 | `AI05`、`AI11`、`ENG06` | [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 设计注入/越权/数据外泄/过度代理负例 | 无未授权副作用的安全测试证据 |
| `AI13` | 模型选型/推理与成本 | 按质量、时延、成本、隐私与可迁移性选模型 | `AI01`、`AI11` | [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) / [S19](https://developers.google.com/machine-learning/crash-course) | 相同金标对比两方案端到端成功任务成本/P95 | 选型 ADR 和不确定性 |
| `AI14` | 微调/后训练选型判断 | 知道何时 RAG/Prompt 不够、是否值得训练 | `AI11`、`AI13` | [S19](https://developers.google.com/machine-learning/crash-course) / [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | 对错误类型分类，比较不训练/微调的投入与效益 | 门槛与数据许可/离线评测方案 |

## 产品工程（14 个知识点）

| 节点 | 内容 | 在产品中解决什么 | 逻辑关联/前置 | 官方/原作者资料 | 动手任务 | 留下什么证据 |
|---|---|---|---|---|---|---|
| `ENG01` | Web/HTTP/DNS/TLS | 理解浏览器→代理→服务的请求路径 | `PM07` | [S10](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 画从浏览器到后端请求链并定位 401/502/超时 | 请求/响应抓包与原因分析 |
| `ENG02` | 前端组件/状态/TypeScript | 保证数据展示、交互与错误状态一致 | `ENG01`、`PM08` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S21](https://nextjs.org/docs/app/getting-started/deploying) | 搭建可交互表单，注入失败/重复点击/刷新 | 前端状态测试和构建日志 |
| `ENG03` | API 契约与输入验证 | 设计清晰请求/响应和错误边界 | `ENG01`、`PM07` | [S10](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [S11](https://fastapi.tiangolo.com/tutorial/security/) | 写三接口 schema，覆盖非法输入、错误与幂等键 | OpenAPI/集成测试与日志 |
| `ENG04` | SQL/事务/迁移 | 持久化数据并在失败时保持一致 | `ENG03` | [S13](https://www.postgresql.org/docs/current/tutorial.html) | 模拟事务失败、回滚、唯一索引与迁移降级 | 事务与迁移回滚测试 |
| `ENG05` | 数据模型/对象存储/缓存 | 区分结构化数据、文件、缓存的一致性责任 | `ENG04` | [S13](https://www.postgresql.org/docs/current/tutorial.html) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 用合成文档测数据版本与缓存失效 | TTL/删除/备份策略和过期负例 |
| `ENG06` | AuthN/AuthZ/多租户隔离 | 身份验证不等于授权；每个数据读写检查权限 | `ENG03`、`ENG04` | [S11](https://fastapi.tiangolo.com/tutorial/security/) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 用户 A 与 B 交叉读写、伪造角色与过期令牌 | 横向越权测试和审计 |
| `ENG07` | 异步任务/队列/SSE/状态 | 处理长任务、重试、状态转移与前端反馈 | `ENG03`、`ENG04` | [S10](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [S17](https://docs.langchain.com/oss/python/learn) | Mock 长任务重复执行/中断/重新连接 | 幂等+状态恢复+前端错误态测试 |
| `ENG08` | 分布式可靠性与故障恢复 | 掌握超时/重试/限流/熔断/幂等/退避 | `ENG07` | [S12](https://fastapi.tiangolo.com/deployment/concepts/) / [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 模拟 429/500、网络断开、死信与重复消息 | 可控故障注入与恢复证据 |
| `ENG09` | 测试金字塔与契约测试 | 用单元/集成/E2E/安全负例锁定行为 | `ENG03`、`PM07` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 为主流程加两条失败场景和一条 E2E | 测试命令、版本与失败报告 |
| `ENG10` | Web 安全/输入/依赖供应链 | 覆盖常见 Web 攻击、依赖风险与敏感配置 | `ENG06`、`ENG09` | [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) / [S23](https://owasp.org/projects/top-ten) | 执行授权/注入/泄密测试与依赖清单审查 | 无硬失败的安全负例 |
| `ENG11` | 容器/环境与配置管理 | 在新环境稳定启动并区分配置与密钥 | `ENG03`、`ENG04` | [S12](https://fastapi.tiangolo.com/deployment/concepts/) / [S15](https://docs.docker.com/compose/how-tos/production/) | 干净环境 Docker Compose 启动/重启并拒绝缺密钥 | 复现、健康检查、重启与日志 |
| `ENG12` | 部署拓扑与架构演化 | 选单体、模块化和服务拆分的迁移边界 | `ENG11`、`PM06` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S21](https://nextjs.org/docs/app/getting-started/deploying) | 用 ADR 比较 Next.js 全栈、FastAPI、BFF、拆服务成本 | 部署图、数据边界与可逆迁移演练 |
| `ENG13` | 前端 SEO/性能/可访问性 | 确保公开站点可被发现、可访问、可用 | `ENG02` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S09](https://www.w3.org/WAI/WCAG22/quickref/) | 测关键路径的性能/语义/键盘操作和错误状态 | Lighthouse/人工辅助验收记录（按任务定阈） |
| `ENG14` | API 文档/版本化/兼容性 | 防止前后端与外部集成被破坏 | `ENG03`、`ENG09` | [S10](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 旧客户端回放，新版本新增字段/删除字段对照 | 兼容性案例与变更计划 |

## 生产运营（6 个知识点）

| 节点 | 内容 | 在产品中解决什么 | 逻辑关联/前置 | 官方/原作者资料 | 动手任务 | 留下什么证据 |
|---|---|---|---|---|---|---|
| `OPS01` | CI/CD/Release/回滚 | 保障从提交到发布的证据链 | `ENG09`、`ENG11` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S15](https://docs.docker.com/compose/how-tos/production/) | 在测试环境跑构建/测试/迁移检查/回滚演练 | CI run、固定 SHA、部署与回滚记录 |
| `OPS02` | 日志/Trace/指标/SLI-SLO | 从症状定位检索/模型/工具/数据库瓶颈 | `ENG03` | [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 为请求串联 trace_id, 隐去 PII 并模拟超时定位 | Trace、告警与用户视角 SLI |
| `OPS03` | 容量/压测/成本上限 | 识别瓶颈与安全容量，不只看单次延迟 | `OPS02`、`ENG08` | [S12](https://fastapi.tiangolo.com/deployment/concepts/) / [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 合成压测并记录 P95/错误率/调用成本 | 负载曲线和容量保护决策 |
| `OPS04` | 备份/恢复/事故响应 | 恢复数据与服务且留下审计复盘 | `ENG04`、`OPS01` | [S12](https://fastapi.tiangolo.com/deployment/concepts/) / [S15](https://docs.docker.com/compose/how-tos/production/) | 测试备份恢复、机密泄露撤销/密钥轮换预案 | 恢复演练日志与 RPO/RTO 假设 |
| `OPS05` | 数据隐私/合规/删除与审计 | 权利、使用许可、最小化与数据生命周期 | `ENG06`、`AI12` | [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 模拟撤回授权/删除数据与日志保留冲突 | 授权矩阵、删除演练与审计边界 |
| `OPS06` | 真实用户 UAT/发布与维护门禁 | 可运行不等于经用户验证/可长期运营 | `OPS01`、`OPS02`、`PM09`、`AI11` | [S04](https://pair.withgoogle.com/guidebook-v2/) / [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 执行干净环境 UAT+故障注入，列责任/回滚/值班 | 发布包，明确证据和未证实项 |

## 数据与增长（4 个知识点）

| 节点 | 内容 | 在产品中解决什么 | 逻辑关联/前置 | 官方/原作者资料 | 动手任务 | 留下什么证据 |
|---|---|---|---|---|---|---|
| `DATA01` | 事件埋点/北极星/漏斗 | 度量真实用户价值而不是请求数 | `PM02` | [S20](https://www.amplitude.com/guides/product-analytics) | 定义 task_started/completed 与转化分母 | 事件字典及合成样本复算 |
| `DATA02` | Cohort 留存与归因 | 分析用户是否反复获得价值及偏差 | `DATA01` | [S20](https://www.amplitude.com/guides/product-analytics) | 计算按 cohort 留存，解释抽样偏差与数据缺失 | SQL/电子表样例与分母 |
| `DATA03` | 实验设计/A-B/反事实 | 区分相关与因果、守门指标与提前停止风险 | `DATA01`、`PM06` | [S20](https://www.amplitude.com/guides/product-analytics) / [S01](https://www.atlassian.com/agile/product-management/discovery) | 预注册实验假设、样本、指标、守门与停止规则 | 合成分析报告不冒充线上提升 |
| `DATA04` | 增长飞轮/渠道/留存生命周期 | Growth Loop 将每次成功的用户体验、分发、获取与再参与形成反馈链，且需有真实转化与持续价值证据。 | `DATA02`、`BIZ04` | [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) / [S37](https://www.atlassian.com/agile/product-management/discovery) | 画一个渠道→激活→成功→推荐→新客户的闭环并找断点 | 事件/时间窗/分母、自然回访与人工推动分开 |

## 商业化与销售（12 个知识点）

| 节点 | 内容 | 在产品中解决什么 | 逻辑关联/前置 | 官方/原作者资料 | 动手任务 | 留下什么证据 |
|---|---|---|---|---|---|---|
| `BIZ01` | Buyer/采购/价值与定价 | 真正知道谁可以付费、以什么单位付费 | `PM05` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 画买方/用户/审批/采购图，列定价验证途径 | 买方验证计划、未知项与停止条件 |
| `BIZ02` | 单位经济/CAC/LTV/现金流 | 避免以贡献毛利冒充净利润或获客/收入事实 | `BIZ01`、`DATA02` | [S20](https://www.amplitude.com/guides/product-analytics) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 用三档情景计算单成功任务成本、贡献毛利和回本假设 | 带分母和敏感性的情景表 |
| `BIZ03` | 支付/订阅/计费需求设计 | 买方报价到技术账单/退款/对账的边界 | `BIZ01`、`ENG06`、`ENG04` | [S13](https://www.postgresql.org/docs/current/tutorial.html) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 合成支付 webhook 乱序/重复与套餐权限切换 | 对账/幂等/取消/退款需求和负例 |
| `BIZ04` | 渠道/增长/留存商业验证 | 找到可触达渠道而非只看总用户规模 | `BIZ01`、`DATA01` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S20](https://www.amplitude.com/guides/product-analytics) | 设计一项小规模可逆获客假设与转化衡量 | 样本分母、渠道成本及停止条件 |
| `BIZ05` | 产品组合/Go-to-market/客户支持 | 承诺范围、交付、支持和升级路径 | `BIZ01`、`PM11` | [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) / [S01](https://www.atlassian.com/agile/product-management/discovery) | 模拟试点条款、交付/支持边界、成功/失败定义 | 可审查试点计划与非目标 |
| `BIZ06` | ICP 与销售线索验证 | Ideal Customer Profile 表达有相似购买条件的客户类型，销售线索需要区分关注、询问、试点、成交与付费证据。 | `BIZ01`、`PM03` | [S31](https://www.strategyzer.com/library/the-value-proposition-canvas) / [S30](https://www.strategyzer.com/library/the-business-model-canvas) | 设计 2 类 ICP 和从接触到签约的漏斗口径 | 线索来源/授权/阶段/分母，未付费不冒充订单 |
| `BIZ07` | B2B 采购/谈判/合同交付边界 | 企业采购涉及使用方/决策方/采购/法务/财务的多方流程、试点要求、验收/合同风险与总拥有成本。 | `BIZ06`、`PM16` | [S33](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 模拟采购角色链、POC 目标、里程碑验收与变更争议 | 无敏感信息的 RACI、验收和升级流程 |
| `BIZ08` | 商业模式画布 BMC/价值主张 VPC | Business Model Canvas 用九要素描述如何创造、交付、获取价值；Value Proposition Canvas 对齐 Customer Jobs/Pains/Gains 与产品价值。 | `PM05`、`BIZ01` | [S30](https://www.strategyzer.com/library/the-business-model-canvas) / [S31](https://www.strategyzer.com/library/the-value-proposition-canvas) | 用两个不同客户群画出 BMC/VPC 并标核心未知 | 假设矩阵和可推翻商业模式的试验 |
| `BIZ09` | 经营财务/现金流/预算预测 | 现金流是现金实际进出的时间分布，区别于利润和贡献毛利；预算和现金缓冲约束产品投资节奏。 | `BIZ02` | [S30](https://www.strategyzer.com/library/the-business-model-canvas) / [S33](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) | 用合成账单按月模拟回款延迟、退款与服务器成本翻倍 | 现金流表、情景敏感性、停止预算门槛 |
| `BIZ10` | GTM 上市/渠道与营销销售协同 | Go-to-Market 协同定位、定价、渠道、营销、销售、客户成功与上市指标，需区分获客与任务价值。 | `BIZ06`、`BIZ04` | [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) / [S37](https://www.atlassian.com/agile/product-management/discovery) | 设计一个低成本 GTM 假设：渠道→激活→试用→保留 | 渠道漏斗指标与真实/合成证据分层 |
| `BIZ11` | 定价研究与收费实验 | 定价策略区分计价单位、价值捕获、支付意愿证据、价格实验、合同限制及边际成本。 | `BIZ01`、`DATA03` | [S30](https://www.strategyzer.com/library/the-business-model-canvas) / [S31](https://www.strategyzer.com/library/the-value-proposition-canvas) | 比较席位/按任务/订阅套餐，制定可逆的价格验证协议 | 价格假设来源、退款/毛利与真实付费分离 |
| `BIZ12` | SaaS 订阅产品规则/生命周期 | 订阅产品管理涉及配额、升级降级、试用、账单周期、续费、取消、退款、权限与数据留存协同。 | `BIZ03`、`BIZ09` | [S30](https://www.strategyzer.com/library/the-business-model-canvas) / [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) | 一份含重复 webhook/配额/取消/退款的产品规则与测试 | 规则状态机、权责边界和未授权操作拒绝 |

## 组织与管理（5 个知识点）

| 节点 | 内容 | 在产品中解决什么 | 逻辑关联/前置 | 官方/原作者资料 | 动手任务 | 留下什么证据 |
|---|---|---|---|---|---|---|
| `MGT01` | 战略与资源配置管理 | 战略管理是在资源约束下选择竞争方向、投资重点、机会成本和阶段目标，持续拒绝低价值事项。 | `PM06`、`BIZ08` | [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 预算减半下重排 3 条路线，写出不做理由 | 决策来源、成本、反证、复核日期 |
| `MGT02` | 项目与风险管理 | 项目管理围绕具体目标的范围、进度、成本、质量、风险、依赖和干系人协调，不等于产品发现。 | `PM17` | [S33](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) / [S32](https://scrumguides.org/scrum-guide.html?lang=en) | 列 RACI/风险登记/里程碑/验收及变更示例 | 范围变更与风险响应演练 |
| `MGT03` | 组织协作/角色与委派 | 跨职能协作使用明确决策权、授权、激励、反馈和升级机制，人员管理只有真实团队触发时深入。 | `PM16`、`MGT02` | [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 模拟冲突：设计、技术、销售在上线前争议权衡 | 职责矩阵、升级条件和沟通脚本 |
| `MGT04` | 流程治理/标准化与风险 | Product Ops/流程治理建立重复可靠的决策日志、发布审批、变更、异常与风险响应制度。 | `PM10`、`ENG10` | [S36](https://www.atlassian.com/agile/product-management/product-operating-model) / [S33](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) | 从一次合成事故写 SOP、监控信号、回滚/审批 | 根因、控制点、责任与复测规则 |
| `MGT05` | 管理决策复盘与人机共练 | Decision Review 通过记录当时证据、备选、概率、停止阈值和事后结果进行校准，避免事后诸葛亮。 | `MGT01`、`COG01` | [S25](https://www.svpg.com/product-management-an-introduction/) / [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) | 写一份决策日志，用 AI 反方质疑后关闭 AI 做新案例 | 原始预测、到期核验、人审与反证 |

## 认知与决策（3 个知识点）

| 节点 | 内容 | 在产品中解决什么 | 逻辑关联/前置 | 官方/原作者资料 | 动手任务 | 留下什么证据 |
|---|---|---|---|---|---|---|
| `COG01` | 证据等级/预测校准 | Evidence Calibration 将可观察事实、推断、猜测及预测概率分离，用结果反馈改进决策可靠性。 | `PM03` | [S27](https://www.producttalk.org/glossary-discovery-product-discovery/) / [S25](https://www.svpg.com/product-management-an-introduction/) | 对 10 个可判定判断写概率、来源和截止日 | 预测与结果分离、校准复盘与未知标记 |
| `COG02` | 系统思维/因果与反馈环 | Systems Thinking 把变量、延迟、约束和反馈循环放入因果假设图，区分相关与因果。 | `DATA03`、`PM06` | [S27](https://www.producttalk.org/glossary-discovery-product-discovery/) / [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) | 画获客→成本→服务→满意→留存的因果与反作用图 | 至少两个替代解释和干预/观察计划 |
| `COG03` | 认知偏差/反事实与决策质量 | Cognitive Bias 管理关注确认偏误、幸存者偏差、沉没成本与可得性等如何扭曲研究与产品选择。 | `COG01` | [S25](https://www.svpg.com/product-management-an-introduction/) / [S29](https://www.nngroup.com/articles/which-ux-research-methods/) | 给案例找三种反证、陌生人群/成本情景 | 明确偏差、反事实和可改变结论的证据 |

## 行业与合规（3 个知识点）

| 节点 | 内容 | 在产品中解决什么 | 逻辑关联/前置 | 官方/原作者资料 | 动手任务 | 留下什么证据 |
|---|---|---|---|---|---|---|
| `ETH01` | 可访问性/公平性/可信产品 | 识别被忽视的用户群、误导与伤害 | `PM08`、`AI11` | [S09](https://www.w3.org/WAI/WCAG22/quickref/) / [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | 设计对抗/边缘用户与人工接管样本 | 可测试公平性/可用性风险记录 |
| `GO01` | 行业知识/采购/政策约束 | 行业产品管理需要理解领域工作流、购买流程、监管边界和机构激励，不能把通用互联网增长经验机械照搬。 | `PM05`、`BIZ07` | [S33](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 针对指定行业列使用者/采购者/数据许可/验收规则 | 可溯源规则与专家复核需求，未知不猜 |
| `GO02` | 合同/知识产权/AI 数据治理责任 | 上市和商业交付需要对数据许可、IP、保留/删除、合同交付、审计与责任划分进行风险核查。 | `OPS05`、`MGT04` | [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 建立数据流、保留/删除、来源许可、第三方责任与升级审查 | 拒绝无权数据使用、人工专业审查、审计链 |


## 新增知识卡的专业定义与大白话对照

### PM13 · 机会解决方案树 OST

**专业定义**：Opportunity Solution Tree 用可衡量成果 Outcome 组织用户机会、候选方案和待验证假设之间的因果关系。

**大白话**：像医生先确定要治好的症状，再找可能病因，最后比较治疗方法；不是先买药再找病。

**何时学习**：产品需求很多且不知道为什么做。

**必须做**：画一棵 1 结果→3 机会→各2方案→关键假设的树，并提出反证。

**通过证据**：可追溯 Outcome/Opportunity/Solution/Assumption，三种不是同一层。

**关联上游资料**：[UP05 Founder 需求到能力](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/problem-to-capability-learning-loop-20261029.md) / [UP15 Founder 研究 GitHub 索引](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-problem-founder-research-20261029.md)。

### PM14 · 研究方法选型与三角验证

**专业定义**：按探索/评估目标，组合定性行为研究、可用性研究和定量实验，并识别抽样与观察偏差。

**大白话**：想知道‘为什么不买’要看人做事、问原因；想知道‘多少人没买’才看数据，不能拿一把尺子量所有问题。

**何时学习**：访谈和问卷结论矛盾。

**必须做**：同一合成现象提出访谈、观察、日志分析各能/不能回答的问题。

**通过证据**：方法决策表、证据缺口和至少一项相反解释。

**关联上游资料**：由本仓权威资料支撑。

### PM15 · OKR/Outcome/北极星对齐

**专业定义**：OKR 将目标与关键结果建立可观察的对齐关系；北极星表达长期核心用户价值，关键结果不应等同任务清单。

**大白话**：目标是让顾客吃得满意，不是‘装修5面墙’；墙是行动，顾客回来才是结果。

**何时学习**：Roadmap 全是功能和进度。

**必须做**：把十条功能需求转换成目标、结果与可证伪指标。

**通过证据**：结果指标、领先输入和守门指标齐全，不以工作量充成果。

**关联上游资料**：由本仓权威资料支撑。

### PM16 · Stakeholder 利益相关者与决策权

**专业定义**：Stakeholder 管理识别使用者、买方、技术、设计、法务、运营、审批者的目标与决策权，建立可沟通的责任分工。

**大白话**：开餐馆时顾客、厨师、财务、消防各有话语权；不明确谁拍板就会互相打架。

**何时学习**：部门意见冲突。

**必须做**：绘制 6 角色影响-兴趣矩阵与可升级的责任表。

**通过证据**：决策/执行/咨询/知会与冲突升级说明。

**关联上游资料**：[UP01 管理八域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/management-demand-to-practice-20261029.md)。

### PM17 · 产品交付与项目控制

**专业定义**：产品交付管理通过范围、依赖、风险、验收、沟通和发布计划将持续发现转为可靠增量。

**大白话**：厨师研究新菜属于产品，按时出菜、食材不断供属于交付；不能把排期表当产品价值。

**何时学习**：项目延期或频繁变更。

**必须做**：为模拟 2 周 Release 列 WBS/依赖/风险、UAT 与风险预警。

**通过证据**：明确范围、风险责任、变更处理和实际复盘。

**关联上游资料**：[UP13 产品工程判断](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/product-engineering-demand-to-practice-20261029.md) / [UP16 产品工程技术路线](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/ai-product-engineer-roadmap-20261028.md)。

### PM18 · Product Operating Model / 产品组织运作

**专业定义**：产品运营模式规定产品目标、团队授权、决策权、发现-交付流程与反馈治理的协作系统。

**大白话**：不仅有菜谱，还要规定谁试菜、谁拍板、谁上菜、谁追踪差评。

**何时学习**：团队功能多但交付与发现割裂。

**必须做**：绘制产品三人组或单人多角色职责、决策与审查节奏。

**通过证据**：发现与交付双向信息流和决策责任表。

**关联上游资料**：[UP01 管理八域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/management-demand-to-practice-20261029.md)。

### PM19 · 市场定位和竞争差异化

**专业定义**：定位通过目标细分、竞争参照和价值差异解释为何特定用户应选择此产品。

**大白话**：同一条街开饭馆，要先决定给谁吃、与旁边家相比为何值得走进来。

**何时学习**：功能同质化/找不到用户。

**必须做**：选择 2 类买方，做替代方案/差异对比与反证。

**通过证据**：一句可验证定位 + 数据/访问证据分层。

**关联上游资料**：由本仓权威资料支撑。

### PM20 · 用户旅程/服务蓝图

**专业定义**：Customer Journey Map 描述跨触点用户体验，Service Blueprint 同时揭示前台和后台流程/交接。

**大白话**：客人从看到招牌、点餐、支付到售后是一整趟旅程，不只是一张点单页面。

**何时学习**：单个页面正常但完整任务失败。

**必须做**：绘制前台动作、后台 API/人员、跨触点失败与恢复。

**通过证据**：服务蓝图、可观察触点和错误恢复用例。

**关联上游资料**：由本仓权威资料支撑。

### PM21 · 平台型产品/API 产品思维

**专业定义**：平台产品把内部能力以 API/组件/权限及 SLA 形式交给其他团队或第三方消费，需同时关注开发者体验和兼容成本。

**大白话**：普通餐馆直接卖饭；中央厨房则要让很多店能稳定调用它的能力。

**何时学习**：多团队要复用 AI 能力。

**必须做**：写 API 消费者故事、版本契约、配额、失败响应与支持范围。

**通过证据**：兼容变更、租户隔离与文档演练。

**关联上游资料**：[UP12 SaaS 开发交付](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/playbooks/saas-business-system.md) / [UP16 产品工程技术路线](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/ai-product-engineer-roadmap-20261028.md)。

### PM22 · Pre-mortem 预演失败和产品风险矩阵

**专业定义**：Premortem 在投入前假设项目已失败，逆向列举原因、概率/影响、应对、可检测信号和责任。

**大白话**：开店前想象开业后差评爆炸：是选址、食材、排队还是食品安全？提前设警报。

**何时学习**：做决策总是乐观估计。

**必须做**：模拟产品上线失败，列 8 个失败假设并按四大风险分类。

**通过证据**：风险登记、观测信号、Stop/降级门槛。

**关联上游资料**：[UP13 产品工程判断](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/product-engineering-demand-to-practice-20261029.md) / [UP17 企业产品工程实战](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-product-engineering-market-track.md)。

### PM23 · 产品生命周期/停用与迁移

**专业定义**：Product Lifecycle Management 关注验证、增长、成熟、衰退或停用阶段的产品投资、用户迁移与支持义务。

**大白话**：菜卖不动也不能突然把老顾客预付的套餐作废；停卖要通知、退款或迁移。

**何时学习**：功能过多/需要下线旧产品。

**必须做**：制定产品停用公告、数据导出/删除、用户迁移、合同边界。

**通过证据**：停用清单与用户影响/回滚方案。

**关联上游资料**：由本仓权威资料支撑。

### BIZ06 · ICP 与销售线索验证

**专业定义**：Ideal Customer Profile 表达有相似购买条件的客户类型，销售线索需要区分关注、询问、试点、成交与付费证据。

**大白话**：有人夸你菜香不等于订座，更不等于结账；先找真正有预算又急需解决问题的人。

**何时学习**：流量高但没有真实买家。

**必须做**：设计 2 类 ICP 和从接触到签约的漏斗口径。

**通过证据**：线索来源/授权/阶段/分母，未付费不冒充订单。

**关联上游资料**：[UP04 Founder 产品机会](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/problem-founder-market-roadmap-20261029.md) / [UP06 营销与销售路线](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/marketing-sales-market-roadmap-20261029.md) / [UP07 营销销售 16 域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/marketing-sales-demand-to-practice-20261029.md) / [UP15 Founder 研究 GitHub 索引](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-problem-founder-research-20261029.md) / [UP22 多产品经营与真实商业边界](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/buyer-order-evidence-gap-2026-10-25.md)。

### BIZ07 · B2B 采购/谈判/合同交付边界

**专业定义**：企业采购涉及使用方/决策方/采购/法务/财务的多方流程、试点要求、验收/合同风险与总拥有成本。

**大白话**：顾客喜欢菜，不等于餐饮集团采购会签合同；还得过预算、食安、发票和合同。

**何时学习**：企业客户问法务/SLA/POC。

**必须做**：模拟采购角色链、POC 目标、里程碑验收与变更争议。

**通过证据**：无敏感信息的 RACI、验收和升级流程。

**关联上游资料**：[UP11 行业与采购实践](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/industry-insider-market-roadmap-20261029.md) / [UP21 社会商业交往](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/social-business-market-roadmap-20261029.md)。

### BIZ08 · 商业模式画布 BMC/价值主张 VPC

**专业定义**：Business Model Canvas 用九要素描述如何创造、交付、获取价值；Value Proposition Canvas 对齐 Customer Jobs/Pains/Gains 与产品价值。

**大白话**：一张画布把谁来吃、卖什么、怎么获客、食材成本、怎样赚钱放同一桌上比较。

**何时学习**：方向好像可行但说不清商业逻辑。

**必须做**：用两个不同客户群画出 BMC/VPC 并标核心未知。

**通过证据**：假设矩阵和可推翻商业模式的试验。

**关联上游资料**：[UP04 Founder 产品机会](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/problem-founder-market-roadmap-20261029.md) / [UP08 商业与财富经营 12 域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/wealth-business-market-roadmap-20261029.md) / [UP15 Founder 研究 GitHub 索引](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-problem-founder-research-20261029.md) / [UP22 多产品经营与真实商业边界](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/buyer-order-evidence-gap-2026-10-25.md)。

### BIZ09 · 经营财务/现金流/预算预测

**专业定义**：现金流是现金实际进出的时间分布，区别于利润和贡献毛利；预算和现金缓冲约束产品投资节奏。

**大白话**：饭馆账面赚钱，但供应商今天要付款、平台下月才结算，现金仍可能断。

**何时学习**：做得越多现金越紧。

**必须做**：用合成账单按月模拟回款延迟、退款与服务器成本翻倍。

**通过证据**：现金流表、情景敏感性、停止预算门槛。

**关联上游资料**：[UP08 商业与财富经营 12 域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/wealth-business-market-roadmap-20261029.md) / [UP10 企业财务与经济](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/finance-economics-market-roadmap-20261029.md) / [UP19 财富与商业研究](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-wealth-business-research-20261029.md)。

### BIZ10 · GTM 上市/渠道与营销销售协同

**专业定义**：Go-to-Market 协同定位、定价、渠道、营销、销售、客户成功与上市指标，需区分获客与任务价值。

**大白话**：菜做得好不意味着路人知道；要告诉对的人、给试吃路径、回看是否复购。

**何时学习**：产品上线但无人知晓。

**必须做**：设计一个低成本 GTM 假设：渠道→激活→试用→保留。

**通过证据**：渠道漏斗指标与真实/合成证据分层。

**关联上游资料**：[UP06 营销与销售路线](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/marketing-sales-market-roadmap-20261029.md) / [UP07 营销销售 16 域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/marketing-sales-demand-to-practice-20261029.md) / [UP18 营销漏斗合成实验](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/labs/marketing-sales-funnel-20261029/README.md)。

### BIZ11 · 定价研究与收费实验

**专业定义**：定价策略区分计价单位、价值捕获、支付意愿证据、价格实验、合同限制及边际成本。

**大白话**：饭馆是按位收费、按菜收费还是套餐？先看顾客买的价值和实际成本，不靠拍脑袋。

**何时学习**：不会决定按席位还是按调用收费。

**必须做**：比较席位/按任务/订阅套餐，制定可逆的价格验证协议。

**通过证据**：价格假设来源、退款/毛利与真实付费分离。

**关联上游资料**：[UP07 营销销售 16 域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/marketing-sales-demand-to-practice-20261029.md) / [UP19 财富与商业研究](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-wealth-business-research-20261029.md)。

### BIZ12 · SaaS 订阅产品规则/生命周期

**专业定义**：订阅产品管理涉及配额、升级降级、试用、账单周期、续费、取消、退款、权限与数据留存协同。

**大白话**：月卡买了却被重复扣费、取消后数据没处理，就是产品规则和工程没连起来。

**何时学习**：设计 AI SaaS 付费套餐。

**必须做**：一份含重复 webhook/配额/取消/退款的产品规则与测试。

**通过证据**：规则状态机、权责边界和未授权操作拒绝。

**关联上游资料**：[UP08 商业与财富经营 12 域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/wealth-business-market-roadmap-20261029.md) / [UP12 SaaS 开发交付](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/playbooks/saas-business-system.md)。

### MGT01 · 战略与资源配置管理

**专业定义**：战略管理是在资源约束下选择竞争方向、投资重点、机会成本和阶段目标，持续拒绝低价值事项。

**大白话**：你只有一台炉灶，什么菜先做、什么菜不卖，比把菜单写满更重要。

**何时学习**：要在多个业务方向取舍。

**必须做**：预算减半下重排 3 条路线，写出不做理由。

**通过证据**：决策来源、成本、反证、复核日期。

**关联上游资料**：[UP01 管理八域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/management-demand-to-practice-20261029.md) / [UP02 管理条件式 Roadmap](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/management-market-roadmap-20261029.md) / [UP03 管理练习](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-management-market-track-20261029.md) / [UP08 商业与财富经营 12 域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/wealth-business-market-roadmap-20261029.md) / [UP20 管理独立考核](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/assessments/management-independent-rubric.md)。

### MGT02 · 项目与风险管理

**专业定义**：项目管理围绕具体目标的范围、进度、成本、质量、风险、依赖和干系人协调，不等于产品发现。

**大白话**：菜单好不好是产品问题；订单能否安全、准时送到是项目问题。

**何时学习**：项目延期/跨团队冲突。

**必须做**：列 RACI/风险登记/里程碑/验收及变更示例。

**通过证据**：范围变更与风险响应演练。

**关联上游资料**：[UP01 管理八域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/management-demand-to-practice-20261029.md) / [UP02 管理条件式 Roadmap](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/management-market-roadmap-20261029.md) / [UP03 管理练习](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-management-market-track-20261029.md) / [UP14 管理研究 GitHub 索引](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-management-research-20261029.md) / [UP20 管理独立考核](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/assessments/management-independent-rubric.md)。

### MGT03 · 组织协作/角色与委派

**专业定义**：跨职能协作使用明确决策权、授权、激励、反馈和升级机制，人员管理只有真实团队触发时深入。

**大白话**：主厨、服务员、采购要配合，没人负责收尾就会反复漏单。

**何时学习**：多人协作后职责不清。

**必须做**：模拟冲突：设计、技术、销售在上线前争议权衡。

**通过证据**：职责矩阵、升级条件和沟通脚本。

**关联上游资料**：[UP01 管理八域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/management-demand-to-practice-20261029.md) / [UP02 管理条件式 Roadmap](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/management-market-roadmap-20261029.md) / [UP14 管理研究 GitHub 索引](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-management-research-20261029.md) / [UP21 社会商业交往](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/social-business-market-roadmap-20261029.md)。

### MGT04 · 流程治理/标准化与风险

**专业定义**：Product Ops/流程治理建立重复可靠的决策日志、发布审批、变更、异常与风险响应制度。

**大白话**：厨房不是多请个厨师就能稳定，备料、卫生、交接的 SOP 决定不出事故。

**何时学习**：同样错误反复发生。

**必须做**：从一次合成事故写 SOP、监控信号、回滚/审批。

**通过证据**：根因、控制点、责任与复测规则。

**关联上游资料**：[UP01 管理八域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/management-demand-to-practice-20261029.md)。

### MGT05 · 管理决策复盘与人机共练

**专业定义**：Decision Review 通过记录当时证据、备选、概率、停止阈值和事后结果进行校准，避免事后诸葛亮。

**大白话**：当初为什么选这道菜，为什么后来卖得好？要拿当时的预测对照现实，不凭印象。

**何时学习**：每次复盘都无法说明变好原因。

**必须做**：写一份决策日志，用 AI 反方质疑后关闭 AI 做新案例。

**通过证据**：原始预测、到期核验、人审与反证。

**关联上游资料**：[UP01 管理八域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/management-demand-to-practice-20261029.md) / [UP03 管理练习](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-management-market-track-20261029.md) / [UP05 Founder 需求到能力](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/problem-to-capability-learning-loop-20261029.md) / [UP09 商业认知与判断](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/cognition-business-market-roadmap-20261029.md) / [UP14 管理研究 GitHub 索引](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-management-research-20261029.md) / [UP20 管理独立考核](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/assessments/management-independent-rubric.md)。

### COG01 · 证据等级/预测校准

**专业定义**：Evidence Calibration 将可观察事实、推断、猜测及预测概率分离，用结果反馈改进决策可靠性。

**大白话**：朋友说‘肯定大卖’不是销售数据；先记‘我有多大把握’，到期再看有没有猜对。

**何时学习**：容易把热度当真实需求。

**必须做**：对 10 个可判定判断写概率、来源和截止日。

**通过证据**：预测与结果分离、校准复盘与未知标记。

**关联上游资料**：[UP04 Founder 产品机会](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/problem-founder-market-roadmap-20261029.md) / [UP05 Founder 需求到能力](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/problem-to-capability-learning-loop-20261029.md) / [UP09 商业认知与判断](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/cognition-business-market-roadmap-20261029.md)。

### COG02 · 系统思维/因果与反馈环

**专业定义**：Systems Thinking 把变量、延迟、约束和反馈循环放入因果假设图，区分相关与因果。

**大白话**：打折后客流涨，可能利润却降；不能只盯‘客流’一个表盘。

**何时学习**：单个指标好但整体变差。

**必须做**：画获客→成本→服务→满意→留存的因果与反作用图。

**通过证据**：至少两个替代解释和干预/观察计划。

**关联上游资料**：[UP09 商业认知与判断](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/cognition-business-market-roadmap-20261029.md)。

### COG03 · 认知偏差/反事实与决策质量

**专业定义**：Cognitive Bias 管理关注确认偏误、幸存者偏差、沉没成本与可得性等如何扭曲研究与产品选择。

**大白话**：只问爱吃辣的熟人，就以为全城都爱辣；已经买了锅也不是继续赔钱的理由。

**何时学习**：做错了还想投入更多。

**必须做**：给案例找三种反证、陌生人群/成本情景。

**通过证据**：明确偏差、反事实和可改变结论的证据。

**关联上游资料**：[UP09 商业认知与判断](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/cognition-business-market-roadmap-20261029.md)。

### DATA04 · 增长飞轮/渠道/留存生命周期

**专业定义**：Growth Loop 将每次成功的用户体验、分发、获取与再参与形成反馈链，且需有真实转化与持续价值证据。

**大白话**：老客愿意分享才可能带来新客，狂发传单只能算曝光，不能算餐馆的口碑飞轮。

**何时学习**：曝光高但不留存。

**必须做**：画一个渠道→激活→成功→推荐→新客户的闭环并找断点。

**通过证据**：事件/时间窗/分母、自然回访与人工推动分开。

**关联上游资料**：[UP06 营销与销售路线](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/marketing-sales-market-roadmap-20261029.md) / [UP07 营销销售 16 域](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/market/marketing-sales-demand-to-practice-20261029.md) / [UP18 营销漏斗合成实验](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/labs/marketing-sales-funnel-20261029/README.md)。

### GO01 · 行业知识/采购/政策约束

**专业定义**：行业产品管理需要理解领域工作流、购买流程、监管边界和机构激励，不能把通用互联网增长经验机械照搬。

**大白话**：学校、医院、企业食堂都有不同审批和安全规矩，同样一道菜不能同样卖。

**何时学习**：做政企/行业 AI 产品。

**必须做**：针对指定行业列使用者/采购者/数据许可/验收规则。

**通过证据**：可溯源规则与专家复核需求，未知不猜。

**关联上游资料**：[UP11 行业与采购实践](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/industry-insider-market-roadmap-20261029.md)。

### GO02 · 合同/知识产权/AI 数据治理责任

**专业定义**：上市和商业交付需要对数据许可、IP、保留/删除、合同交付、审计与责任划分进行风险核查。

**大白话**：把顾客资料交给未经授权的外包厨师，即使菜做得好也可能出事。

**何时学习**：客户要求上传私有数据/跨区部署。

**必须做**：建立数据流、保留/删除、来源许可、第三方责任与升级审查。

**通过证据**：拒绝无权数据使用、人工专业审查、审计链。

**关联上游资料**：[UP12 SaaS 开发交付](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/playbooks/saas-business-system.md) / [UP17 企业产品工程实战](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-product-engineering-market-track.md)。


## 非线性使用示例

1. 客户喜欢 Demo 但迟迟不付款：直接查 `BIZ06` → 若不懂买方与用户差异才回溯 `BIZ01`；然后查 `PM05` 和上游 [Founder](../../resources/upstream-pm-knowledge-index.md)。
2. 管理团队混乱：直接查 `MGT03`，缺角色/范围/权限再补 `PM16`/`MGT02`。
3. 产品没方向：直接查 `PM13` 画 OST，再补 `COG01` 和 `BIZ08`；不必先学习高级模型。
4. 已能开发但产品无法上线：直接按 [发布 E1–E8](../launch/production-apprenticeship.md) 找到缺失门禁。

**严禁**把访问私仓研究成果、README 调研或合成演练当作真实客户、已安装工具或本人独立能力合格。技术实验在独立工程/学习仓保留原始证据。
