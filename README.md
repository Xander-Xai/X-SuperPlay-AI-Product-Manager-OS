# X-SuperPlay AI Product Manager OS

**AI Product Manager × AI Product Engineer：知识全景、需求驱动学习、真实交付能力**

> v0.3.0 · 2026-11-14 · CURRICULUM_DESIGNED / PRACTICE_NOT_RUN / HUMAN_UNASSESSED。**知识覆盖完整不等于已经学会，仓库文档 CI 通过不等于任何产品已上线。**

## 核心学习观

**不是课程从 0 → 1 → 2 机械刷完。** 完整知识关系图告诉你学什么、为什么、彼此怎么关联；当真实需求出现时，只定位必要知识和缺口，读权威资料、做最小实验、用独立负例验收。知识内容能覆盖真实上线所需能力，却不要求学习仓变成某个下游项目仓。

## 最新 V3：一张知识地图 + 实际问题直达 + 专业/白话对照

**认知目标**：看到整个产品生命周期、四类产品风险、管理/财务/销售/Founder/行业知识之间的逻辑；**执行目标**：今天哪里不会就先学哪里，用理论与实际反例建立能力。

[专业×大白话入门](docs/atlas/product-manager-primer.md) · [四张可渲染关系图](docs/atlas/product-lifecycle-mermaid.md) · [上游 22 组真实资料路径](resources/upstream-pm-knowledge-index.md) · [非线性学习 SOP](docs/learning/point-to-system-method.md)。

## 四个入口

| 你现在要做什么 | 入口 |
|---|---|
| 看完整知识结构、作用与先修逻辑 | [ROADMAP：全景知识路线](ROADMAP.md) / [知识图谱](docs/atlas/knowledge-graph.md) |
| 卡在一个问题，直接查学什么 | [需求驱动 Router](docs/learning/demand-router.md) / `python tools/learning_router.py search "越权"` |
| 找到具体权威资料与可执行实操 | [知识卡手册](docs/atlas/knowledge-handbook.md) / [官方资料索引](resources/official-resources.md) |
| 想证明学完能做真正可运营的产品 | [上线 Gate](docs/launch/production-readiness.md) / [E1–E8 生产实训](docs/launch/production-apprenticeship.md) / [场景矩阵](docs/scenarios/README.md) |

## PM / PE 双主线

| AI Product Manager (PM) | AI Product Engineer (PE) |
|---|---|
| 用户、问题、替代/价值、PRD、交互、指标、买方、定价、产品风险、技术取舍 | API/UI/SQL/鉴权、LLM/RAG/Agent、Context/Harness、安全、可观测、部署、回滚、独立排错 |
| 产品为何做、如何判断有效、何时停止 | 产品如何可靠实现、如何恢复与演进 |
| 概念要能独立判断，但不要求亲自训练全部模型 | 技术要有可复现证据，仍需理解用户价值与成本 |

## 使用示例（离线，不调用模型 API）

```bash
python tools/learning_router.py list
python tools/learning_router.py search "重复写入"
python tools/learning_router.py route ENG06 --deep
python tools/learning_router.py scenario solo-ai-site
python tools/learning_router.py validate
```

首选场景：[知识助手](docs/scenarios/rag-knowledge-assistant.md) · [Agent审批](docs/scenarios/agent-approval.md) · [个人 AI 网站](docs/scenarios/solo-ai-site.md) · [收费 AI SaaS](docs/scenarios/paid-ai-saas.md) · [效果增长](docs/scenarios/ai-product-metrics.md)。

## 动手练习（纯标准库，无需模型 API）

[3 套离线可执行 Lab](labs/README.md)：RAG 证据/版本/权限、Agent 审批/幂等、产品指标与每成功任务成本；教学 baseline ≠ 生产系统。保留可选 [PM 12 周复盘坐标](docs/learning/optional-cadence.md)，不强制按周学。

## 已有的 12 个课程目录（保留，可按需跳转）

[基础](01-Foundations/README.md) · [研究](02-User-Research/README.md) · [战略](03-Product-Strategy/README.md) · [产品设计](04-Product-Design/README.md) · [AI PM](05-AI-Product-Management/README.md) · [交付](06-Product-Delivery/README.md) · [数据增长](07-Analytics-Growth/README.md) · [商业](08-Commercialization/README.md) · [PE](09-Product-Engineering/README.md) · [Capstone](10-Projects/capstone.md) · [职业](11-Career-Interview/README.md) · [独立考核](12-Assessments/rubric.md)。

## 上游与下游边界

- **技术上游**：[X-SuperPlay-AI-Learning-OS](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS)（Private）；RAG/Agent/LLM、全栈、Context/Harness 深层教程继续由上游维护。
- **本仓**：AI PM/PE **产品知识地图、按需学习路由、实战任务/验收、上线必备知识**。
- **真实工程/下游**：实现、部署和运行证据保留具体工程仓；Career OS 和 OPC 分别管理真实岗位与商业事实。

[跨仓索引与源知识桥](resources/upstream-downstream-index.md) · [从上游迁移的来源记录](resources/source-migration-map.md) · [治理协议](GOVERNANCE.md) · [知识库维护准则](CONTRIBUTING.md)。

**Public 仓库：严禁提交私密 JD、简历、客户/合同/订单、个人信息与密钥。**
