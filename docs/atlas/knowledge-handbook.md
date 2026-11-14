# 知识卡手册：知识点的作用、依赖、权威资料、实操与验收

> 内容来自 [唯一结构化 Atlas](knowledge-catalog.json)，更新机器目录时需同步本表；课程设计状态 NOT_RUN。本索引不是阶段课表，直接跳到**当前卡点**即可。资料中的官方文档仅确认页面可参考，不代表第三方实验已执行或版本适合当前项目。

每行依次给出：**知识点ID → 它解决什么问题 → 为什么关联其他知识 → 可读权威资料 → 必做实验 → 最低证据出口**。学习顺序以 [需求路由](../learning/demand-router.md) 为准。

## 产品发现、设计与决策

| ID | 作用/为什么学 | 逻辑前置（必要时回溯） | 权威资料 | 实操任务 | 需要留下的证据 |
|---|---|---|---|---|---|
| `PM01` | **角色分工与生命周期** — 识别问题-决策-交付-复盘的责任 | 无（随问题进入） | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S02](https://www.atlassian.com/agile/product-management/requirements) | 画出 PM/PE/设计/研发/销售的责任图并指出灰区 | 一份冲突决策表和验收责任人 |
| `PM02` | **问题定义与 JTBD** — 把功能需求翻译成用户待完成任务 | `PM01` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S04](https://pair.withgoogle.com/guidebook-v2/) | 从三条功能请求提炼任务/触发场景/成功行为 | 包含不做条件和失败反例的问题卡 |
| `PM03` | **访谈与行为证据** — 获得可以推翻假设的真实/合成事实 | `PM02` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S04](https://pair.withgoogle.com/guidebook-v2/) | 写非诱导访谈脚本并对照行为/陈述 | 事实/推断/假设台账及证据等级 |
| `PM04` | **竞品与替代方案** — 人工/旧系统/不用 AI 都是竞争 | `PM02` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 比较人工、规则、搜索、AI 并列反证 | 替代方案矩阵与停止门槛 |
| `PM05` | **价值主张与市场细分** — 确认谁痛、频率、可触达性及买方 | `PM03`, `PM04` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 区分用户/买方/采购责任，分场景估算触达 | 一张证据标注的细分/价值卡 |
| `PM06` | **优先级与路线图** — 确定先解决哪个风险而非堆功能 | `PM04`, `PM05` | [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 以 RICE 与明确约束各排一次同一需求，说明差异 | Now/Next/Later 决策与资源 Stop Rule |
| `PM07` | **PRD/用户故事/验收** — 把模糊目标变可测试行为 | `PM02` | [S02](https://www.atlassian.com/agile/product-management/requirements) | 完成一页 PRD + Given/When/Then 正负场景 | 可供他人不猜测地写测试的需求文档 |
| `PM08` | **信息架构/原型/UI 状态** — 从任务流设计空态/失败/等待/恢复 | `PM07` | [S04](https://pair.withgoogle.com/guidebook-v2/) / [S09](https://www.w3.org/WAI/WCAG22/quickref/) | 做两版低保真任务流和错误态原型 | 用户可观察任务结果与无障碍检查表 |
| `PM09` | **AI 信任与可控 UX** — 解释来源、错误、能力边界与人工控制 | `PM08`, `AI01` | [S04](https://pair.withgoogle.com/guidebook-v2/) / [S22](https://pair.withgoogle.com/guidebook-v2/chapters) | 设计引用/拒答/反馈/人工接管的三条流程 | 失败提示及真实/合成可用性测试记录 |
| `PM10` | **交付协作/范围与变更** — 定义变更责任、发布门禁与冲突处理 | `PM07` | [S02](https://www.atlassian.com/agile/product-management/requirements) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 模拟需求变更影响排期、权限、成本并作 ADR | 变更前后 UAT 与审批记录 |
| `PM11` | **客户成功/支持运营** — 将故障/投诉转成可重现事实与服务闭环 | `PM09`, `OPS02` | [S04](https://pair.withgoogle.com/guidebook-v2/) / [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 构建合成支持工单分级/升级/闭环规则 | 优先级、响应预案、重复故障分析 |
| `PM12` | **产品策略与 Portfolio 决策** — 判断多个产品/渠道哪个该停 | `PM06`, `BIZ01` | [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) / [S01](https://www.atlassian.com/agile/product-management/discovery) | 三候选预算减半时选唯一试验并解释淘汰项 | 资源配置和机会成本记录 |

## AI 技术与产品取舍

| ID | 作用/为什么学 | 逻辑前置（必要时回溯） | 权威资料 | 实操任务 | 需要留下的证据 |
|---|---|---|---|---|---|
| `AI01` | **LLM 基础与上下文/Token** — 理解生成不确定性、输入预算和限制 | `PM02` | [S19](https://developers.google.com/machine-learning/crash-course) / [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | 同题短/长上下文比较结构化输出与 Token/成本 | 输入-输出-成本与失败报告 |
| `AI02` | **Prompt/结构化输出** — 实现可校验输出而非靠自然语言猜测 | `AI01` | [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) / [S19](https://developers.google.com/machine-learning/crash-course) | 为合成分类任务比较规则/Prompt + JSON schema 校验 | 字段校验通过率和坏例日志 |
| `AI03` | **Embedding/检索与 RAG** — 区分索引、召回、排序、生成和证据 | `AI01`, `ENG04` | [S19](https://developers.google.com/machine-learning/crash-course) / [S17](https://docs.langchain.com/oss/python/learn) | 在公开小语料比较 BM25/向量/混检并分层评测 | 检索金标、引用支持、拒答与版本失败 |
| `AI04` | **RAG 数据治理/文档生命周期** — 处理来源许可、权限、更新、删除与版本 | `AI03`, `ENG06` | [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S17](https://docs.langchain.com/oss/python/learn) | 模拟文档撤销权限、版本更新、删除后不可检索 | 越权/旧版/删除负例 |
| `AI05` | **工具调用/Workflow/单 Agent** — 知道什么时候让模型决策、什么时候固定流程 | `AI02`, `ENG03` | [S06](https://www.anthropic.com/engineering/building-effective-agents) / [S17](https://docs.langchain.com/oss/python/learn) | Mock 工单比较规则链与工具 Agent 的正确率/成本 | 审批前无写入、超时与错误恢复 |
| `AI06` | **MCP/工具权限与副作用** — 工具连接不代表可以越权执行 | `AI05`, `ENG06` | [S18](https://blog.modelcontextprotocol.io/posts/2026-07-28/) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 在隔离工具沙箱检查 schema、租户权限、审批、审计 | 未授权拒绝、无副作用、版本兼容性记录 |
| `AI07` | **Context Engineering/Memory** — 在正确时机给模型正确的上下文与工具 | `AI01`, `AI05` | [S17](https://docs.langchain.com/oss/python/learn) / [S06](https://www.anthropic.com/engineering/building-effective-agents) | 对比上下文裁剪、版本过滤、checkpoint 恢复 | 同测试集效果/Token/恢复负例 |
| `AI08` | **Harness/Agent 执行治理** — 任务边界、预算、重试、停止、人工介入与恢复 | `AI05`, `AI07`, `OPS02` | [S06](https://www.anthropic.com/engineering/building-effective-agents) / [S17](https://docs.langchain.com/oss/python/learn) | 强制工具失败/循环上限/断点重启，证明 fail-closed | 可重复 Trace、停止与恢复断言 |
| `AI09` | **多 Agent 编排与人机协作** — 只有单 Agent 证据不足才增加角色协作 | `AI08` | [S06](https://www.anthropic.com/engineering/building-effective-agents) / [S17](https://docs.langchain.com/oss/python/learn) | 比较单/多 Agent 的成功率与维护成本，回放交接失败 | 消融报告与责任边界 |
| `AI10` | **多模态/OCR/语音/图片** — 处理上游识别错误与人工纠错 | `AI01` | [S19](https://developers.google.com/machine-learning/crash-course) / [S04](https://pair.withgoogle.com/guidebook-v2/) | 用公开/合成样本比较 OCR 错误如何影响最终任务 | 端到端分母与人工纠错数据 |
| `AI11` | **AI Eval/金标/回归** — 把效果变成可复算的质量门禁 | `AI01`, `PM07` | [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) / [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | 建立正常/边界/对抗/拒答集并审计 LLM judge 偏差 | 金标版本/分母/标注与回归报告 |
| `AI12` | **AI 安全/Prompt Injection/模型治理** — 隔离不可信上下文与高风险工具 | `AI05`, `AI11`, `ENG06` | [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 设计注入/越权/数据外泄/过度代理负例 | 无未授权副作用的安全测试证据 |
| `AI13` | **模型选型/推理与成本** — 按质量、时延、成本、隐私与可迁移性选模型 | `AI01`, `AI11` | [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) / [S19](https://developers.google.com/machine-learning/crash-course) | 相同金标对比两方案端到端成功任务成本/P95 | 选型 ADR 和不确定性 |
| `AI14` | **微调/后训练选型判断** — 知道何时 RAG/Prompt 不够、是否值得训练 | `AI11`, `AI13` | [S19](https://developers.google.com/machine-learning/crash-course) / [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | 对错误类型分类，比较不训练/微调的投入与效益 | 门槛与数据许可/离线评测方案 |

## 产品工程全栈

| ID | 作用/为什么学 | 逻辑前置（必要时回溯） | 权威资料 | 实操任务 | 需要留下的证据 |
|---|---|---|---|---|---|
| `ENG01` | **Web/HTTP/DNS/TLS** — 理解浏览器→代理→服务的请求路径 | `PM07` | [S10](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 画从浏览器到后端请求链并定位 401/502/超时 | 请求/响应抓包与原因分析 |
| `ENG02` | **前端组件/状态/TypeScript** — 保证数据展示、交互与错误状态一致 | `ENG01`, `PM08` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S21](https://nextjs.org/docs/app/getting-started/deploying) | 搭建可交互表单，注入失败/重复点击/刷新 | 前端状态测试和构建日志 |
| `ENG03` | **API 契约与输入验证** — 设计清晰请求/响应和错误边界 | `ENG01`, `PM07` | [S10](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [S11](https://fastapi.tiangolo.com/tutorial/security/) | 写三接口 schema，覆盖非法输入、错误与幂等键 | OpenAPI/集成测试与日志 |
| `ENG04` | **SQL/事务/迁移** — 持久化数据并在失败时保持一致 | `ENG03` | [S13](https://www.postgresql.org/docs/current/tutorial.html) | 模拟事务失败、回滚、唯一索引与迁移降级 | 事务与迁移回滚测试 |
| `ENG05` | **数据模型/对象存储/缓存** — 区分结构化数据、文件、缓存的一致性责任 | `ENG04` | [S13](https://www.postgresql.org/docs/current/tutorial.html) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 用合成文档测数据版本与缓存失效 | TTL/删除/备份策略和过期负例 |
| `ENG06` | **AuthN/AuthZ/多租户隔离** — 身份验证不等于授权；每个数据读写检查权限 | `ENG03`, `ENG04` | [S11](https://fastapi.tiangolo.com/tutorial/security/) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 用户 A 与 B 交叉读写、伪造角色与过期令牌 | 横向越权测试和审计 |
| `ENG07` | **异步任务/队列/SSE/状态** — 处理长任务、重试、状态转移与前端反馈 | `ENG03`, `ENG04` | [S10](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [S17](https://docs.langchain.com/oss/python/learn) | Mock 长任务重复执行/中断/重新连接 | 幂等+状态恢复+前端错误态测试 |
| `ENG08` | **分布式可靠性与故障恢复** — 掌握超时/重试/限流/熔断/幂等/退避 | `ENG07` | [S12](https://fastapi.tiangolo.com/deployment/concepts/) / [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 模拟 429/500、网络断开、死信与重复消息 | 可控故障注入与恢复证据 |
| `ENG09` | **测试金字塔与契约测试** — 用单元/集成/E2E/安全负例锁定行为 | `ENG03`, `PM07` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 为主流程加两条失败场景和一条 E2E | 测试命令、版本与失败报告 |
| `ENG10` | **Web 安全/输入/依赖供应链** — 覆盖常见 Web 攻击、依赖风险与敏感配置 | `ENG06`, `ENG09` | [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) / [S23](https://owasp.org/projects/top-ten) | 执行授权/注入/泄密测试与依赖清单审查 | 无硬失败的安全负例 |
| `ENG11` | **容器/环境与配置管理** — 在新环境稳定启动并区分配置与密钥 | `ENG03`, `ENG04` | [S12](https://fastapi.tiangolo.com/deployment/concepts/) / [S15](https://docs.docker.com/compose/how-tos/production/) | 干净环境 Docker Compose 启动/重启并拒绝缺密钥 | 复现、健康检查、重启与日志 |
| `ENG12` | **部署拓扑与架构演化** — 选单体、模块化和服务拆分的迁移边界 | `ENG11`, `PM06` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S21](https://nextjs.org/docs/app/getting-started/deploying) | 用 ADR 比较 Next.js 全栈、FastAPI、BFF、拆服务成本 | 部署图、数据边界与可逆迁移演练 |
| `ENG13` | **前端 SEO/性能/可访问性** — 确保公开站点可被发现、可访问、可用 | `ENG02` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S09](https://www.w3.org/WAI/WCAG22/quickref/) | 测关键路径的性能/语义/键盘操作和错误状态 | Lighthouse/人工辅助验收记录（按任务定阈） |
| `ENG14` | **API 文档/版本化/兼容性** — 防止前后端与外部集成被破坏 | `ENG03`, `ENG09` | [S10](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 旧客户端回放，新版本新增字段/删除字段对照 | 兼容性案例与变更计划 |

## 生产运营

| ID | 作用/为什么学 | 逻辑前置（必要时回溯） | 权威资料 | 实操任务 | 需要留下的证据 |
|---|---|---|---|---|---|
| `OPS01` | **CI/CD/Release/回滚** — 保障从提交到发布的证据链 | `ENG09`, `ENG11` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S15](https://docs.docker.com/compose/how-tos/production/) | 在测试环境跑构建/测试/迁移检查/回滚演练 | CI run、固定 SHA、部署与回滚记录 |
| `OPS02` | **日志/Trace/指标/SLI-SLO** — 从症状定位检索/模型/工具/数据库瓶颈 | `ENG03` | [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 为请求串联 trace_id, 隐去 PII 并模拟超时定位 | Trace、告警与用户视角 SLI |
| `OPS03` | **容量/压测/成本上限** — 识别瓶颈与安全容量，不只看单次延迟 | `OPS02`, `ENG08` | [S12](https://fastapi.tiangolo.com/deployment/concepts/) / [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 合成压测并记录 P95/错误率/调用成本 | 负载曲线和容量保护决策 |
| `OPS04` | **备份/恢复/事故响应** — 恢复数据与服务且留下审计复盘 | `ENG04`, `OPS01` | [S12](https://fastapi.tiangolo.com/deployment/concepts/) / [S15](https://docs.docker.com/compose/how-tos/production/) | 测试备份恢复、机密泄露撤销/密钥轮换预案 | 恢复演练日志与 RPO/RTO 假设 |
| `OPS05` | **数据隐私/合规/删除与审计** — 权利、使用许可、最小化与数据生命周期 | `ENG06`, `AI12` | [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 模拟撤回授权/删除数据与日志保留冲突 | 授权矩阵、删除演练与审计边界 |
| `OPS06` | **真实用户 UAT/发布与维护门禁** — 可运行不等于经用户验证/可长期运营 | `OPS01`, `OPS02`, `PM09`, `AI11` | [S04](https://pair.withgoogle.com/guidebook-v2/) / [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 执行干净环境 UAT+故障注入，列责任/回滚/值班 | 发布包，明确证据和未证实项 |

## 数据实验

| ID | 作用/为什么学 | 逻辑前置（必要时回溯） | 权威资料 | 实操任务 | 需要留下的证据 |
|---|---|---|---|---|---|
| `DATA01` | **事件埋点/北极星/漏斗** — 度量真实用户价值而不是请求数 | `PM02` | [S20](https://www.amplitude.com/guides/product-analytics) | 定义 task_started/completed 与转化分母 | 事件字典及合成样本复算 |
| `DATA02` | **Cohort 留存与归因** — 分析用户是否反复获得价值及偏差 | `DATA01` | [S20](https://www.amplitude.com/guides/product-analytics) | 计算按 cohort 留存，解释抽样偏差与数据缺失 | SQL/电子表样例与分母 |
| `DATA03` | **实验设计/A-B/反事实** — 区分相关与因果、守门指标与提前停止风险 | `DATA01`, `PM06` | [S20](https://www.amplitude.com/guides/product-analytics) / [S01](https://www.atlassian.com/agile/product-management/discovery) | 预注册实验假设、样本、指标、守门与停止规则 | 合成分析报告不冒充线上提升 |

## 商业化

| ID | 作用/为什么学 | 逻辑前置（必要时回溯） | 权威资料 | 实操任务 | 需要留下的证据 |
|---|---|---|---|---|---|
| `BIZ01` | **Buyer/采购/价值与定价** — 真正知道谁可以付费、以什么单位付费 | `PM05` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 画买方/用户/审批/采购图，列定价验证途径 | 买方验证计划、未知项与停止条件 |
| `BIZ02` | **单位经济/CAC/LTV/现金流** — 避免以贡献毛利冒充净利润或获客/收入事实 | `BIZ01`, `DATA02` | [S20](https://www.amplitude.com/guides/product-analytics) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 用三档情景计算单成功任务成本、贡献毛利和回本假设 | 带分母和敏感性的情景表 |
| `BIZ03` | **支付/订阅/计费需求设计** — 买方报价到技术账单/退款/对账的边界 | `BIZ01`, `ENG06`, `ENG04` | [S13](https://www.postgresql.org/docs/current/tutorial.html) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 合成支付 webhook 乱序/重复与套餐权限切换 | 对账/幂等/取消/退款需求和负例 |
| `BIZ04` | **渠道/增长/留存商业验证** — 找到可触达渠道而非只看总用户规模 | `BIZ01`, `DATA01` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S20](https://www.amplitude.com/guides/product-analytics) | 设计一项小规模可逆获客假设与转化衡量 | 样本分母、渠道成本及停止条件 |
| `BIZ05` | **产品组合/Go-to-market/客户支持** — 承诺范围、交付、支持和升级路径 | `BIZ01`, `PM11` | [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) / [S01](https://www.atlassian.com/agile/product-management/discovery) | 模拟试点条款、交付/支持边界、成功/失败定义 | 可审查试点计划与非目标 |

## 可信与可用

| ID | 作用/为什么学 | 逻辑前置（必要时回溯） | 权威资料 | 实操任务 | 需要留下的证据 |
|---|---|---|---|---|---|
| `ETH01` | **可访问性/公平性/可信产品** — 识别被忽视的用户群、误导与伤害 | `PM08`, `AI11` | [S09](https://www.w3.org/WAI/WCAG22/quickref/) / [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | 设计对抗/边缘用户与人工接管样本 | 可测试公平性/可用性风险记录 |


## 使用约定

- **图谱的 requires 是概念关系，不是强制排队课程**；会做的前置可跳过，遇到不能解释/不能通过负例再补。
- 每次只选一个主 Gap，不因下游项目“也许未来要用”就把所有框架学完；知识覆盖完整但工作量受控。
- 不能复制上游私仓与受限教材到公开仓；页面/源码存在不代表独立掌握；真实系统测试、隐私和生产责任由对应项目或 Owner 核实。
