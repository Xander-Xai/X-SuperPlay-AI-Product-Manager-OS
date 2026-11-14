# AI Product Manager × AI Product Engineer：全景知识 Roadmap（需求驱动版）

> **v0.2.0 · 2026-11-14 · CURRICULUM_DESIGNED / PRACTICE_NOT_RUN / HUMAN_UNASSESSED**  
> **全景知识关系是稳定地图，不是强制学习顺序。学习顺序由实际问题、风险与缺口动态选择。** 12 周/30-60-90 天只作为可选复盘节奏，不再是先修关卡。

## 一、三层操作模型

1. **知识全景 Atlas**：回答「这个知识解决什么、和哪些知识存在逻辑依赖、为何必须懂？」→ [图谱解释](docs/atlas/knowledge-graph.md) / [机器可读知识卡](docs/atlas/knowledge-catalog.json) / [逐主题实操指南](docs/atlas/knowledge-handbook.md)。
2. **需求驱动 Router**：回答「今天卡在哪、最低要学什么？」→ [触发矩阵](docs/learning/demand-router.md)、[命令行路由](tools/learning_router.py)、[学习任务契约](docs/learning/task-contract.md)。
3. **真实上线 Gate**：回答「学完能否开发、部署、测试、运营？」→ [生产门禁](docs/launch/production-readiness.md)、[迁移决策](docs/launch/architecture-evolution.md)、[场景练习](docs/scenarios/README.md)。

这三层互补：**知识覆盖要完整，执行按需求最小化；学习产物要能迁移到真实交付，但不要求每次学习都启动一个下游项目。**

## 二、知识地图的逻辑关系（不是课程时序）

```text
真实问题 / 触发证据
├── 用户是谁/为何痛 ─→ JTBD / 访谈 ─→ 市场替代/买方 ─→ 产品战略/优先级
├── 产品要怎样运行 ─→ PRD/UAT ─→ 流程/异常UX ─→ 数据指标/留存
├── AI 是否值得用 ─→ NO_AI基线 ─→ LLM/Prompt ─→ RAG 或 Workflow/Agent
│                                  ├── Context/Harness/Memory/MCP（必要时）
│                                  └── Eval/Guardrails/成本/安全（必须）
├── 系统如何工作 ─→ HTTP/API ─→ 数据/事务 ─→ 身份与授权 ─→ UI/异步
│                     └── 测试 ─→ Docker/CI/CD ─→ Trace/容量 ─→ 恢复/发布
└── 业务是否值得做 ─→ 买方/定价 ─→ 单位经济 ─→ 增长/实验 ─→ 复盘或停止
```

依赖表示**理解/安全上的最小前置知识**，不是「必须按 ID 从小到大刷课」。例如定位“跨租户越权”可以直接进入 ENG06，缺 HTTP/数据库概念时再沿图回溯 ENG03/ENG04，**不需要从产品历史开始**。

## 三、能力全景：跨角色、跨产品阶段覆盖

