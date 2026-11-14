# 09 AI Product Engineer：产品工程知识全景与按需训练

> 公开适配自私有上游 AI Learning OS；原始技术深度课程仍归上游维护。本目录强调产品工程角色与证据，学习不限于 30/60/90 天时序。

## 两种互补的入口

- **能力与角色**：[职业路线](roadmap.md) / [30/60/90 条件路线](30-60-90.md) / [7 日 Lab](lab-track.md) 保留作为职业规划参考。
- **当前不会的知识**：直接使用 [图谱节点](../docs/atlas/knowledge-handbook.md)（ENG/AI/OPS）与 [按需 Router](../docs/learning/demand-router.md)，例如 AuthZ 只学 ENG06 的直接依赖；不要求完整刷完全栈路径。

## 产品工程必须覆盖但不要求一次学完

1. **正确需求**：PRD、UAT、非 AI 替代、MVP 边界、业务角色。
2. **稳定交付**：前端 TypeScript、API/数据库、AuthN/AuthZ、多租户、异步/幂等、测试/CI/部署。
3. **AI 可靠性**：模型/Prompt、RAG、Agent/MCP、Context/Harness、金标 Eval、安全与成本。
4. **生产运营**：Trace/SLI-SLO、故障恢复、权限/删除、备份/回滚、持续支持和上线门禁。

涉及 Next.js/Java/FastAPI 的架构迁移，先读 [演进路线](../docs/launch/architecture-evolution.md)。涉及部署是否已可运营，使用 [生产门禁](../docs/launch/production-readiness.md)。

## 最小学习/工程证据

当期主缺口一个，做前测 → 最少理论 → 成功与至少两个相关失败实验 → 本人关 AI 独立排错 → 隔日新约束迁移。工程实际运行记录归原项目仓，学习记录遵循 [治理协议](../GOVERNANCE.md)。
