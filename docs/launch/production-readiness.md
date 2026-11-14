# 从“能跑 Demo”到“真实可运营”：上线知识与证据门禁

> **本仓提供可学习/可验收的知识体系，不证明任何项目已上线。** 风险分级决定实际门槛；涉及支付、健康、法律等高风险用途需额外专业审查和合规验证。上线不等于有真实用户/有营收。

## 上线 Gate 不是阶段课表，而是交付前必须具备的证据

| Gate | 它解决的真实问题 | 最小应提交证据 | 知识节点 |
|---|---|---|---|
| G0 需求与授权 | 为谁做、数据是否合法、是否允许开发 | 来源/用途/授权、停止条件、非 AI 基线 | PM02 PM03 PM07 OPS05 |
| G1 技术边界 | UI/API/DB/模型/工具的稳定契约 | 版本化 ADR、数据边界、依赖图、迁移计划 | ENG03 ENG04 ENG12 AI05 |
| G2 数据与权限 | 登录≠授权；读写/删改必须安全 | 用户 A/B 交叉读写失败、权限撤销、敏感数据最小化 | ENG06 ENG10 OPS05 AI04 |
| G3 AI 质量与安全 | 错答、引用错误、注入、过度代理、成本飙升 | 有版本的金标/负例、人工复核、模型变更回归 | AI11 AI12 AI13 |
| G4 工程可靠性 | 宕机、双写、队列积压、回滚 | 正常+失败端到端测试、重试幂等、故障注入 | ENG07 ENG08 ENG09 |
| G5 部署与恢复 | 本机能跑但线上起不来 | 干净环境/密钥/HTTPS/健康检查、备份恢复、CI/CD 回滚演练 | ENG11 OPS01 OPS04 |
| G6 运营可观测 | 线上问题找不到根因、用户损失无法估算 | 端到端 trace、错误/延迟/成本仪表、告警责任人 | OPS02 OPS03 PM11 |
| G7 用户与业务验收 | 服务运行≠解决需求；收费不等于利润 | 经授权 UAT、运营支持流程、成本边界、定价假设 | PM09 OPS06 BIZ02 DATA01 |

**发布阻断**：缺明确数据授权、跨租户越权、可触发未审批高风险写操作、泄露密钥/PII、无法回滚关键数据迁移等按本场景设为 HARD_FAIL。非安全指标阈值需要需求方在实验前设定；不能用一组放之四海皆准的数字谎称生产就绪。

**可执行实训**：[E1–E8 真实交付训练路径](production-apprenticeship.md) · [Release Evidence 模板](release-evidence-template.md)。

## 上线之前的最小演练

1. 用隔离的公开/合成数据，在干净环境构建与启动，固定版本、依赖、配置、权限、健康检查。
2. 做用户主流程成功场景，记录服务端日志、请求追踪、实际时延和成本。
3. 预先注册 2 条以上本场景关键失败用例（AuthZ、重复写入、模型超时、引用错、注入等），实际运行并保存结果。
4. 做数据备份恢复、发布回滚、密钥轮换/异常停机演练。
5. 与实际业务/用户验收隔离：**合成 UAT 只证明练习**，真实投产要使用方授权、安全和可恢复性经实际负责人审查。

## 正确理解“可上线”和“长期可用”

本仓覆盖知识点与训练方法，即使静态 CI 通过，也只是 Curriculum Gate。真正的服务交付需要**项目本体工程仓**保留测试执行输出、部署链接、监控、负责人和故障恢复记录。业务需求和收入事实另由权威源核实。

参考：[Docker Production](https://docs.docker.com/compose/how-tos/production/) · [FastAPI Deploy](https://fastapi.tiangolo.com/deployment/concepts/) · [Next.js Checklist](https://nextjs.org/docs/app/guides/production-checklist) · [OWASP 2025](https://top10.owasp.org/2025/0x00_2025-Introduction/) · [OpenTelemetry](https://opentelemetry.io/docs/concepts/observability-primer/) · [NIST](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)。
