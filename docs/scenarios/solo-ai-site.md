# 个人 AI 网站从 MVP 到长期可用

> 场景设计状态：DESIGNED_NOT_RUN / HUMAN_UNASSESSED。不能把合成演练当真实用户或生产验收。

## 最小问题与反证

基于公开/合成资料，写一个真实可观察的用户任务。先比较人工/规则/现成平台方案，说明什么证据会让你放弃新建应用。场景常见失败：Next.js/FastAPI 部署边界、SEO、用户注册/内容/AI 功能。

## 按需知识路由

首选节点：`PM02`（问题定义与 JTBD）、`PM08`（信息架构/原型/UI 状态）、`ENG01`（Web/HTTP/DNS/TLS）、`ENG02`（前端组件/状态/TypeScript）、`ENG03`（API 契约与输入验证）、`ENG04`（SQL/事务/迁移）、`ENG06`（AuthN/AuthZ/多租户隔离）、`ENG11`（容器/环境与配置管理）、`ENG12`（部署拓扑与架构演化）、`ENG13`（前端 SEO/性能/可访问性）、`OPS01`（CI/CD/Release/回滚）、`OPS06`（真实用户 UAT/发布与维护门禁）。

不要一口气全学；先找导致失败的**一个**节点，按直接依赖回溯未掌握基础。运行：
```bash
python tools/learning_router.py scenario solo-ai-site
python tools/learning_router.py route PM02
```

## 实验协议

1. **需求基线**：用户、使用者和买方、权限、当前替代、成本和停止条件。无买方证明写 UNKNOWN。
2. **前测**：关闭 AI 绘制最短工作链或行为流，并预测至少两个失败点。
3. **学习**：只读本次节点的权威资料 1–2 篇，解释如何改变产品/工程决策；参考 [知识手册](../atlas/knowledge-handbook.md)。
4. **最小实践**：构建公开/合成样本与 Mock API/Mock 工具，对同一任务做 NO_AI/规则基线和需要时的 AI 对照。
5. **测试**：一条成功用例 + 两条与场景相关的失败/安全负例，预注册指标与分母；提交输出与 commit，而非只描述结果。
6. **闭卷**：关闭 AI 独立修一个陌生输入/状态错误；1/3/7 天换约束复测。
7. **Go/Stop**：记录技术门禁/用户验证/商业证据，不能越权使用真实客户资料。

**最低验收**：干净部署+AuthZ+备份恢复+发布回滚+真实UAT证据分级。完整上线必须另经过 [生产 Gate](../launch/production-readiness.md)。

记录：[Task Contract](../learning/task-contract.md)；资料：[权威资源索引](../../resources/official-resources.md)。
