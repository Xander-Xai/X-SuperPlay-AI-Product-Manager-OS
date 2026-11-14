# PM × PE 独立能力量表

> ASSESSMENT_DESIGNED / HUMAN_UNASSESSED。机器静态校验不为人打分，AI 做完不等于本人掌握。

## 0–4 级
0 不会；1 在 AI 指导下能做；2 能独立解释/局部复现；3 **关闭 AI** 能独立设计、完成和排错；4 间隔 1–7 天变更陌生数据/业务/权限仍独立完成。关键技能 ≥3 且无安全硬失败才可标独立通过，迁移需相应能力达 4，由人类评审留痕。

| 领域 | PM 闭卷考题 | PE 闭卷考题 | 核心证据 |
|---|---|---|---|
| 用户价值 | 证明/否定 JTBD、替代品和买方 | 把模糊场景变成可测 UAT | 来源、反证、Stop Rule |
| 产品决策 | 资源收缩下做优先级和定价选择 | 比较人工/规则/RAG/Agent | ADR 与成本 |
| 体验交付 | PRD、异常与信任/接管状态 | 前后端/权限/回滚完整实现 | PRD、线框、正负测试 |
| AI 评测 | 指标、分母、风险与发布阈值 | 金标、拒答、检索、工具与独立排错 | 原始运行日志与版本 |
| 数据商业 | 留存/漏斗、单位经济口径 | 推理/重试/支持成本测量 | 可复算数字与假设等级 |
| 迁移 | 新买方/新约束下重新定义产品 | 关 AI 修陌生跨层 Bug | 原始答卷/复测日期 |

## 四轨不混淆
Engineering: NOT_RUN / RUN_WITH_EVIDENCE / VERIFIED；
Human: UNASSESSED / PRACTICING / INDEPENDENT_PASS / TRANSFER_PASS；
User: NOT_RUN / OBSERVED_WITH_CONSENT / VALIDATED_WITH_EVIDENCE；
Commercial: NOT_VERIFIED / VERIFIED_BY_OWNER_REPO。

**硬失败**：越权、数据泄露、擅自危险写入、虚构客户或收入、用 AI 自评冒充独立能力。公开仓只保留匿名试题/非敏感证据，原始客户、订单和求职事实留权威仓。