| 能力域 | 产品侧必须懂的 | 工程侧需能做的 | 权威参考 | 实际成果 |
|---|---|---|---|---|
| 发现与战略 | JTBD/访谈/替代/细分/优先级/路线图 | 技术可行性与非 AI 方案 | [Atlassian Discovery](https://www.atlassian.com/agile/product-management/discovery) | 带反证的问题/价值卡 |
| 设计与体验 | PRD、工作流、错误态、可信交互/无障碍 | UI、状态、接口契约、无障碍 | [Google PAIR](https://pair.withgoogle.com/guidebook-v2/) / [W3C](https://www.w3.org/WAI/WCAG22/quickref/) | 可测试 PRD + UX |
| AI 产品 | LLM/Prompt/RAG/Agent/MCP/多模态/模型选型 | 检索、Context/Harness、工具、安全、恢复 | [Anthropic](https://www.anthropic.com/engineering/building-effective-agents) / [OpenAI Evals](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | ADR、金标、负例与对照 |
| 产品工程 | MVP架构与迁移成本、风险边界 | HTTP/UI/API/SQL/事务/AuthZ/异步/缓存/版本 | [FastAPI](https://fastapi.tiangolo.com/tutorial/security/) / [PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) | 端到端纵切和恢复日志 |
| 生产运营 | SLO/支持/上线判断 | CI/CD、监控/Trace、压测、密钥/备份/回滚 | [OpenTelemetry](https://opentelemetry.io/docs/concepts/observability-primer/) / [Docker](https://docs.docker.com/compose/how-tos/production/) | 运行手册与故障演练 |
| 风险与合规 | 风险分级、真实用户知情、商业承诺边界 | Web/LLM 安全、数据删除/租户隔离、审计 | [OWASP 2025](https://top10.owasp.org/2025/0x00_2025-Introduction/) / [NIST](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | 权限/注入/恢复负例 |
| 数据与商业 | 北极星、漏斗、A/B、Buyer/价格/现金流 | 埋点、成本测量、订阅幂等 | [Amplitude](https://www.amplitude.com/guides/product-analytics) | 可复算指标和经济模型 |

## 四、双轨与选修深度

- **AI Product Manager**：在所有领域先达到 **可独立判断/定义验收**，不强制自己训练模型或写 K8s；AI 选型、安全、数据与商业必须能解释取舍。
- **AI Product Engineer**：在要交付的场景完成 **可运行、可测试、可恢复** 的技术纵切；同时具备最小产品发现/PRD/商业判断，不以写代码代替需求验证。
- **技术深入（按需）**：大模型训练/LoRA、优化器、分布式推理、RAG、LangGraph、Harness、Context Engineering、Fullstack 来自 [上游技术学习仓](resources/upstream-downstream-index.md)，本仓提供它们在产品中的位置/触发条件/目标证据，不重复所有技术教程。
- **可选时间视图**：保留 [原 PE 30/60/90](09-Product-Engineering/30-60-90.md) 与 [PM 基础 12 周参考时窗](docs/learning/optional-cadence.md) 供复盘；**不得当成必走路线**。今天若有上线授权失败，直接走 AuthZ/安全/发布学习路径。

## 五、学习一个知识点的 7 个动作

```text
需求/失败 → 事实证据与权限 → 选择 1 个主 Gap
→ 查询 Atlas 的“为何/依赖/权威资料”
→ 先关 AI 前测 → 最小实验（正例+至少2负例）
→ 关 AI 独立复现/解释 → 1/3/7 天陌生约束迁移
→ 已有证据则入库；真实用户/收入仍由权威仓判定
```

每张机器知识卡保证：**ID / 作用 / 逻辑依赖 / 触发词 / 官方资料 / 动手练习 / 客观证据**；[按需路由 CLI](tools/learning_router.py) 会沿依赖回溯，但默认只推荐**主节点 + 直接前置**，可选 `--deep` 查看完整依赖链。

## 六、常见需求：跳转，不从头学

| 当前遇到的现象 | 第一个学习入口 | 何时向前补 |
|---|---|---|
| 不确定用户为何要 AI | PM02 / PM03 / PM04 | 没有用户目标时看 PM01 |
| PRD 到研发不断返工 | PM07 / PM10 / ENG03 | 验收问题不清再补 PM02 |
| RAG 引用旧文档/泄密 | AI04 / ENG06 / AI11 | 不懂召回/金标时再补 AI03 |
| Agent 乱调用/重试双写 | AI05 / AI08 / ENG07 / AI12 | 不懂工具边界再看 ENG03 |
| 上线后卡顿/费用高 | OPS02 / OPS03 / AI13 | 无请求链补 ENG01 |
| Next.js MVP 担心迁移 | ENG12 / ENG04 / ENG06 | 先明确数据模型、外部接口和边界 |
| AI SaaS 收费与退款 | BIZ01 / BIZ03 / BIZ02 | 先证明真实买方与授权使用 |
| 活跃多但用户没价值 | DATA01 / DATA02 / PM09 | 先定义任务完成 |
| 产品能跑但不敢上线 | OPS06 / OPS04 / OPS05 / ENG10 | 安全硬门禁优先，缺基础依赖按需补 |

## 七、完成的判断

**覆盖完成**：知识节点有可信材料、逻辑/依赖关系、练习与可检查的门槛。  
**学会**：本人独立做出/解释/迁移；从未练过不能标 PASS。  
**真正上线**：有合法数据/权限、可复现部署、AuthZ/安全、评测、监控、备份/回滚、真实运维责任和用户验证（按场景）。产品能上线不等于客户会付费。详见 [生产上线清单](docs/launch/production-readiness.md)。

## 八、索引与边界

[按需求搜索](docs/learning/demand-router.md) · [知识与来源](docs/atlas/knowledge-handbook.md) · [官方参考](resources/official-resources.md) · [场景矩阵](docs/scenarios/README.md) · [跨仓责任](resources/upstream-downstream-index.md) · [学习验收](12-Assessments/rubric.md)。

> **特别提示（2026-11-14）**：OpenAI 官方资料明确旧 Evals 平台已进入弃用流程（2026-10-31 只读、2026-11-30 计划关闭），本仓引用的是**评测方法**，不要把旧平台 API 作为新练习的可持续依赖。


## 九、可直接运行的三个微型实验

[离线 Lab 总索引](labs/README.md)：规则检索/引用与租户隔离、Agent 审批与幂等、任务成功率与单位成本。所有输入均为合成数据，**不是生产级 RAG 或 Agent**；先理解机制/失败，再在真实授权项目中扩展。
