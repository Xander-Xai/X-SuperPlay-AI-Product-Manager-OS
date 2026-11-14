# PM × PE 独立学习与上线验收量表

> RUBRIC_DESIGNED / HUMAN_UNASSESSED。**机器目录一致性通过 ≠ 人已经掌握 ≠ 任何产品已生产验证**。

## 人的知识能力 0–4

0 不会；1 AI 指导下能完成；2 可独立解释与部分复现；3 关 AI 独立完成、测试与解释权衡；4 间隔 1–7 日在陌生业务/数据/权限条件仍能独立迁移。**不按学习小时数/文档条目数加分**；只有实际证据及人工复核才升级。

## 课程内容分级

| 状态 | 说明 |
|---|---|
| INDEXED | 已有概念/逻辑依赖/官方资料/实操/证据出口 |
| EXERCISE_DESIGNED | 有明确输入输出、成功与至少两个失败用例 |
| RUN_WITH_EVIDENCE | 在隔离环境有真实运行版本/命令/结果 |
| HUMAN_INDEPENDENT | 本人关 AI 完成陌生用例，有人工复核 |
| TRANSFER_VERIFIED | 隔日更换约束仍通过 |
| PRODUCTION_EVIDENCE | 工程仓真实环境和上线 Gate 验证，非课程仓可自行宣称 |

## 四轨业务事实状态保持原有契约

- Engineering：NOT_RUN / RUN_WITH_EVIDENCE / VERIFIED。
- Human：UNASSESSED / PRACTICING / INDEPENDENT_PASS / TRANSFER_PASS。
- User：NOT_RUN / OBSERVED_WITH_CONSENT / VALIDATED_WITH_EVIDENCE。
- Commercial：NOT_VERIFIED / VERIFIED_BY_OWNER_REPO。

## PM/PE 关键实操

| 场景 | PM 独立测评 | PE 独立测评 | 必须保留的证据 |
|---|---|---|---|
| 用户要求做 AI | 反证 JTBD、替代/买方与 Stop Rule | 制定最轻实现与非 AI 基线 | 原始事实/假设分层 |
| UI/PRD 返工 | 用任务流程/错误态写可测需求 | 前端/API 契约与安全测试 | PRD、交互/UAT |
| RAG 过期/越权 | 设计可追溯拒答、评测分母和人工接管 | 金标、数据版本/权限与负例 | Eval 数据、版本、测试 |
| Agent 重复写入 | 设计审批/风险告知与恢复行为 | 工具权限、幂等、持久化、停止、Trace | 失败注入与恢复日志 |
| SaaS 经营成本 | 买方、定价与可证伪的单位经济 | Token/重试/支持成本与伸缩 | 可复算模型/实际证据 |
| 真正上线 | 真实/模拟 UAT 分级、客户支持与发布决策 | 干净环境、CI、AuthZ、监控、备份/回滚 | [G0–G7](../docs/launch/production-readiness.md) 门禁 |

**硬失败**：越权、隐私泄漏、未经审批危险写入、无恢复方案的不可逆数据更改、虚构客户/营收/个人能力。条件触发的风险管理需人工负责，不等于法规认证。
