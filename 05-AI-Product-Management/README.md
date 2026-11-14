# 05 AI Product Manager：技术理解与业务决策

**目标**：懂技术限制、商业代价和用户风险，而非要求所有 PM 自己训练基础模型。

| 能力单元 | PM 必问 | 典型测量与风险 |
|---|---|---|
| LLM 基础、Token、上下文 | 输出不确定性、模型可用性、数据隐私、成本如何影响产品 | 任务成功/错误、单位成本、P95 |
| Prompt 与结构化输出 | 规则/模板是否更好，输出格式如何验证 | 格式成功率、鲁棒性、注入 |
| RAG/Embedding/检索 | 用户需要外部证据吗？BM25/人工是否够用 | 召回、证据支持率、拒答与越权 |
| 工作流 / Agent | 规则路径固定还是模型动态决策，谁审批副作用 | 完成率、审批、重复操作、回滚 |
| 多模态 OCR/语音/视觉 | 上游识别错误如何传递，需哪些人工纠错 | 端到端正确率/交互成本 |
| 模型供应与部署 | API/自部署如何平衡质量、成本、时延、锁定风险 | TCO、SLA、安全/可移植性 |
| AI UX | 用户何时知道 AI 不可靠，如何纠错/接管 | 误用、信任校准、人工介入 |
| 产品经济 | 重试/审核/故障后每成功任务的真实成本 | 单成功任务总成本与贡献毛利 |

### 架构选型顺序

**NO_AI/人工 → 规则/搜索 → Prompt → RAG → 固定 Workflow → 单 Agent → 多 Agent**。每提高一层复杂度必须证明价值、质量或必要的灵活性足以抵消延迟、维护、安全与成本。选择结果形成 [ADR](../templates/ADR.md)。

### AI PRD 必填
用途/非用途、数据来源与授权、模型输入输出、不能回答的情况、出处、反馈与撤销、人工审批、版本与漂移、成本上限、评测集/负例、上线与回滚。详见 [Eval/Guardrails](eval-and-guardrails.md)，可复现系统由 [PE](../09-Product-Engineering/README.md) 实践。

### 学习资源
[Google PAIR](https://pair.withgoogle.com/guidebook-v2/) · [Anthropic Agents](https://www.anthropic.com/engineering/building-effective-agents) · [OpenAI Eval Best Practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) · [NIST GenAI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)。
