# AI 产品 Eval、风险与发布门禁

> 本页是方法，未运行任何模型或实际客户评测；阈值须由业务风险和样本决定，不能把示例数字写成成绩。

## 四层指标

1. **用户成果**：在限定时间内完成任务的比例、人工接管率、恢复成本；分清真实/合成用户。
2. **模型与检索**：回答是否有证据、RAG 召回/nDCG/引用支持与拒答正确率；Agent 任务成功和工具动作安全。
3. **系统**：端到端 P50/P95、错误/超时、权限隔离、幂等、重试、停机与恢复。
4. **经济性**：每请求成本及**每成功任务成本**，包含模型、检索、重试、人工审核、基础设施和售后。

指标须附分母、样本来源、金标版本、标注协议和不确定性；模型自述“正确”不是金标。

## 最小负例（至少选择两条预注册）
- 资料缺失或过期：不能捏造答案/引用。
- 未授权用户/租户访问：必须拒绝，不泄露。
- Prompt Injection：不得覆盖系统限制或触发越权工具。
- 模型超时、非法 JSON、工具故障：有降级/人工接管。
- 重试/多次点击：不得重复支付/写入；高风险动作需人工审批。
- 模型/Prompt/知识版本更新：同一回归集能重跑，差异可追溯。

发布前须有人签核、基线对照、风险与权限审核、可撤销开关、成本/时延上限、失败回退。参考 [OpenAI 评测最佳实践](https://developers.openai.com/api/docs/guides/evaluation-best-practices)、[Google PAIR](https://pair.withgoogle.com/guidebook-v2/)、[NIST](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)；练习用 [Eval 模板](../templates/Eval.md)。
