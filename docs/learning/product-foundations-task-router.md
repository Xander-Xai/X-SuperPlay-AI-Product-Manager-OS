# 产品经理基础：遇到什么问题就学哪个节点

> **不按先后顺序刷课**。对应 [完整知识目录](../atlas/knowledge-handbook.md)、[缺口审计](../quality/coverage-audit-20261114.md)、[角色术语](../quality/terminology-contract.md)。案例仅作教学样本。

| 你今天遇到的真实卡点 | 第一入口 | 要补再查 | 动手练习 / 可以独立证明什么 |
|---|---|---|---|
| 想进入某赛道，但不知道有多少市场 | PM24 | PM05,PM19 | TAM/SAM/SOM 区间及最敏感假设 |
| 只有几条访谈，想知道需求普遍程度 | PM25 | PM03,PM14 | 抽样方法及不具代表性的局限 |
| 想录用户访谈或把资料发给 AI | PM26 | OPS05 | 授权、最小留存、撤回与使用边界 |
| 客户说先做 MVP，担心 Demo 变技术债 | PM27 | PM13,ENG12 | 明确是 Prototype、POC、Pilot 还是生产 |
| 团队问 PM 和 PO 谁负责 Backlog | PM28 | PM16,PM06 | Scrum Product Goal 与 Backlog 的责任 |
| 功能做完仍验收不通过 | PM29 | PM07,ENG09 | 区分 AC、DoD、DoR 与发布 Gate |
| 客服十条反馈想都变新功能 | PM30 | PM03,PM11 | VoC 去重、具体用户行为与可否证需求 |
| 上线前领导和研发关注点冲突 | PM31 | PM16,PM17 | 同一问题的决策 Memo 与工程 ADR |
| 问用户“喜欢吗”但不知道是否好用 | PM32 | PM08,PM14 | 观察任务完成而非喜好自报 |
| 发布后用户根本不会操作 | PM33 | DATA05,PM20 | 新手 FAQ/Release Notes/支持责任 |
| 注册高但首次任务低 | DATA05 | DATA01,PM20 | 激活漏斗与首次价值 |
| 实验结果看着提高却不可信 | DATA06 | DATA03 | 随机化/SRM/早停检查 |
| 前后端报表任务数不同 | DATA07 | DATA01,ENG03 | Tracking Plan 与事件去重 |
| 市场上有用户却不知是否具备 PMF | BIZ13 | BIZ06,DATA02 | 用户持续价值/复购与反证 |
| 客户需要节省多少人工工时才能采购 | BIZ14 | BIZ07,BIZ02 | 客户 ROI/TCO 与卖方贡献毛利区别 |
| 模型上线后有一天突然变差 | AI15 | AI11,OPS02 | 匿名采样、回归对照、人工审查与回滚 |
| 新功能公布后销售和客服不愿推广 | MGT06 | PM18,PM33 | Product Ops 培训/变更管理 |
| 多语言/不同地区产品使用失败 | GO03 | PM08,ETH01 | 本地化/无障碍/规则差异负例 |

**最短路径**：`python tools/learning_router.py search "抽样"` → `python tools/learning_router.py route PM25`，只读一个主权威材料并完成练习；依赖只有在关 AI 前测失败时再回溯。

**非教学阻塞**（客户不付钱、权限不明确、缺渠道、缺招聘资格）不能通过多学框架自动解决，先处理 H/E/S/C 分类。
