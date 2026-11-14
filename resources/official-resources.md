# AI 产品经理学习资料：规范、原作者、厂商与社区工具

> 审计日期 2026-11-14。全部资料元数据的唯一权威：[authorities.json](authorities.json)。**链接存在/页面曾阅读 ≠ 已验证全部操作步骤/代码**；外部站点可能变更。此页是索引，不复制第三方知识产权文本。

| ID | 领域 | 原始资料链接 | 学术/业界地位与适用边界 | 状态 |
|---|---|---|---|---|
| `S01` | 产品发现与需求来源 | [Atlassian Product Discovery](https://www.atlassian.com/agile/product-management/discovery) | 官方产品方法 | PAGE_REVIEWED_NOT_EXECUTED |
| `S02` | PRD 与需求 | [Atlassian Requirements](https://www.atlassian.com/agile/product-management/requirements) | 官方产品方法 | PAGE_REVIEWED_NOT_EXECUTED |
| `S03` | 路线图与决策 | [Atlassian Product Roadmaps](https://www.atlassian.com/agile/product-management/product-roadmaps) | 官方产品方法 | PAGE_REVIEWED_NOT_EXECUTED |
| `S04` | 以人为本 AI 设计 | [Google PAIR Guidebook](https://pair.withgoogle.com/guidebook-v2/) | 官方设计指南（仅链接；有非商业授权限制） | PAGE_REVIEWED_NOT_EXECUTED |
| `S05` | AI 评测方法 | [OpenAI Evaluation Best Practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | 官方指南；旧 Evals 平台有退役安排，勿把旧接口当新实验起点 | PAGE_REVIEWED_NOT_EXECUTED |
| `S06` | Workflow/Agent 工程取舍 | [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | 厂商工程指南 | PAGE_REVIEWED_NOT_EXECUTED |
| `S07` | AI 治理风险 | [NIST GenAI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | 官方风险框架；非法律合规认证 | PAGE_REVIEWED_NOT_EXECUTED |
| `S08` | Web应用安全（非LLM安全） | [OWASP Top 10:2025 (Web Application Security)](https://top10.owasp.org/2025/0x00_2025-Introduction/) | 行业安全项目；LLM 安全需看专门的 S56 清单 | PAGE_REVIEWED_NOT_EXECUTED |
| `S09` | 无障碍 | [W3C WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) | W3C 技术标准 | PAGE_REVIEWED_NOT_EXECUTED |
| `S10` | HTTP 与协议 | [MDN Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) | Web 文档参考 | PAGE_REVIEWED_NOT_EXECUTED |
| `S11` | 应用鉴权 | [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/) | 框架官方文档 | PAGE_REVIEWED_NOT_EXECUTED |
| `S12` | 后端部署 | [FastAPI Deployment Concepts](https://fastapi.tiangolo.com/deployment/concepts/) | 框架官方文档 | PAGE_REVIEWED_NOT_EXECUTED |
| `S13` | 数据库事务 | [PostgreSQL Official Tutorial](https://www.postgresql.org/docs/current/tutorial.html) | 数据库官方文档 | PAGE_REVIEWED_NOT_EXECUTED |
| `S14` | Next.js 上线清单 | [Next.js Production Checklist](https://nextjs.org/docs/app/guides/production-checklist) | 框架官方文档 | PAGE_REVIEWED_NOT_EXECUTED |
| `S15` | 容器化部署 | [Docker Compose in Production](https://docs.docker.com/compose/how-tos/production/) | 基础设施官方文档 | PAGE_REVIEWED_NOT_EXECUTED |
| `S16` | 可观测性 | [OpenTelemetry Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/) | 开源项目官方文档 | PAGE_REVIEWED_NOT_EXECUTED |
| `S17` | Agent/RAG/Context 教程 | [LangChain/LangGraph Learn](https://docs.langchain.com/oss/python/learn) | 框架官方文档；使用前确认版本与状态机制 | PAGE_REVIEWED_NOT_EXECUTED |
| `S18` | MCP 现代协议 | [MCP 2026-07-28 Release](https://blog.modelcontextprotocol.io/posts/2026-07-28/) | 官方版本公告；实现需核对具体 SDK 版本 | PAGE_REVIEWED_NOT_EXECUTED |
| `S19` | LLM/Embedding/生产 ML | [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) | 官方课程含交互与练习 | PAGE_REVIEWED_NOT_EXECUTED |
| `S20` | 分析与增长 | [Amplitude Product Analytics Guide](https://www.amplitude.com/guides/product-analytics) | 厂商产品分析指南 | PAGE_REVIEWED_NOT_EXECUTED |
| `S21` | 前端部署选项 | [Next.js Deploying](https://nextjs.org/docs/app/getting-started/deploying) | 框架官方部署指南 | PAGE_REVIEWED_NOT_EXECUTED |
| `S22` | AI 数据与失败设计 | [Google PAIR Chapters](https://pair.withgoogle.com/guidebook-v2/chapters) | 官方 UX 指南，仅链接 | PAGE_REVIEWED_NOT_EXECUTED |
| `S23` | Web 安全清单入口 | [OWASP Top 10](https://owasp.org/projects/top-ten) | 安全共识参考，按当前版本复核 | PAGE_REVIEWED_NOT_EXECUTED |
| `S24`（同 `S17`） | LangGraph 教程索引 | [LangChain Learn](https://docs.langchain.com/oss/python/learn) | 框架官方教程；条件触发时深入；重复入口，优先使用 S17 | ALIAS_USE_CANONICAL |
| `S25` | expanded-product-management | [SVPG 产品经理与四大风险](https://www.svpg.com/product-management-an-introduction/) | SVPG 原作者产品方法介绍 | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S26` | expanded-product-management | [SVPG 产品运营模式](https://www.svpg.com/the-product-operating-model-an-introduction/) | 跨职能团队、发现与交付 | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S27` | expanded-product-management | [Product Talk 产品发现概念](https://www.producttalk.org/glossary-discovery-product-discovery/) | 作者对 Discovery 的定义与工作循环 | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S28` | expanded-product-management | [Opportunity Solution Tree / 持续发现](https://www.producttalk.org/getting-started-with-discovery/) | 作者方法论；结果-机会-方案-假设 | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S29` | expanded-product-management | [NN/g 用户研究方法选择](https://www.nngroup.com/articles/which-ux-research-methods/) | UX 研究一手研究方法解释，2026-07 复核 | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S30` | expanded-product-management | [Strategyzer 商业模式画布](https://www.strategyzer.com/library/the-business-model-canvas) | 官方画布原作者方法 | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S31` | expanded-product-management | [Strategyzer 价值主张画布](https://www.strategyzer.com/library/the-value-proposition-canvas) | 官方画布原作者方法 | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S32` | expanded-product-management | [Scrum Guide](https://scrumguides.org/scrum-guide.html?lang=en) | Scrum 官方指南：Product Owner、Backlog、Product Goal | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S33` | expanded-product-management | [PMI 项目与风险管理材料](https://www.pmi.org/learning/library/bringing-pmbok-guide-life-practical-8009) | 项目管理组织技术说明；页面为旧文章，只作框架理解 | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S34` | expanded-product-management | [Atlassian 新产品开发流程](https://www.atlassian.com/agile/product-management/new-product-development-process) | 来源解释 discovery→development→launch 迭代非严格线性 | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S35` | expanded-product-management | [Atlassian 产品优先级框架](https://www.atlassian.com/agile/product-management/prioritization-framework) | RICE 输入和适用限制 | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S36` | expanded-product-management | [Atlassian Product Operating Model](https://www.atlassian.com/agile/product-management/product-operating-model) | 组织的产品运作、治理与责任 | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S37`（同 `S01`） | expanded-product-management | [Atlassian 动态产品发现](https://www.atlassian.com/agile/product-management/discovery) | 持续发现、Now/Next/Later 与跨团队反馈；重复入口，优先使用 S01 | ALIAS_USE_CANONICAL |
| `S38` | expanded-product-management | [NN/g UX Research Cheat Sheet](https://www.nngroup.com/articles/ux-research-cheat-sheet/) | 从用户研究任务选用合适方法 | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S39` | expanded-product-management | [phuryn/pm-skills（开源社区工具，不是权威理论）](https://github.com/phuryn/pm-skills) | 可选 PM 工作流参考；安装前审查许可/权限/当前 SHA | WEB_PAGE_REVIEWED_NOT_EXECUTED |
| `S40`（同 `S22`） | expanded-product-management | [Google PAIR 六章节 AI 人机体验](https://pair.withgoogle.com/guidebook-v2/chapters) | 官方 AI UX：需求、数据、心智模型、解释、反馈与错误；重复入口，优先使用 S22 | ALIAS_USE_CANONICAL |
| `S41` | 四大产品风险 | [SVPG The Four Big Risks](https://www.svpg.com/four-big-risks/) | SVPG 原作者；value/usability/feasibility/viability，非法律强制标准 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S42` | OST 发现与机会 | [Product Talk Opportunity Solution Trees](https://www.producttalk.org/opportunity-solution-trees/) | Product Talk 方法原作者，机会与方案不是同一个层次 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S43` | 研究伦理 | [NN/g Obtaining Consent for User Research](https://www.nngroup.com/articles/informed-consent/) | NN/g 研究知情同意原则 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S44` | 研究运营 | [NN/g ResearchOps Study Guide](https://www.nngroup.com/articles/research-ops-study-guide/) | NN/g 研究样本、隐私与研究资料治理 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S45` | 可用性测试 | [NN/g Qualitative Usability Testing](https://www.nngroup.com/articles/qual-usability-testing-study-guide/) | NN/g 代表性任务、参与者、主持与观察 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S46` | 假设与实验 | [Strategyzer Experiment Library](https://www.strategyzer.com/library/experiment-library) | 原作者实验库；成本/证据强度，具体实验设计需结合情境 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S47`（同 `S32`） | Scrum Product Owner 规范 | [Official Scrum Guide 2020](https://scrumguides.org/scrum-guide.html?lang=en) | Scrum 唯一官方职责、工件和承诺定义（2026-11 查仍为2020官方版）；与 S32 同一 URL | ALIAS_USE_CANONICAL |
| `S48` | DoD/DoR/AC 术语 | [Atlassian Definition of Done](https://www.atlassian.com/agile/project-management/definition-of-done) | 实践解释；Scrum DoD 责任以 Scrum Guide 为准 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S49` | Backlog 需求管理 | [Atlassian Product Backlog](https://www.atlassian.com/agile/scrum/backlogs/) | 厂商敏捷方法，不代替 Scrum 官方角色规范 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S50` | 产品发布与交接 | [Atlassian Product Launch](https://www.atlassian.com/agile/product-management/product-launch) | 产品定位、发布沟通、销售与支持材料 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S51` | 激活与首次价值 | [Amplitude Product Activation](https://www.amplitude.com/blog/getting-started-activation) | 厂商产品分析指南，需按本产品定义激活 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S52` | 埋点分类与数据质量 | [Amplitude Plan Event Taxonomy](https://amplitude.com/docs/data/data-planning-playbook) | 厂商官方数据规划文档，事件版本和口径 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S53` | 实验健康检查 | [Statsig Sample Ratio Mismatch](https://docs.statsig.com/experiments/monitoring/srm) | Statsig 产品实验文档，流量分配偏差检查 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S54` | 实验统计与观察 | [Statsig Product Experimentation Best Practices](https://statsig.com/blog/product-experimentation-best-practices) | 厂商实验实务；样本量/多重查看/顺序检验须按设计 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S55` | 问卷研究方法 | [NN/g UX Research Methods Glossary](https://www.nngroup.com/articles/research-methods-glossary/) | NN/g 调查/观察方法差异与定义 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S56` | 大模型应用安全 | [OWASP Top 10 for LLM Applications](https://owasp.org/projects/top-10-for-large-language-model-applications) | LLM 风险目录；与 OWASP Web Top10 不是同一清单 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |
| `S57` | 市场环境与机会 | [Strategyzer Business Model Environment](https://www.strategyzer.com/library/your-business-model-environment) | Strategyzer 原作者对市场/行业/趋势/宏观环境的框架 | SOURCE_PAGE_CHECKED_NOT_PRACTICED |

## 一致性重点

- `S08`：Web 应用 OWASP Top 10；`S56`：LLM 应用安全 OWASP Top 10。不能混为同一份清单。
- `S24→S17`、`S37→S01`、`S40→S22`、`S47→S32` 为旧入口的兼容别名；这四组同 URL 只算一份独立来源。**不删除原 ID，否则旧知识卡会失效**。
- Scrum 的 PO、Scrum Team、Product Goal、Backlog、DoD 以官方 Scrum Guide 为规范。PM 与 PO 职位是否合并由具体组织决定。
- SVPG、Product Talk、Strategyzer 为**方法原作者**；NN/g 是用户研究专业机构；Atlassian/Amplitude/Statsig/OpenAI 是厂商资料。方法论不是强制法律标准。
- Google PAIR、第三方图文/教材等必须按原授权使用；本公共 MIT 仓仅保存链接与原创解释。
- OpenAI 的旧 Evals 平台截至审计日被标记进入只读/计划关停，开发新评测要按官方最新受支持产品或可独立运行的评测框架，不能照搬旧工作流。

**使用**：[102 节点知识手册](../docs/atlas/knowledge-handbook.md) · [按需求路由](../docs/learning/product-foundations-task-router.md) · [上游私人专题资料](upstream-pm-knowledge-index.md)。
