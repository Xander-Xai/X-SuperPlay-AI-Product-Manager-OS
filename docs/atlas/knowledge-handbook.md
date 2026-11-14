# 产品经理知识手册：专业定义、通俗类比、先修与实践

> v4.0 · 2026-11-14 · INDEXED / PRACTICE_NOT_RUN。**概念依赖不是强制学习顺序。** 每次只选择实际被需求触发的一个主 Gap，已有前置可跳过。权威与原作者链接不表示代码已经运行或人已经掌握。

[全景 Roadmap](../../ROADMAP.md) · [产品关系图](product-lifecycle-mermaid.md) · [角色和状态术语](../quality/terminology-contract.md) · [覆盖审计矩阵](../quality/coverage-audit-20261114.md) · [上游私仓资料指针](../../resources/upstream-pm-knowledge-index.md)。

## 产品基础、研究、策略与交付（33 项）

| ID | 知识/意义 | 逻辑前置（不代表先学顺序） | 权威/原作者资料 | 最小动手任务 | 可复核证据 |
|---|---|---|---|---|---|
| `PM01` | **角色分工与生命周期**：识别问题-决策-交付-复盘的责任 | 视当前问题 | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S02](https://www.atlassian.com/agile/product-management/requirements) | 画出 PM/PE/设计/研发/销售的责任图并指出灰区 | 一份冲突决策表和验收责任人 |
| `PM02` | **问题定义与 JTBD**：把功能需求翻译成用户待完成任务 | `PM01` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S04](https://pair.withgoogle.com/guidebook-v2/) | 从三条功能请求提炼任务/触发场景/成功行为 | 包含不做条件和失败反例的问题卡 |
| `PM03` | **访谈与行为证据**：获得可以推翻假设的真实/合成事实 | `PM02` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S04](https://pair.withgoogle.com/guidebook-v2/) | 写非诱导访谈脚本并对照行为/陈述 | 事实/推断/假设台账及证据等级 |
| `PM04` | **竞品与替代方案**：人工/旧系统/不用 AI 都是竞争 | `PM02` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 比较人工、规则、搜索、AI 并列反证 | 替代方案矩阵与停止门槛 |
| `PM05` | **价值主张与市场细分**：确认谁痛、频率、可触达性及买方 | `PM03`、`PM04` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 区分用户/买方/采购责任，分场景估算触达 | 一张证据标注的细分/价值卡 |
| `PM06` | **优先级与路线图**：确定先解决哪个风险而非堆功能 | `PM04`、`PM05` | [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 以 RICE 与明确约束各排一次同一需求，说明差异 | Now/Next/Later 决策与资源 Stop Rule |
| `PM07` | **PRD/用户故事/验收**：把模糊目标变可测试行为 | `PM02` | [S02](https://www.atlassian.com/agile/product-management/requirements) | 完成一页 PRD + Given/When/Then 正负场景 | 可供他人不猜测地写测试的需求文档 |
| `PM08` | **信息架构/原型/UI 状态**：从任务流设计空态/失败/等待/恢复 | `PM07` | [S04](https://pair.withgoogle.com/guidebook-v2/) / [S09](https://www.w3.org/WAI/WCAG22/quickref/) | 做两版低保真任务流和错误态原型 | 用户可观察任务结果与无障碍检查表 |
| `PM09` | **AI 信任与可控 UX**：解释来源、错误、能力边界与人工控制 | `PM08`、`AI01` | [S04](https://pair.withgoogle.com/guidebook-v2/) / [S22](https://pair.withgoogle.com/guidebook-v2/chapters) | 设计引用/拒答/反馈/人工接管的三条流程 | 失败提示及真实/合成可用性测试记录 |
| `PM10` | **交付协作/范围与变更**：定义变更责任、发布门禁与冲突处理 | `PM07` | [S02](https://www.atlassian.com/agile/product-management/requirements) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 模拟需求变更影响排期、权限、成本并作 ADR | 变更前后 UAT 与审批记录 |
| `PM11` | **客户成功/支持运营**：将故障/投诉转成可重现事实与服务闭环 | `PM09`、`OPS02` | [S04](https://pair.withgoogle.com/guidebook-v2/) / [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 构建合成支持工单分级/升级/闭环规则 | 优先级、响应预案、重复故障分析 |
| `PM12` | **产品策略与 Portfolio 决策**：判断多个产品/渠道哪个该停 | `PM06`、`BIZ01` | [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) / [S01](https://www.atlassian.com/agile/product-management/discovery) | 三候选预算减半时选唯一试验并解释淘汰项 | 资源配置和机会成本记录 |
| `PM13` | **机会解决方案树 OST**：Opportunity Solution Tree 用可衡量成果 Outcome 组织用户机会、候选方案和待验证假设之间的因果关系。 | `PM02`、`PM03`、`PM06` | [S27](https://www.producttalk.org/glossary-discovery-product-discovery/) / [S28](https://www.producttalk.org/getting-started-with-discovery/) / [S37](https://www.atlassian.com/agile/product-management/discovery)（同 S01） | 画一棵 1 结果→3 机会→各2方案→关键假设的树，并提出反证 | 可追溯 Outcome/Opportunity/Solution/Assumption，三种不是同一层 |
| `PM14` | **研究方法选型与三角验证**：按探索/评估目标，组合定性行为研究、可用性研究和定量实验，并识别抽样与观察偏差。 | `PM03` | [S29](https://www.nngroup.com/articles/which-ux-research-methods/) / [S38](https://www.nngroup.com/articles/ux-research-cheat-sheet/) | 同一合成现象提出访谈、观察、日志分析各能/不能回答的问题 | 方法决策表、证据缺口和至少一项相反解释 |
| `PM15` | **OKR/Outcome/北极星对齐**：OKR 将目标与关键结果建立可观察的对齐关系；北极星表达长期核心用户价值，关键结果不应等同任务清单。 | `PM06`、`DATA01` | [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 把十条功能需求转换成目标、结果与可证伪指标 | 结果指标、领先输入和守门指标齐全，不以工作量充成果 |
| `PM16` | **Stakeholder 利益相关者与决策权**：Stakeholder 管理识别使用者、买方、技术、设计、法务、运营、审批者的目标与决策权，建立可沟通的责任分工。 | `PM07` | [S32](https://scrumguides.org/scrum-guide.html?lang=en) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 绘制 6 角色影响-兴趣矩阵与可升级的责任表 | 决策/执行/咨询/知会与冲突升级说明 |
| `PM17` | **产品交付与项目控制**：产品交付管理通过范围、依赖、风险、验收、沟通和发布计划将持续发现转为可靠增量。 | `PM10` | [S32](https://scrumguides.org/scrum-guide.html?lang=en) / [S33](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) / [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) | 为模拟 2 周 Release 列 WBS/依赖/风险、UAT 与风险预警 | 明确范围、风险责任、变更处理和实际复盘 |
| `PM18` | **Product Operating Model / 产品组织运作**：产品运营模式规定产品目标、团队授权、决策权、发现-交付流程与反馈治理的协作系统。 | `PM16`、`PM06` | [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 绘制产品三人组或单人多角色职责、决策与审查节奏 | 发现与交付双向信息流和决策责任表 |
| `PM19` | **市场定位和竞争差异化**：定位通过目标细分、竞争参照和价值差异解释为何特定用户应选择此产品。 | `PM05`、`PM04` | [S31](https://www.strategyzer.com/library/the-value-proposition-canvas) / [S25](https://www.svpg.com/product-management-an-introduction/) | 选择 2 类买方，做替代方案/差异对比与反证 | 一句可验证定位 + 数据/访问证据分层 |
| `PM20` | **用户旅程/服务蓝图**：Customer Journey Map 描述跨触点用户体验，Service Blueprint 同时揭示前台和后台流程/交接。 | `PM08`、`PM03` | [S29](https://www.nngroup.com/articles/which-ux-research-methods/) / [S40](https://pair.withgoogle.com/guidebook-v2/chapters)（同 S22） | 绘制前台动作、后台 API/人员、跨触点失败与恢复 | 服务蓝图、可观察触点和错误恢复用例 |
| `PM21` | **平台型产品/API 产品思维**：平台产品把内部能力以 API/组件/权限及 SLA 形式交给其他团队或第三方消费，需同时关注开发者体验和兼容成本。 | `ENG03`、`PM07` | [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 写 API 消费者故事、版本契约、配额、失败响应与支持范围 | 兼容变更、租户隔离与文档演练 |
| `PM22` | **Pre-mortem 预演失败和产品风险矩阵**：Premortem 在投入前假设项目已失败，逆向列举原因、概率/影响、应对、可检测信号和责任。 | `PM06`、`PM07` | [S25](https://www.svpg.com/product-management-an-introduction/) / [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) | 模拟产品上线失败，列 8 个失败假设并按四大风险分类 | 风险登记、观测信号、Stop/降级门槛 |
| `PM23` | **产品生命周期/停用与迁移**：Product Lifecycle Management 关注验证、增长、成熟、衰退或停用阶段的产品投资、用户迁移与支持义务。 | `PM12`、`PM11` | [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) / [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) | 制定产品停用公告、数据导出/删除、用户迁移、合同边界 | 停用清单与用户影响/回滚方案 |
| `PM24` | **市场规模 TAM/SAM/SOM 与机会测算**：TAM 为理论总可触达需求上限，SAM 为约束产品能力/地域下的可服务市场，SOM 为考虑渠道与竞争后一定时间可获得的部分；应把规模与频率、价格、证据和假设分开。 | `PM05`、`PM19` | [S57](https://www.strategyzer.com/library/your-business-model-environment) / [S30](https://www.strategyzer.com/library/the-business-model-canvas) | 用公开人口/行业资料和三个明确假设估计范围，并做假设敏感性 | 注明来源、单位、年份、区间、反证，不把市场总量当订单 |
| `PM25` | **问卷设计/抽样/定量需求研究**：Survey 是受访者自我报告的态度或行为；样本框、招募/无响应偏差、措辞诱导和分母决定能否外推。 | `PM14` | [S55](https://www.nngroup.com/articles/research-methods-glossary/) / [S29](https://www.nngroup.com/articles/which-ux-research-methods/) | 设计 8 题问卷并列出诱导/双重问题/抽样局限；分析合成应答 | 目标总体、分母、抽样偏差、至少两个反例和不可外推范围 |
| `PM26` | **用户研究知情同意/数据治理**：研究参与者应知情自愿，理解数据采集、使用、留存、共享与退出边界；研究数据与真实产品事件可能有不同授权要求。 | `PM03` | [S43](https://www.nngroup.com/articles/informed-consent/) / [S44](https://www.nngroup.com/articles/research-ops-study-guide/) | 起草研究同意与撤回流程，用合成数据模拟权限变化/删除 | 同意说明、最小化、删除/保留限制与责任人，不保存私人资料在公开仓 |
| `PM27` | **MVP/POC/原型与假设实验**：Prototype 用于探索交互，POC 验证技术可行性，MVP 用最小有意义产品/服务检验关键价值假设，Pilot 是受控试点，Production 是真实运营环境；这些不是同义词。 | `PM13`、`PM22` | [S46](https://www.strategyzer.com/library/experiment-library) / [S42](https://www.producttalk.org/opportunity-solution-trees/) / [S41](https://www.svpg.com/four-big-risks/) | 为一个产品风险比较访谈/纸面原型/手工服务/POC/MVP，选择最便宜有效验证 | 每种方法的问题、成功/失败、停止阈值及证据强度 |
| `PM28` | **Scrum Product Owner/Product Goal/Backlog**：在 Scrum 框架中 Product Owner 对最大化产品价值与有效管理 Product Backlog 负责，包括 Product Goal 与条目排序；PM 职位不必然等于 PO。 | `PM16`、`PM06` | [S47](https://scrumguides.org/scrum-guide.html?lang=en) / [S49](https://www.atlassian.com/agile/scrum/backlogs/) | 拆一条 Product Goal 与 5 条 Backlog，演示 PO 如何排序与拒绝 | Product Goal、Backlog、责任边界，标明 Scrum 与其他组织模式不同 |
| `PM29` | **验收标准 AC/DoD/DoR 的边界**：Acceptance Criteria 约束单条需求的验收行为；Definition of Done 是 Increment 的完成质量共同标准；Definition of Ready 常用但不是官方 Scrum 2020 强制工件。 | `PM28`、`PM07` | [S47](https://scrumguides.org/scrum-guide.html?lang=en) / [S48](https://www.atlassian.com/agile/project-management/definition-of-done) | 为 3 条需求写 AC，提一个全团队 DoD，并设计错误/安全反例 | 区分范围，不用 AC 冒充上线安全门禁，DoR 标可选实践 |
| `PM30` | **客户之声 VoC/反馈归因与需求合并**：Voice of Customer 需要将售后、访谈、使用日志、投诉按事件去重并标来源与频次；反馈不是未经研究就能直接转换的功能任务。 | `PM03`、`PM11` | [S44](https://www.nngroup.com/articles/research-ops-study-guide/) / [S29](https://www.nngroup.com/articles/which-ux-research-methods/) | 合并合成客服/评论/日志，形成问题-证据-假设-行为方案 | 来源、主题聚类、反例、优先级决定与用户通知闭环 |
| `PM31` | **产品叙事/决策汇报/跨职能沟通**：产品沟通将问题、证据、取舍、风险、备选与结果翻译成可供不同职能作决定的叙事，而不以漂亮 PPT 取代证据。 | `PM15`、`PM16` | [S25](https://www.svpg.com/product-management-an-introduction/) / [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) | 同一决策写领导一页纸与研发 ADR 两种版本，并答反方疑问 | 受众目标、事实/假设、备选、明确决策与反证 |
| `PM32` | **可用性测试任务与观察/迭代**：Usability Testing 请代表性参与者做代表性任务，观察成功、错误、时长和困难；评价 UI 可用性不同于询问是否喜欢产品。 | `PM08`、`PM14` | [S45](https://www.nngroup.com/articles/qual-usability-testing-study-guide/) / [S29](https://www.nngroup.com/articles/which-ux-research-methods/) | 为原型设计 3 个不诱导的任务，做合成演示并计划真实授权用户测试 | 任务脚本/成功定义/观察与误用，不把模拟评估当真实可用性 |
| `PM33` | **产品发布沟通/帮助文档/教育**：产品发布需要版本说明、已知限制、支持路径、用户教育、内部销售/客服培训和反馈渠道，与仅完成 CI/CD 不同。 | `PM17`、`BIZ10` | [S50](https://www.atlassian.com/agile/product-management/product-launch) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 写发行说明、FAQ、用户引导、内部培训和故障回退通知 | 可理解文档、支持责任、重大错误公告与可恢复路径 |

## AI 专业技术与安全（15 项）

| ID | 知识/意义 | 逻辑前置（不代表先学顺序） | 权威/原作者资料 | 最小动手任务 | 可复核证据 |
|---|---|---|---|---|---|
| `AI01` | **LLM 基础与上下文/Token**：理解生成不确定性、输入预算和限制 | `PM02` | [S19](https://developers.google.com/machine-learning/crash-course) / [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | 同题短/长上下文比较结构化输出与 Token/成本 | 输入-输出-成本与失败报告 |
| `AI02` | **Prompt/结构化输出**：实现可校验输出而非靠自然语言猜测 | `AI01` | [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) / [S19](https://developers.google.com/machine-learning/crash-course) | 为合成分类任务比较规则/Prompt + JSON schema 校验 | 字段校验通过率和坏例日志 |
| `AI03` | **Embedding/检索与 RAG**：区分索引、召回、排序、生成和证据 | `AI01`、`ENG04` | [S19](https://developers.google.com/machine-learning/crash-course) / [S17](https://docs.langchain.com/oss/python/learn) | 在公开小语料比较 BM25/向量/混检并分层评测 | 检索金标、引用支持、拒答与版本失败 |
| `AI04` | **RAG 数据治理/文档生命周期**：处理来源许可、权限、更新、删除与版本 | `AI03`、`ENG06` | [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S17](https://docs.langchain.com/oss/python/learn) | 模拟文档撤销权限、版本更新、删除后不可检索 | 越权/旧版/删除负例 |
| `AI05` | **工具调用/Workflow/单 Agent**：知道什么时候让模型决策、什么时候固定流程 | `AI02`、`ENG03` | [S06](https://www.anthropic.com/engineering/building-effective-agents) / [S17](https://docs.langchain.com/oss/python/learn) | Mock 工单比较规则链与工具 Agent 的正确率/成本 | 审批前无写入、超时与错误恢复 |
| `AI06` | **MCP/工具权限与副作用**：工具连接不代表可以越权执行 | `AI05`、`ENG06` | [S18](https://blog.modelcontextprotocol.io/posts/2026-07-28/) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) / [S56](https://owasp.org/projects/top-10-for-large-language-model-applications) | 在隔离工具沙箱检查 schema、租户权限、审批、审计 | 未授权拒绝、无副作用、版本兼容性记录 |
| `AI07` | **Context Engineering/Memory**：在正确时机给模型正确的上下文与工具 | `AI01`、`AI05` | [S17](https://docs.langchain.com/oss/python/learn) / [S06](https://www.anthropic.com/engineering/building-effective-agents) | 对比上下文裁剪、版本过滤、checkpoint 恢复 | 同测试集效果/Token/恢复负例 |
| `AI08` | **Harness/Agent 执行治理**：任务边界、预算、重试、停止、人工介入与恢复 | `AI05`、`AI07`、`OPS02` | [S06](https://www.anthropic.com/engineering/building-effective-agents) / [S17](https://docs.langchain.com/oss/python/learn) / [S56](https://owasp.org/projects/top-10-for-large-language-model-applications) | 强制工具失败/循环上限/断点重启，证明 fail-closed | 可重复 Trace、停止与恢复断言 |
| `AI09` | **多 Agent 编排与人机协作**：只有单 Agent 证据不足才增加角色协作 | `AI08` | [S06](https://www.anthropic.com/engineering/building-effective-agents) / [S17](https://docs.langchain.com/oss/python/learn) | 比较单/多 Agent 的成功率与维护成本，回放交接失败 | 消融报告与责任边界 |
| `AI10` | **多模态/OCR/语音/图片**：处理上游识别错误与人工纠错 | `AI01` | [S19](https://developers.google.com/machine-learning/crash-course) / [S04](https://pair.withgoogle.com/guidebook-v2/) | 用公开/合成样本比较 OCR 错误如何影响最终任务 | 端到端分母与人工纠错数据 |
| `AI11` | **AI Eval/金标/回归**：把效果变成可复算的质量门禁 | `AI01`、`PM07` | [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) / [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | 建立正常/边界/对抗/拒答集并审计 LLM judge 偏差 | 金标版本/分母/标注与回归报告 |
| `AI12` | **AI 安全/Prompt Injection/模型治理**：隔离不可信上下文与高风险工具 | `AI05`、`AI11`、`ENG06` | [S56](https://owasp.org/projects/top-10-for-large-language-model-applications) / [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 设计注入/越权/数据外泄/过度代理负例 | 无未授权副作用的安全测试证据 |
| `AI13` | **模型选型/推理与成本**：按质量、时延、成本、隐私与可迁移性选模型 | `AI01`、`AI11` | [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) / [S19](https://developers.google.com/machine-learning/crash-course) | 相同金标对比两方案端到端成功任务成本/P95 | 选型 ADR 和不确定性 |
| `AI14` | **微调/后训练选型判断**：知道何时 RAG/Prompt 不够、是否值得训练 | `AI11`、`AI13` | [S19](https://developers.google.com/machine-learning/crash-course) / [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | 对错误类型分类，比较不训练/微调的投入与效益 | 门槛与数据许可/离线评测方案 |
| `AI15` | **生产 AI 质量漂移与人工复核运营**：上线后 AI 质量随模型/检索数据/用户输入/工具环境变化而漂移，需要带版本的采样审计、用户纠错、权限/成本守门和回滚。 | `AI11`、`OPS02`、`OPS05` | [S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) / [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S56](https://owasp.org/projects/top-10-for-large-language-model-applications) | 设计金标回归与线上匿名采样计划，模拟来源变更或 Prompt 更新的退化 | 质量/安全/成本监控、人工审查、回滚阈值，避免泄露用户内容 |

## 工程交付（14 项）

| ID | 知识/意义 | 逻辑前置（不代表先学顺序） | 权威/原作者资料 | 最小动手任务 | 可复核证据 |
|---|---|---|---|---|---|
| `ENG01` | **Web/HTTP/DNS/TLS**：理解浏览器→代理→服务的请求路径 | `PM07` | [S10](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 画从浏览器到后端请求链并定位 401/502/超时 | 请求/响应抓包与原因分析 |
| `ENG02` | **前端组件/状态/TypeScript**：保证数据展示、交互与错误状态一致 | `ENG01`、`PM08` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S21](https://nextjs.org/docs/app/getting-started/deploying) | 搭建可交互表单，注入失败/重复点击/刷新 | 前端状态测试和构建日志 |
| `ENG03` | **API 契约与输入验证**：设计清晰请求/响应和错误边界 | `ENG01`、`PM07` | [S10](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [S11](https://fastapi.tiangolo.com/tutorial/security/) | 写三接口 schema，覆盖非法输入、错误与幂等键 | OpenAPI/集成测试与日志 |
| `ENG04` | **SQL/事务/迁移**：持久化数据并在失败时保持一致 | `ENG03` | [S13](https://www.postgresql.org/docs/current/tutorial.html) | 模拟事务失败、回滚、唯一索引与迁移降级 | 事务与迁移回滚测试 |
| `ENG05` | **数据模型/对象存储/缓存**：区分结构化数据、文件、缓存的一致性责任 | `ENG04` | [S13](https://www.postgresql.org/docs/current/tutorial.html) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 用合成文档测数据版本与缓存失效 | TTL/删除/备份策略和过期负例 |
| `ENG06` | **AuthN/AuthZ/多租户隔离**：身份验证不等于授权；每个数据读写检查权限 | `ENG03`、`ENG04` | [S11](https://fastapi.tiangolo.com/tutorial/security/) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 用户 A 与 B 交叉读写、伪造角色与过期令牌 | 横向越权测试和审计 |
| `ENG07` | **异步任务/队列/SSE/状态**：处理长任务、重试、状态转移与前端反馈 | `ENG03`、`ENG04` | [S10](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [S17](https://docs.langchain.com/oss/python/learn) | Mock 长任务重复执行/中断/重新连接 | 幂等+状态恢复+前端错误态测试 |
| `ENG08` | **分布式可靠性与故障恢复**：掌握超时/重试/限流/熔断/幂等/退避 | `ENG07` | [S12](https://fastapi.tiangolo.com/deployment/concepts/) / [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 模拟 429/500、网络断开、死信与重复消息 | 可控故障注入与恢复证据 |
| `ENG09` | **测试金字塔与契约测试**：用单元/集成/E2E/安全负例锁定行为 | `ENG03`、`PM07` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 为主流程加两条失败场景和一条 E2E | 测试命令、版本与失败报告 |
| `ENG10` | **Web 安全/输入/依赖供应链**：覆盖常见 Web 攻击、依赖风险与敏感配置 | `ENG06`、`ENG09` | [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) / [S23](https://owasp.org/projects/top-ten) | 执行授权/注入/泄密测试与依赖清单审查 | 无硬失败的安全负例 |
| `ENG11` | **容器/环境与配置管理**：在新环境稳定启动并区分配置与密钥 | `ENG03`、`ENG04` | [S12](https://fastapi.tiangolo.com/deployment/concepts/) / [S15](https://docs.docker.com/compose/how-tos/production/) | 干净环境 Docker Compose 启动/重启并拒绝缺密钥 | 复现、健康检查、重启与日志 |
| `ENG12` | **部署拓扑与架构演化**：选单体、模块化和服务拆分的迁移边界 | `ENG11`、`PM06` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S21](https://nextjs.org/docs/app/getting-started/deploying) | 用 ADR 比较 Next.js 全栈、FastAPI、BFF、拆服务成本 | 部署图、数据边界与可逆迁移演练 |
| `ENG13` | **前端 SEO/性能/可访问性**：确保公开站点可被发现、可访问、可用 | `ENG02` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S09](https://www.w3.org/WAI/WCAG22/quickref/) | 测关键路径的性能/语义/键盘操作和错误状态 | Lighthouse/人工辅助验收记录（按任务定阈） |
| `ENG14` | **API 文档/版本化/兼容性**：防止前后端与外部集成被破坏 | `ENG03`、`ENG09` | [S10](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [S12](https://fastapi.tiangolo.com/deployment/concepts/) | 旧客户端回放，新版本新增字段/删除字段对照 | 兼容性案例与变更计划 |

## 生产运维（6 项）

| ID | 知识/意义 | 逻辑前置（不代表先学顺序） | 权威/原作者资料 | 最小动手任务 | 可复核证据 |
|---|---|---|---|---|---|
| `OPS01` | **CI/CD/Release/回滚**：保障从提交到发布的证据链 | `ENG09`、`ENG11` | [S14](https://nextjs.org/docs/app/guides/production-checklist) / [S15](https://docs.docker.com/compose/how-tos/production/) | 在测试环境跑构建/测试/迁移检查/回滚演练 | CI run、固定 SHA、部署与回滚记录 |
| `OPS02` | **日志/Trace/指标/SLI-SLO**：从症状定位检索/模型/工具/数据库瓶颈 | `ENG03` | [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 为请求串联 trace_id, 隐去 PII 并模拟超时定位 | Trace、告警与用户视角 SLI |
| `OPS03` | **容量/压测/成本上限**：识别瓶颈与安全容量，不只看单次延迟 | `OPS02`、`ENG08` | [S12](https://fastapi.tiangolo.com/deployment/concepts/) / [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 合成压测并记录 P95/错误率/调用成本 | 负载曲线和容量保护决策 |
| `OPS04` | **备份/恢复/事故响应**：恢复数据与服务且留下审计复盘 | `ENG04`、`OPS01` | [S12](https://fastapi.tiangolo.com/deployment/concepts/) / [S15](https://docs.docker.com/compose/how-tos/production/) | 测试备份恢复、机密泄露撤销/密钥轮换预案 | 恢复演练日志与 RPO/RTO 假设 |
| `OPS05` | **数据隐私/合规/删除与审计**：权利、使用许可、最小化与数据生命周期 | `ENG06`、`AI12` | [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 模拟撤回授权/删除数据与日志保留冲突 | 授权矩阵、删除演练与审计边界 |
| `OPS06` | **真实用户 UAT/发布与维护门禁**：可运行不等于经用户验证/可长期运营 | `OPS01`、`OPS02`、`PM09`、`AI11` | [S04](https://pair.withgoogle.com/guidebook-v2/) / [S16](https://opentelemetry.io/docs/concepts/observability-primer/) | 执行干净环境 UAT+故障注入，列责任/回滚/值班 | 发布包，明确证据和未证实项 |

## 产品数据与实验（7 项）

| ID | 知识/意义 | 逻辑前置（不代表先学顺序） | 权威/原作者资料 | 最小动手任务 | 可复核证据 |
|---|---|---|---|---|---|
| `DATA01` | **事件埋点/北极星/漏斗**：度量真实用户价值而不是请求数 | `PM02` | [S20](https://www.amplitude.com/guides/product-analytics) | 定义 task_started/completed 与转化分母 | 事件字典及合成样本复算 |
| `DATA02` | **Cohort 留存与归因**：分析用户是否反复获得价值及偏差 | `DATA01` | [S20](https://www.amplitude.com/guides/product-analytics) | 计算按 cohort 留存，解释抽样偏差与数据缺失 | SQL/电子表样例与分母 |
| `DATA03` | **实验设计/A-B/反事实**：区分相关与因果、守门指标与提前停止风险 | `DATA01`、`PM06` | [S20](https://www.amplitude.com/guides/product-analytics) / [S01](https://www.atlassian.com/agile/product-management/discovery) | 预注册实验假设、样本、指标、守门与停止规则 | 合成分析报告不冒充线上提升 |
| `DATA04` | **增长飞轮/渠道/留存生命周期**：Growth Loop 将每次成功的用户体验、分发、获取与再参与形成反馈链，且需有真实转化与持续价值证据。 | `DATA02`、`BIZ04` | [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) / [S37](https://www.atlassian.com/agile/product-management/discovery)（同 S01） | 画一个渠道→激活→成功→推荐→新客户的闭环并找断点 | 事件/时间窗/分母、自然回访与人工推动分开 |
| `DATA05` | **激活/新手引导/首次价值**：Activation 应定义用户首次完成价值事件，而不是仅注册；Onboarding 降低从进入产品到获得价值的阻力。 | `DATA01`、`PM20` | [S51](https://www.amplitude.com/blog/getting-started-activation) / [S20](https://www.amplitude.com/guides/product-analytics) | 用合成事件拆注册→首任务→有效完成漏斗并设计两种引导 | 分母/时间窗/合格用户/真实成功定义，无法验证标假设 |
| `DATA06` | **实验统计基础/置信区间/SRM**：随机实验需预定义随机化单位、样本量、主要指标和停止规则；SRM、重复查看、多重比较、非独立样本等可能导致假阳性。 | `DATA03` | [S53](https://docs.statsig.com/experiments/monitoring/srm) / [S54](https://statsig.com/blog/product-experimentation-best-practices) | 合成试验设置预定样本/分组，注入 SRM、提前停止，说明该放弃哪些结论 | 随机化/口径/健康检查/局限，不能把 p 值当效果大小 |
| `DATA07` | **事件埋点规划/数据字典/身份去重**：Event Taxonomy 定义行为事件、属性、版本、身份映射和采集时机，防止漏采/双算/隐私越界；数据质量决定分析可靠性。 | `DATA01`、`ENG03` | [S52](https://amplitude.com/docs/data/data-planning-playbook) / [S20](https://www.amplitude.com/guides/product-analytics) | 写 8 个事件的字段/类型/去重/权限，并测试重复发送与匿名转登录 | 事件字典、兼容与变更审查、分母/时间窗可复算 |

## 商业与增长（14 项）

| ID | 知识/意义 | 逻辑前置（不代表先学顺序） | 权威/原作者资料 | 最小动手任务 | 可复核证据 |
|---|---|---|---|---|---|
| `BIZ01` | **Buyer/采购/价值与定价**：真正知道谁可以付费、以什么单位付费 | `PM05` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 画买方/用户/审批/采购图，列定价验证途径 | 买方验证计划、未知项与停止条件 |
| `BIZ02` | **单位经济/CAC/LTV/现金流**：避免以贡献毛利冒充净利润或获客/收入事实 | `BIZ01`、`DATA02` | [S20](https://www.amplitude.com/guides/product-analytics) / [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) | 用三档情景计算单成功任务成本、贡献毛利和回本假设 | 带分母和敏感性的情景表 |
| `BIZ03` | **支付/订阅/计费需求设计**：买方报价到技术账单/退款/对账的边界 | `BIZ01`、`ENG06`、`ENG04` | [S13](https://www.postgresql.org/docs/current/tutorial.html) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 合成支付 webhook 乱序/重复与套餐权限切换 | 对账/幂等/取消/退款需求和负例 |
| `BIZ04` | **渠道/增长/留存商业验证**：找到可触达渠道而非只看总用户规模 | `BIZ01`、`DATA01` | [S01](https://www.atlassian.com/agile/product-management/discovery) / [S20](https://www.amplitude.com/guides/product-analytics) | 设计一项小规模可逆获客假设与转化衡量 | 样本分母、渠道成本及停止条件 |
| `BIZ05` | **产品组合/Go-to-market/客户支持**：承诺范围、交付、支持和升级路径 | `BIZ01`、`PM11` | [S03](https://www.atlassian.com/agile/product-management/product-roadmaps) / [S01](https://www.atlassian.com/agile/product-management/discovery) | 模拟试点条款、交付/支持边界、成功/失败定义 | 可审查试点计划与非目标 |
| `BIZ06` | **ICP 与销售线索验证**：Ideal Customer Profile 表达有相似购买条件的客户类型，销售线索需要区分关注、询问、试点、成交与付费证据。 | `BIZ01`、`PM03` | [S31](https://www.strategyzer.com/library/the-value-proposition-canvas) / [S30](https://www.strategyzer.com/library/the-business-model-canvas) | 设计 2 类 ICP 和从接触到签约的漏斗口径 | 线索来源/授权/阶段/分母，未付费不冒充订单 |
| `BIZ07` | **B2B 采购/谈判/合同交付边界**：企业采购涉及使用方/决策方/采购/法务/财务的多方流程、试点要求、验收/合同风险与总拥有成本。 | `BIZ06`、`PM16` | [S33](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 模拟采购角色链、POC 目标、里程碑验收与变更争议 | 无敏感信息的 RACI、验收和升级流程 |
| `BIZ08` | **商业模式画布 BMC/价值主张 VPC**：Business Model Canvas 用九要素描述如何创造、交付、获取价值；Value Proposition Canvas 对齐 Customer Jobs/Pains/Gains 与产品价值。 | `PM05`、`BIZ01` | [S30](https://www.strategyzer.com/library/the-business-model-canvas) / [S31](https://www.strategyzer.com/library/the-value-proposition-canvas) | 用两个不同客户群画出 BMC/VPC 并标核心未知 | 假设矩阵和可推翻商业模式的试验 |
| `BIZ09` | **经营财务/现金流/预算预测**：现金流是现金实际进出的时间分布，区别于利润和贡献毛利；预算和现金缓冲约束产品投资节奏。 | `BIZ02` | [S30](https://www.strategyzer.com/library/the-business-model-canvas) / [S33](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) | 用合成账单按月模拟回款延迟、退款与服务器成本翻倍 | 现金流表、情景敏感性、停止预算门槛 |
| `BIZ10` | **GTM 上市/渠道与营销销售协同**：Go-to-Market 协同定位、定价、渠道、营销、销售、客户成功与上市指标，需区分获客与任务价值。 | `BIZ06`、`BIZ04` | [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) / [S37](https://www.atlassian.com/agile/product-management/discovery)（同 S01） | 设计一个低成本 GTM 假设：渠道→激活→试用→保留 | 渠道漏斗指标与真实/合成证据分层 |
| `BIZ11` | **定价研究与收费实验**：定价策略区分计价单位、价值捕获、支付意愿证据、价格实验、合同限制及边际成本。 | `BIZ01`、`DATA03` | [S30](https://www.strategyzer.com/library/the-business-model-canvas) / [S31](https://www.strategyzer.com/library/the-value-proposition-canvas) | 比较席位/按任务/订阅套餐，制定可逆的价格验证协议 | 价格假设来源、退款/毛利与真实付费分离 |
| `BIZ12` | **SaaS 订阅产品规则/生命周期**：订阅产品管理涉及配额、升级降级、试用、账单周期、续费、取消、退款、权限与数据留存协同。 | `BIZ03`、`BIZ09` | [S30](https://www.strategyzer.com/library/the-business-model-canvas) / [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) | 一份含重复 webhook/配额/取消/退款的产品规则与测试 | 规则状态机、权责边界和未授权操作拒绝 |
| `BIZ13` | **产品市场契合 PMF 的证据与反证**：PMF 是持续可观察的市场需求、采用、留存及经济性支持产品价值的判断，不由某个单一百分比、问卷、爆款或一次付费自动证明。 | `BIZ06`、`DATA02`、`PM05` | [S41](https://www.svpg.com/four-big-risks/) / [S31](https://www.strategyzer.com/library/the-value-proposition-canvas) | 对两个产品构建留存、买方、替代成本和风险证据清单并列反证 | 按细分/时间窗/真实重复行为，明确尚未知证据 |
| `BIZ14` | **B2B ROI/价值量化与总拥有成本**：ROI 假设需要对照当前替代方案，含实施/集成/培训/迁移/安全支持成本和可验证收益；客户 ROI 不等于供应商收入。 | `BIZ07`、`BIZ02` | [S30](https://www.strategyzer.com/library/the-business-model-canvas) / [S57](https://www.strategyzer.com/library/your-business-model-environment) | 按三档假设计算客户现状/AI 方案的 TCO、风险与价值，明确保守假设 | 客户侧/卖方侧成本分开、收益来源和敏感性 |

## 组织与协作（6 项）

| ID | 知识/意义 | 逻辑前置（不代表先学顺序） | 权威/原作者资料 | 最小动手任务 | 可复核证据 |
|---|---|---|---|---|---|
| `MGT01` | **战略与资源配置管理**：战略管理是在资源约束下选择竞争方向、投资重点、机会成本和阶段目标，持续拒绝低价值事项。 | `PM06`、`BIZ08` | [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 预算减半下重排 3 条路线，写出不做理由 | 决策来源、成本、反证、复核日期 |
| `MGT02` | **项目与风险管理**：项目管理围绕具体目标的范围、进度、成本、质量、风险、依赖和干系人协调，不等于产品发现。 | `PM17` | [S33](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) / [S32](https://scrumguides.org/scrum-guide.html?lang=en) | 列 RACI/风险登记/里程碑/验收及变更示例 | 范围变更与风险响应演练 |
| `MGT03` | **组织协作/角色与委派**：跨职能协作使用明确决策权、授权、激励、反馈和升级机制，人员管理只有真实团队触发时深入。 | `PM16`、`MGT02` | [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 模拟冲突：设计、技术、销售在上线前争议权衡 | 职责矩阵、升级条件和沟通脚本 |
| `MGT04` | **流程治理/标准化与风险**：Product Ops/流程治理建立重复可靠的决策日志、发布审批、变更、异常与风险响应制度。 | `PM10`、`ENG10` | [S36](https://www.atlassian.com/agile/product-management/product-operating-model) / [S33](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) | 从一次合成事故写 SOP、监控信号、回滚/审批 | 根因、控制点、责任与复测规则 |
| `MGT05` | **管理决策复盘与人机共练**：Decision Review 通过记录当时证据、备选、概率、停止阈值和事后结果进行校准，避免事后诸葛亮。 | `MGT01`、`COG01` | [S25](https://www.svpg.com/product-management-an-introduction/) / [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) | 写一份决策日志，用 AI 反方质疑后关闭 AI 做新案例 | 原始预测、到期核验、人审与反证 |
| `MGT06` | **产品运营 Product Ops 与变更采用**：Product Operations 聚焦产品团队研究、数据、流程和跨部门协作机制；变更采用包括用户/内部支持和反馈，不能等同监控服务器。 | `PM18`、`PM33` | [S26](https://www.svpg.com/the-product-operating-model-an-introduction/) / [S50](https://www.atlassian.com/agile/product-management/product-launch) | 模拟跨部门发布，做沟通/培训/知识库维护/决策日志 | 采用率/反馈/职责，区分 Product Ops 与 DevOps |

## 因果与认知（3 项）

| ID | 知识/意义 | 逻辑前置（不代表先学顺序） | 权威/原作者资料 | 最小动手任务 | 可复核证据 |
|---|---|---|---|---|---|
| `COG01` | **证据等级/预测校准**：Evidence Calibration 将可观察事实、推断、猜测及预测概率分离，用结果反馈改进决策可靠性。 | `PM03` | [S27](https://www.producttalk.org/glossary-discovery-product-discovery/) / [S25](https://www.svpg.com/product-management-an-introduction/) | 对 10 个可判定判断写概率、来源和截止日 | 预测与结果分离、校准复盘与未知标记 |
| `COG02` | **系统思维/因果与反馈环**：Systems Thinking 把变量、延迟、约束和反馈循环放入因果假设图，区分相关与因果。 | `DATA03`、`PM06` | [S27](https://www.producttalk.org/glossary-discovery-product-discovery/) / [S34](https://www.atlassian.com/agile/product-management/new-product-development-process) | 画获客→成本→服务→满意→留存的因果与反作用图 | 至少两个替代解释和干预/观察计划 |
| `COG03` | **认知偏差/反事实与决策质量**：Cognitive Bias 管理关注确认偏误、幸存者偏差、沉没成本与可得性等如何扭曲研究与产品选择。 | `COG01` | [S25](https://www.svpg.com/product-management-an-introduction/) / [S29](https://www.nngroup.com/articles/which-ux-research-methods/) | 给案例找三种反证、陌生人群/成本情景 | 明确偏差、反事实和可改变结论的证据 |

## 治理与信任（4 项）

| ID | 知识/意义 | 逻辑前置（不代表先学顺序） | 权威/原作者资料 | 最小动手任务 | 可复核证据 |
|---|---|---|---|---|---|
| `ETH01` | **可访问性/公平性/可信产品**：识别被忽视的用户群、误导与伤害 | `PM08`、`AI11` | [S09](https://www.w3.org/WAI/WCAG22/quickref/) / [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | 设计对抗/边缘用户与人工接管样本 | 可测试公平性/可用性风险记录 |
| `GO01` | **行业知识/采购/政策约束**：行业产品管理需要理解领域工作流、购买流程、监管边界和机构激励，不能把通用互联网增长经验机械照搬。 | `PM05`、`BIZ07` | [S33](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) / [S36](https://www.atlassian.com/agile/product-management/product-operating-model) | 针对指定行业列使用者/采购者/数据许可/验收规则 | 可溯源规则与专家复核需求，未知不猜 |
| `GO02` | **合同/知识产权/AI 数据治理责任**：上市和商业交付需要对数据许可、IP、保留/删除、合同交付、审计与责任划分进行风险核查。 | `OPS05`、`MGT04` | [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S08](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 建立数据流、保留/删除、来源许可、第三方责任与升级审查 | 拒绝无权数据使用、人工专业审查、审计链 |
| `GO03` | **多语言/本地化/包容性产品**：Internationalization 与 Localization 涉及文本、日期/数字/币种、文化约束、无障碍及用户研究差异；多语言翻译不等于产品适用当地法律与任务。 | `PM08`、`ETH01` | [S09](https://www.w3.org/WAI/WCAG22/quickref/) / [S29](https://www.nngroup.com/articles/which-ux-research-methods/) | 检查三个地区的语言/货币/时区/无障碍任务流，列需专业审查法规 | 本地化清单、测试与未知监管项，不虚构合规认证 |


## 专业定义 + 大白话补充（新增基础空缺）

### `PM24` 市场规模 TAM/SAM/SOM 与机会测算

**专业原理**：TAM 为理论总可触达需求上限，SAM 为约束产品能力/地域下的可服务市场，SOM 为考虑渠道与竞争后一定时间可获得的部分；应把规模与频率、价格、证据和假设分开。

**大白话**：城市里所有吃饭的人不是你这家店的客户；店能送到的范围、真正来买的人又是两回事。

**触发需求**：需要评估市场空间或向投资/老板解释机会。

**最小实验**：用公开人口/行业资料和三个明确假设估计范围，并做假设敏感性。

**验收证据**：注明来源、单位、年份、区间、反证，不把市场总量当订单。

**资料**：[S57](https://www.strategyzer.com/library/your-business-model-environment) / [S30](https://www.strategyzer.com/library/the-business-model-canvas)。

### `PM25` 问卷设计/抽样/定量需求研究

**专业原理**：Survey 是受访者自我报告的态度或行为；样本框、招募/无响应偏差、措辞诱导和分母决定能否外推。

**大白话**：只在爱吃辣的微信群发问卷，得到99%爱辣，不能当整个城市的事实。

**触发需求**：想用问卷判断需求比例。

**最小实验**：设计 8 题问卷并列出诱导/双重问题/抽样局限；分析合成应答。

**验收证据**：目标总体、分母、抽样偏差、至少两个反例和不可外推范围。

**资料**：[S55](https://www.nngroup.com/articles/research-methods-glossary/) / [S29](https://www.nngroup.com/articles/which-ux-research-methods/)。

### `PM26` 用户研究知情同意/数据治理

**专业原理**：研究参与者应知情自愿，理解数据采集、使用、留存、共享与退出边界；研究数据与真实产品事件可能有不同授权要求。

**大白话**：顾客给你建议，不等于同意你把录音发布到网上或丢给外部 AI。

**触发需求**：要采访用户/录屏/上传用户资料。

**最小实验**：起草研究同意与撤回流程，用合成数据模拟权限变化/删除。

**验收证据**：同意说明、最小化、删除/保留限制与责任人，不保存私人资料在公开仓。

**资料**：[S43](https://www.nngroup.com/articles/informed-consent/) / [S44](https://www.nngroup.com/articles/research-ops-study-guide/)。

### `PM27` MVP/POC/原型与假设实验

**专业原理**：Prototype 用于探索交互，POC 验证技术可行性，MVP 用最小有意义产品/服务检验关键价值假设，Pilot 是受控试点，Production 是真实运营环境；这些不是同义词。

**大白话**：试吃小摊验证有没有人买（MVP），先试炉灶能否炒菜（POC），画菜单（原型），正式开店（生产）是不同证据。

**触发需求**：客户要求先做 Demo/MVP 或没法判断先做什么。

**最小实验**：为一个产品风险比较访谈/纸面原型/手工服务/POC/MVP，选择最便宜有效验证。

**验收证据**：每种方法的问题、成功/失败、停止阈值及证据强度。

**资料**：[S46](https://www.strategyzer.com/library/experiment-library) / [S42](https://www.producttalk.org/opportunity-solution-trees/) / [S41](https://www.svpg.com/four-big-risks/)。

### `PM28` Scrum Product Owner/Product Goal/Backlog

**专业原理**：在 Scrum 框架中 Product Owner 对最大化产品价值与有效管理 Product Backlog 负责，包括 Product Goal 与条目排序；PM 职位不必然等于 PO。

**大白话**：老板决定做哪类菜；Scrum 的 PO 还要对菜单待办项的透明和排序负责，不代表他包揽每道菜的操作。

**触发需求**：被问 PO/PM 差别或 Sprint 中需求排序。

**最小实验**：拆一条 Product Goal 与 5 条 Backlog，演示 PO 如何排序与拒绝。

**验收证据**：Product Goal、Backlog、责任边界，标明 Scrum 与其他组织模式不同。

**资料**：[S47](https://scrumguides.org/scrum-guide.html?lang=en) / [S49](https://www.atlassian.com/agile/scrum/backlogs/)。

### `PM29` 验收标准 AC/DoD/DoR 的边界

**专业原理**：Acceptance Criteria 约束单条需求的验收行为；Definition of Done 是 Increment 的完成质量共同标准；Definition of Ready 常用但不是官方 Scrum 2020 强制工件。

**大白话**：菜‘少盐’是这单需求的验收；厨房统一食品安全才是全店的 DoD；备料齐不齐是常见 DoR 检查，不是法律。

**触发需求**：需求做完总被退回/验收争议。

**最小实验**：为 3 条需求写 AC，提一个全团队 DoD，并设计错误/安全反例。

**验收证据**：区分范围，不用 AC 冒充上线安全门禁，DoR 标可选实践。

**资料**：[S47](https://scrumguides.org/scrum-guide.html?lang=en) / [S48](https://www.atlassian.com/agile/project-management/definition-of-done)。

### `PM30` 客户之声 VoC/反馈归因与需求合并

**专业原理**：Voice of Customer 需要将售后、访谈、使用日志、投诉按事件去重并标来源与频次；反馈不是未经研究就能直接转换的功能任务。

**大白话**：十个人说‘太慢’可能是同一网络故障，不等于该增加十个功能。

**触发需求**：收到很多用户建议不知道怎么处理。

**最小实验**：合并合成客服/评论/日志，形成问题-证据-假设-行为方案。

**验收证据**：来源、主题聚类、反例、优先级决定与用户通知闭环。

**资料**：[S44](https://www.nngroup.com/articles/research-ops-study-guide/) / [S29](https://www.nngroup.com/articles/which-ux-research-methods/)。

### `PM31` 产品叙事/决策汇报/跨职能沟通

**专业原理**：产品沟通将问题、证据、取舍、风险、备选与结果翻译成可供不同职能作决定的叙事，而不以漂亮 PPT 取代证据。

**大白话**：跟厨师谈做法、跟采购谈成本、跟老板谈投资回报，不是把同一句话重复三遍。

**触发需求**：方案讲不清/评审无法拍板。

**最小实验**：同一决策写领导一页纸与研发 ADR 两种版本，并答反方疑问。

**验收证据**：受众目标、事实/假设、备选、明确决策与反证。

**资料**：[S25](https://www.svpg.com/product-management-an-introduction/) / [S26](https://www.svpg.com/the-product-operating-model-an-introduction/)。

### `PM32` 可用性测试任务与观察/迭代

**专业原理**：Usability Testing 请代表性参与者做代表性任务，观察成功、错误、时长和困难；评价 UI 可用性不同于询问是否喜欢产品。

**大白话**：不要问‘你觉得菜单好看吗’，让客人真的完成点菜并看在哪里卡住。

**触发需求**：原型很美但用户操作失败。

**最小实验**：为原型设计 3 个不诱导的任务，做合成演示并计划真实授权用户测试。

**验收证据**：任务脚本/成功定义/观察与误用，不把模拟评估当真实可用性。

**资料**：[S45](https://www.nngroup.com/articles/qual-usability-testing-study-guide/) / [S29](https://www.nngroup.com/articles/which-ux-research-methods/)。

### `PM33` 产品发布沟通/帮助文档/教育

**专业原理**：产品发布需要版本说明、已知限制、支持路径、用户教育、内部销售/客服培训和反馈渠道，与仅完成 CI/CD 不同。

**大白话**：厨房新菜出锅，不告诉服务员怎么介绍、过敏信息或如何退换，顾客仍体验差。

**触发需求**：功能上线没人会用或客服重复答同样问题。

**最小实验**：写发行说明、FAQ、用户引导、内部培训和故障回退通知。

**验收证据**：可理解文档、支持责任、重大错误公告与可恢复路径。

**资料**：[S50](https://www.atlassian.com/agile/product-management/product-launch) / [S12](https://fastapi.tiangolo.com/deployment/concepts/)。

### `DATA05` 激活/新手引导/首次价值

**专业原理**：Activation 应定义用户首次完成价值事件，而不是仅注册；Onboarding 降低从进入产品到获得价值的阻力。

**大白话**：进店不等于吃到饭；第一次成功下单且吃到满意的饭才接近激活。

**触发需求**：注册很多但次日无人使用。

**最小实验**：用合成事件拆注册→首任务→有效完成漏斗并设计两种引导。

**验收证据**：分母/时间窗/合格用户/真实成功定义，无法验证标假设。

**资料**：[S51](https://www.amplitude.com/blog/getting-started-activation) / [S20](https://www.amplitude.com/guides/product-analytics)。

### `DATA06` 实验统计基础/置信区间/SRM

**专业原理**：随机实验需预定义随机化单位、样本量、主要指标和停止规则；SRM、重复查看、多重比较、非独立样本等可能导致假阳性。

**大白话**：掷硬币分组本应一半一半却严重偏斜，胜负很可能是分组坏了，不是菜更好吃。

**触发需求**：AB 测试涨了 2% 不知道真假。

**最小实验**：合成试验设置预定样本/分组，注入 SRM、提前停止，说明该放弃哪些结论。

**验收证据**：随机化/口径/健康检查/局限，不能把 p 值当效果大小。

**资料**：[S53](https://docs.statsig.com/experiments/monitoring/srm) / [S54](https://statsig.com/blog/product-experimentation-best-practices)。

### `DATA07` 事件埋点规划/数据字典/身份去重

**专业原理**：Event Taxonomy 定义行为事件、属性、版本、身份映射和采集时机，防止漏采/双算/隐私越界；数据质量决定分析可靠性。

**大白话**：顾客点两次按钮不代表吃了两碗饭；如果收银和厨房各记一单就会算错销量。

**触发需求**：指标报表与真实业务数字打架。

**最小实验**：写 8 个事件的字段/类型/去重/权限，并测试重复发送与匿名转登录。

**验收证据**：事件字典、兼容与变更审查、分母/时间窗可复算。

**资料**：[S52](https://amplitude.com/docs/data/data-planning-playbook) / [S20](https://www.amplitude.com/guides/product-analytics)。

### `BIZ13` 产品市场契合 PMF 的证据与反证

**专业原理**：PMF 是持续可观察的市场需求、采用、留存及经济性支持产品价值的判断，不由某个单一百分比、问卷、爆款或一次付费自动证明。

**大白话**：朋友夸好吃只是兴趣，持续复购、合理价格和竞争下仍选你才逐渐支持经营判断。

**触发需求**：不知道产品是否值得扩张。

**最小实验**：对两个产品构建留存、买方、替代成本和风险证据清单并列反证。

**验收证据**：按细分/时间窗/真实重复行为，明确尚未知证据。

**资料**：[S41](https://www.svpg.com/four-big-risks/) / [S31](https://www.strategyzer.com/library/the-value-proposition-canvas)。

### `BIZ14` B2B ROI/价值量化与总拥有成本

**专业原理**：ROI 假设需要对照当前替代方案，含实施/集成/培训/迁移/安全支持成本和可验证收益；客户 ROI 不等于供应商收入。

**大白话**：省了服务员半小时，但买设备、培训和修机器花更多钱，投资未必划算。

**触发需求**：客户问 AI 为什么值得采购。

**最小实验**：按三档假设计算客户现状/AI 方案的 TCO、风险与价值，明确保守假设。

**验收证据**：客户侧/卖方侧成本分开、收益来源和敏感性。

**资料**：[S30](https://www.strategyzer.com/library/the-business-model-canvas) / [S57](https://www.strategyzer.com/library/your-business-model-environment)。

### `MGT06` 产品运营 Product Ops 与变更采用

**专业原理**：Product Operations 聚焦产品团队研究、数据、流程和跨部门协作机制；变更采用包括用户/内部支持和反馈，不能等同监控服务器。

**大白话**：有新菜单还要通知服务员、培训、收集问题、更新备货，而不是只在厨房贴海报。

**触发需求**：组织已交付但一线不用新功能。

**最小实验**：模拟跨部门发布，做沟通/培训/知识库维护/决策日志。

**验收证据**：采用率/反馈/职责，区分 Product Ops 与 DevOps。

**资料**：[S26](https://www.svpg.com/the-product-operating-model-an-introduction/) / [S50](https://www.atlassian.com/agile/product-management/product-launch)。

### `AI15` 生产 AI 质量漂移与人工复核运营

**专业原理**：上线后 AI 质量随模型/检索数据/用户输入/工具环境变化而漂移，需要带版本的采样审计、用户纠错、权限/成本守门和回滚。

**大白话**：试营业时菜好吃不代表换了食材/厨师后一直好吃，得持续抽查并处理差评。

**触发需求**：模型升级后答案突然变差。

**最小实验**：设计金标回归与线上匿名采样计划，模拟来源变更或 Prompt 更新的退化。

**验收证据**：质量/安全/成本监控、人工审查、回滚阈值，避免泄露用户内容。

**资料**：[S05](https://developers.openai.com/api/docs/guides/evaluation-best-practices) / [S07](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) / [S56](https://owasp.org/projects/top-10-for-large-language-model-applications)。

### `GO03` 多语言/本地化/包容性产品

**专业原理**：Internationalization 与 Localization 涉及文本、日期/数字/币种、文化约束、无障碍及用户研究差异；多语言翻译不等于产品适用当地法律与任务。

**大白话**：同一菜单在不同城市不仅要翻译，还要按当地口味、支付和过敏法规适配。

**触发需求**：产品面向多区域用户。

**最小实验**：检查三个地区的语言/货币/时区/无障碍任务流，列需专业审查法规。

**验收证据**：本地化清单、测试与未知监管项，不虚构合规认证。

**资料**：[S09](https://www.w3.org/WAI/WCAG22/quickref/) / [S29](https://www.nngroup.com/articles/which-ux-research-methods/)。


## 如何不按顺序学习

场景先行（例如用户首次登录不会操作），直接 `python tools/learning_router.py route DATA05`，然后沿它的直接前置 DATA01 和 PM20 检查是否已懂；不懂哪个才补哪个。其他路径如 `PM26` 研究授权、`PM27` MVP、`DATA06` A/B、`PM28` Scrum。真正上线需要跨节点 [G0–G7 安全与运营 Gate](../launch/production-readiness.md)，不是可通过跳过学习绕过的系统约束。

**事实分层**：官方/作者方法 ≠ 绝对行业共识，合成案例 ≠ 真实用户，CI PASS ≠ 人独立学会，生产部署 ≠ 市场需求验证或合同成交。
