# 跨仓知识责任与上下游索引（公共版）

> 本仓 Public；上游 AI Learning OS 当前 Private（2026-11-14 GitHub 权限核验），公开读者未必能访问，**不能在此仓复印上游私人材料**。这里仅给可公开的知识职责索引。

## 角色与边界

| 仓库 | 主职责 | 读写接口 |
|---|---|---|
| [X-SuperPlay-AI-Learning-OS](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS)（上游 Private） | 算法、训练、RAG、Agent、Context/Harness、全栈工程深层知识/实验 | 本仓根据需求路由到上游专题；上游返回独立技术考核和证据引用 |
| [X-SuperPlay-AI-Product-Manager-OS](https://github.com/Xander-Xai/X-SuperPlay-AI-Product-Manager-OS)（本仓 Public） | PM/PE 产品化知识图谱、需求驱动选学、产品/上线验收与商业判断 | 本仓提供学习目标、缺口 ID、产品证据和课程导航 |
| [X-SuperPlay-AI-Engineering-OS](https://github.com/Xander-Xai/X-SuperPlay-AI-Engineering-OS) | 真实工程任务与交付规范 | 真实代码、CI、Trace、部署记录归工程/具体项目仓 |
| [AI-Career-Interview-OS](https://github.com/Xander-Xai/AI-Career-Interview-OS) | 实际求职岗位、简历、面试真实性 | 本仓只存匿名的技能 Gap |
| [X-SuperPlay-OPC-Blueprint](https://github.com/Xander-Xai/X-SuperPlay-OPC-Blueprint) | 商业假设/试点、授权/客户与真实成交证据 | 客户与收入只由该仓升级 |
| [X-SuperPlay-Personal-OS](https://github.com/Xander-Xai/X-SuperPlay-Personal-OS) | 现实优先级/时间资源与复盘 | 只复用必要决策指针 |

## 精确知识桥接：本仓节点 ↔ 上游参考专题

| 本仓节点 | 上游学习专题（源路径为私有可见性约束） | 何时使用 |
|---|---|---|
| AI01/AI13/AI14 | `docs/career/llm-market-learning-roadmap-20261029.md`、LLM 训练/推理研究 | 成本/模型限制/微调决策无法解释时 |
| AI03/AI04/AI11 | `docs/career/market-driven-rag-roadmap-20261029.md`、RAG Track | RAG 检索/版本/评测失败时 |
| AI05/AI08/AI09 | `docs/tracks/project-driven/ai-native-agent-market-track-20261029.md` | Workflow/工具/状态恢复失败时 |
| AI07 | `docs/career/context-engineering-market-roadmap-20261029.md` | 上下文污染、版本、Token/记忆错误时 |
| AI08/AI12 | `docs/career/harness-market-learning-roadmap-20261029.md` | 长任务治理、工具权限、恢复与安全时 |
| ENG01–ENG14 | `docs/tracks/project-driven/ai-native-fullstack-track.md` | UI→API→DB/AuthZ/上线边界失败时 |
| OPS01–OPS06 | `docs/atlas/06-production.md` | LLMOps、部署、监控、回滚与安全时 |
| PM/PE 角色 | `docs/career/ai-product-engineer-roadmap-20261028.md` | 产品工程职业定位/基础能力复核时 |

本仓的课程与公共索引可以独立使用，不依赖访问私有 repo；源私人材料的版本与历史快照见 [迁移映射](source-migration-map.md)。

## 一次跨仓知识补充的操作规则

1. 在本仓记录产品需求/技能 Gap/所需产品行为；判断是否属于技术深钻。
2. 属技术原理则查上游对应专题，必要时回到上游补**算法与工程知识**；本仓只更新概念、触发、验收与权威资料指针。
3. 真实项目的 commit/test/日志不搬到本仓；以固定 SHA 的公开可分享证据做复核。
4. 不自动同步敏感岗位、买方、收入和个人信息，不将示例状态升级为真实交付事实。

**权威优先级**：事实权威仓 > 可重复工程/独立个人证据 > 公开研究 > 合成样本。仓库分工不等于访问授权。
