# 权威资料学习索引（2026-11-14 复核）

> 索引的目标是**每个知识点都有来源**，不是为涨收藏数。资料 URL 见机器源 [authorities.json](authorities.json)，逐知识匹配见 [knowledge-handbook](../docs/atlas/knowledge-handbook.md)。外部页面只核查到可阅读，不代表第三方工具本地实测。

| 类别 | 官方入口 | 适用学习节点 | 限制与版本 |
|---|---|---|---|
| 产品发现与需求来源 | [Atlassian Product Discovery](https://www.atlassian.com/agile/product-management/discovery) | `PM01`、`PM02`、`PM03`、`PM04`、`PM05`、`PM12`、`DATA03`、`BIZ01`、`BIZ04`、`BIZ05` | 官方产品方法；核验 2026-11-14 |
| PRD 与需求 | [Atlassian Requirements](https://www.atlassian.com/agile/product-management/requirements) | `PM01`、`PM07`、`PM10` | 官方产品方法；核验 2026-11-14 |
| 路线图与决策 | [Atlassian Product Roadmaps](https://www.atlassian.com/agile/product-management/product-roadmaps) | `PM04`、`PM05`、`PM06`、`PM10`、`PM12`、`BIZ01`、`BIZ02`、`BIZ05` | 官方产品方法；核验 2026-11-14 |
| 以人为本 AI 设计 | [Google PAIR Guidebook](https://pair.withgoogle.com/guidebook-v2/) | `PM02`、`PM03`、`PM08`、`PM09`、`PM11`、`AI10`、`OPS06` | 官方设计指南（仅链接；有非商业授权限制）；核验 2026-11-14 |
| AI 评测方法 | [OpenAI Evaluation Best Practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | `AI01`、`AI02`、`AI11`、`AI13`、`AI14` | 官方指南；旧 Evals 平台有退役安排，勿把旧接口当新实验起点；核验 2026-11-14 |
| Workflow/Agent 工程取舍 | [Anthropic Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | `AI05`、`AI07`、`AI08`、`AI09` | 厂商工程指南；核验 2026-11-14 |
| AI 治理风险 | [NIST GenAI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) | `AI04`、`AI11`、`AI12`、`OPS05`、`ETH01` | 官方风险框架；非法律合规认证；核验 2026-11-14 |
| Web 安全风险 | [OWASP Top 10:2025](https://top10.owasp.org/2025/0x00_2025-Introduction/) | `AI06`、`AI12`、`ENG06`、`ENG10`、`OPS05`、`BIZ03` | 行业安全项目；核验 2026-11-14 |
| 无障碍 | [W3C WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/) | `PM08`、`ENG13`、`ETH01` | W3C 技术标准；核验 2026-11-14 |
| HTTP 与协议 | [MDN Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) | `ENG01`、`ENG03`、`ENG07`、`ENG14` | Web 文档参考；核验 2026-11-14 |
| 应用鉴权 | [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/) | `ENG03`、`ENG06` | 框架官方文档；核验 2026-11-14 |
| 后端部署 | [FastAPI Deployment Concepts](https://fastapi.tiangolo.com/deployment/concepts/) | `ENG01`、`ENG05`、`ENG08`、`ENG09`、`ENG11`、`ENG14`、`OPS03`、`OPS04` | 框架官方文档；核验 2026-11-14 |
| 数据库事务 | [PostgreSQL Official Tutorial](https://www.postgresql.org/docs/current/tutorial.html) | `ENG04`、`ENG05`、`BIZ03` | 数据库官方文档；核验 2026-11-14 |
| Next.js 上线清单 | [Next.js Production Checklist](https://nextjs.org/docs/app/guides/production-checklist) | `ENG02`、`ENG09`、`ENG12`、`ENG13`、`OPS01` | 框架官方文档；核验 2026-11-14 |
| 容器化部署 | [Docker Compose in Production](https://docs.docker.com/compose/how-tos/production/) | `ENG11`、`OPS01`、`OPS04` | 基础设施官方文档；核验 2026-11-14 |
| 可观测性 | [OpenTelemetry Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/) | `PM11`、`ENG08`、`OPS02`、`OPS03`、`OPS06` | 开源项目官方文档；核验 2026-11-14 |
| Agent/RAG/Context 教程 | [LangChain/LangGraph Learn](https://docs.langchain.com/oss/python/learn) | `AI03`、`AI04`、`AI05`、`AI07`、`AI08`、`AI09`、`ENG07` | 框架官方文档；使用前确认版本与状态机制；核验 2026-11-14 |
| MCP 现代协议 | [MCP 2026-07-28 Release](https://blog.modelcontextprotocol.io/posts/2026-07-28/) | `AI06` | 官方版本公告；实现需核对具体 SDK 版本；核验 2026-11-14 |
| LLM/Embedding/生产 ML | [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) | `AI01`、`AI02`、`AI03`、`AI10`、`AI13`、`AI14` | 官方课程含交互与练习；核验 2026-11-14 |
| 分析与增长 | [Amplitude Product Analytics Guide](https://www.amplitude.com/guides/product-analytics) | `DATA01`、`DATA02`、`DATA03`、`BIZ02`、`BIZ04` | 厂商产品分析指南；核验 2026-11-14 |
| 前端部署选项 | [Next.js Deploying](https://nextjs.org/docs/app/getting-started/deploying) | `ENG02`、`ENG12` | 框架官方部署指南；核验 2026-11-14 |
| AI 数据与失败设计 | [Google PAIR Chapters](https://pair.withgoogle.com/guidebook-v2/chapters) | `PM09` | 官方 UX 指南，仅链接；核验 2026-11-14 |
| Web 安全清单入口 | [OWASP Top 10](https://owasp.org/projects/top-ten) | `ENG10` | 安全共识参考，按当前版本复核；核验 2026-11-14 |
| LangGraph 教程索引 | [LangChain Learn](https://docs.langchain.com/oss/python/learn) |  | 框架官方教程；条件触发时深入；核验 2026-11-14 |

**重要时效提醒**：OpenAI [Evaluation Best Practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) 描述旧 Evals 平台于 **2026-10-31** 转只读，并计划 **2026-11-30** 关闭；学习的是 Eval 方法与数据集/回归思路，新项目先核查最新可用评测 API/工具。MCP 需按协议版本判断兼容性，2026-07-28 已发生重要变化；不能无脑复用旧会话/传输教程。

**素材版权**：Google PAIR 内容标注 CC BY-NC-SA 许可，出于公共仓 MIT 内容兼容考虑仅放来源链接和原创解释，不复制其页面/插图。其他官方文档也须按原许可使用，不因链接在此仓而自动重授权。
