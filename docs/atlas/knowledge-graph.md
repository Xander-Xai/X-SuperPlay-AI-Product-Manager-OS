# 知识图谱：为什么知识点相互关联（不是时间顺序）

**V3 完整跨域可视化**：[产品闭环、四风险、知识网络、需求路由四张图](product-lifecycle-mermaid.md) · [专业定义与大白话对照](product-manager-primer.md)。原有 AI/工程因果链继续保留，本次补入管理、采购、创始人、财务、营销与认知横向知识。

## 关系类型

- **depends**：为理解/安全操作必须有的底层概念（例如 ENG06 授权检查依赖 ENG03 接口和 ENG04 数据所有权）。
- **helps**：改善结果但不是硬先修（例如对 PM 来说，了解模型训练能帮助选型，但通常不必亲自训练基础模型）。
- **checks**：质量门禁，任何相关方案都要过（例如 AI11 Eval、ENG06 AuthZ、OPS06 发布）。
- **optional**：条件升级；单 Agent 失败且有证据后才考虑 AI09 多 Agent。
- **feedback**：真实失败会生成新的学习 Gap（OPS02 可观测 → AI03 检索/ENG08 可靠性 → 回归）。

## 四条关键逻辑链

**价值链**：PM02 用户任务 → PM03 行为证据 → PM04 替代方案 → PM05 买方/价值 → PM06 优先级 → PM07 PRD → DATA01 指标 → DATA03 实验 → BIZ01 价格。没有用户任务，仅会画高保真图不代表产品合理。

**AI 可信链**：AI01 LLM 约束 → AI03 RAG / AI05 工具 Agent → AI04 数据版本与授权、AI07 Context、AI08 Harness → AI11 金标评测 → AI12 安全 → PM09 可信 UX → OPS06 发布。只有模型能回答不是上线条件。

**工程链**：ENG01 HTTP → ENG03 API → ENG04 DB/事务 → ENG06 AuthZ → ENG07 异步状态 → ENG09 测试 → ENG11 环境 → OPS01 CI/CD → OPS02 Trace → OPS04 备份 → OPS06 发布。各个箭头是必要时补的因果知识，不要求同一天全部完成。

**商业链**：PM05 买方 → BIZ01 定价/采购 → BIZ02 单位经济 ↔ AI13 模型成功任务成本 → BIZ03 计费/退款 → DATA02 留存。先判断能否卖，再优化计算账单系统。

## 典型交叉依赖

1. **RAG 可信引用**：检索 AI03 + 数据版本 AI04 + 用户范围 ENG06 + 标注指标 AI11 + 交互呈现 PM09。
2. **Agent 可靠执行**：AI05 工具选择 + AI06 MCP 授权 + ENG07 幂等状态 + AI07 Context + AI08 Harness + OPS02 Trace + AI12 注入防护。
3. **Next.js 单体演进**：ENG02 UI + ENG03 API + ENG04 事务 + ENG06 授权 + ENG12 部署边界 + OPS01 迁移/回滚，参考 [架构演进](../launch/architecture-evolution.md)。
4. **真正可运营**：OPS06 不只由部署决定，还依赖产品 UAT PM07/PM09、AI11 回归、ENG10 Web 安全、OPS02 监控、OPS04 恢复、OPS05 数据生命周期与 BIZ02 长期成本。

## 依赖不等于执行顺序

- **问题先行**：用户报告跨租户泄露，直接做 ENG06 的前测/安全隔离（安全硬失败优先），不先学 40 个模块。
- **知识回溯**：如果“数据所有权”理解不清，再补 ENG04；如果会 SQL 不会接口权限，再补 ENG03。
- **知识迁移**：ENG06 授权会同时用于 RAG AI04、支付 BIZ03、Agent 工具 AI06，无需重复做三门课。
- **学习停止**：问题已被已证实的最轻方案解决，当前学习迭代可停止；保留全景图以便下次再查。

可运行的依赖查询：[学习路由 CLI](../../tools/learning_router.py)；机器结构：[knowledge-catalog.json](knowledge-catalog.json)。
