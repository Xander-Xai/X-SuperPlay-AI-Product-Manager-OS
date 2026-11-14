# 场景反向索引：需求 → 知识 → 实验 → 可上线门禁

> 这里是知识使用样本与练习路径，不要求每学一个知识就建一个下游产品。场景全部 DESIGNED_NOT_RUN。

| 当前要解决的真实需求 | 直接入口 | 重点知识 | 预期证据 |
|---|---|---|---|
| [知识助手引用错误/权限越界](rag-knowledge-assistant.md) | `python tools/learning_router.py scenario rag-knowledge-assistant` | `PM02`, `PM07`, `AI03`, `AI04`, `AI11`, `ENG06`, `OPS06` | retrieval gold+引用支持率与越权 0 次通过、干净环境复现 |
| [Agent 工单工具越权/重试双写](agent-approval.md) | `python tools/learning_router.py scenario agent-approval` | `PM07`, `AI05`, `AI06`, `AI08`, `ENG07`, `ENG08`, `AI12`, `OPS02` | 所有安全硬门禁通过、审批前零写入、trace 可回放 |
| [个人 AI 网站从 MVP 到长期可用](solo-ai-site.md) | `python tools/learning_router.py scenario solo-ai-site` | `PM02`, `PM08`, `ENG01`, `ENG02`, `ENG03`, `ENG04`, `ENG06`, `ENG11`, `ENG12`, `ENG13`, `OPS01`, `OPS06` | 干净部署+AuthZ+备份恢复+发布回滚+真实UAT证据分级 |
| [AI SaaS 订阅与可靠交付](paid-ai-saas.md) | `python tools/learning_router.py scenario paid-ai-saas` | `PM03`, `BIZ01`, `BIZ02`, `BIZ03`, `ENG06`, `ENG04`, `AI13`, `OPS03`, `OPS04`, `OPS05` | 账单/数据隔离与成本控制的合成测试，无付费证明不得商业升级 |
| [AI 产品效果与增长掉队](ai-product-metrics.md) | `python tools/learning_router.py scenario ai-product-metrics` | `DATA01`, `DATA02`, `DATA03`, `AI11`, `AI13`, `PM09` | 埋点字典+分母+预注册指标+反事实分析 |

**使用**：先确认问题是否真实、授权和商业风险，再运行 CLI 找主 Gap、直接依赖和权威资料。继续阅读 [学习契约](../learning/task-contract.md) 与 [生产门禁](../launch/production-readiness.md)。场景映射原始数据：[scenarios.json](scenarios.json)。
