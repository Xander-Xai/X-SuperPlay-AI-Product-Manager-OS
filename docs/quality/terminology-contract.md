# 产品管理术语与状态一致性公约（唯一语义入口）

> 2026-11-14。以 SVPG、Scrum Guide、NN/g、Strategyzer 与测试/工程官方资料为参考。此文件用于统一跨文档**含义**，不宣称所有机构只允许一种组织方式。

## 角色不是同义词

| 术语 | 专业含义与决策范围 | 常见误用（应避免） |
|---|---|---|
| Product Manager（PM） | 以用户价值、商业可持续性、战略/范围和结果为核心，和设计、工程共同发现/交付；责任会随企业组织变化 | PM 等于 Jira 工单管理员、原型绘图员或所有技术风险的唯一责任人 |
| Product Owner（PO，Scrum） | 按 [Scrum Guide](https://scrumguides.org/scrum-guide.html?lang=en) 为产品价值最大化和有效管理 Product Backlog 负责；与 Product Goal 及条目排序相关 | 任何 PM 都自动等于 Scrum PO；PO 一个人决定开发技术方案 |
| Project Manager（项目经理） | 组织范围、进度、预算、依赖、风险和交付协调 | 把“完成进度”当已验证用户价值 |
| Product Designer | 交互、研究与体验可用性的重要责任方 | 只负责美化页面或所有研究均由其独自做 |
| Product Engineer / Tech Lead | 保障技术方案可构建、可运维、可安全演进，参与早期产品发现 | 可以因为代码可运行而宣布商业成功 |
| Product Ops | 产品团队的数据、研究、知识和协作运作机制 | DevOps / IT 运维、后台生产事故监控 |

**SVPG 的四大风险**：Value（用户会用/会买吗）、Usability（能用好吗）、Feasibility（在约束下可做吗）、Viability（业务/合规/成本能持续吗）。**角色分工因组织而异**，不能把四类风险拆成四个永久孤立岗位。[原作者论述](https://www.svpg.com/four-big-risks/)。

## 不同方法/交付物的边界

| 名称 | 定义 | 不等于 |
|---|---|---|
| Discovery | 以用户和证据决定做什么、风险是否值得承担的持续活动 | 只在项目开始前做一次访谈 |
| Delivery | 构建、测试、部署、维护能实现结果的增量 | 只有编程没有 UAT/运维 |
| Prototype | 方便学习/验证体验或行为的模型，可以是无代码 | 已经可长期运营的正式产品 |
| Technical POC | 技术上是否可能/关键依赖能否实现的验证 | 用户愿意买或产品满足所有需求 |
| MVP | 尽可能低成本地验证关键价值/商业假设的可使用方案 | 功能不完整的生产系统或者所有 Demo |
| Pilot | 范围、客户和风险受控的小规模真实/合成试点；须标来源 | 全面生产交付或已达 PMF |
| Production | 获授权的实际运行、权限、监控、备份、支持和恢复环境 | CI 绿灯、Docker 容器启动 |
| PRD | 用户任务、范围、行为和可验证需求的协作契约 | 项目管理日历 |
| Acceptance Criteria（AC） | 单条用户故事或需求何时满足的具体条件 | Definition of Done |
| Definition of Done（DoD） | 增量可被认为完成的共同质量标准；Scrum 有正式定义 | 发布 Gate、每条需求特殊条件 |
| Definition of Ready（DoR） | 团队选用的开工准备检查实践 | Scrum 2020 的强制事件/工件 |
| UAT | 产品需求的使用方/业务验收 | 仅单元测试或 AI 自动评测 |
| Market Validation | 经过授权的使用/行为/买方/付款证据 | 模拟问卷、评论点赞或销售线索 |
| Business Model Canvas（BMC） | 对价值创造/交付/获取的九要素假设地图 | 有真实现金收入 |
| Go-to-Market（GTM） | 定位、定价、渠道、销售、支持等上市协作 | 只发一条宣传帖 |

## 数据与财务口径

- **注册不等于激活**：Activation 应是首次取得用户可验证价值。
- **输出不等于结果**：Output 是交付功能/文章，Outcome 是用户或业务价值的变化。
- **Retention/PMF**：重复有效行为与经济性证据随时间观察；单次点赞或一个 NPS 不证明产品市场契合。
- **实验 SRM**：分组流量异常必须排查；“显著性”需要固定随机化单位/样本/停止规则/置信区间，不是百分比看涨就算通过。
- **TAM/SAM/SOM**：市场总机会、可服务机会和可获得机会估计，不能自动等于已有买家或年收入。
- **贡献毛利≠净利润≠现金流**：成本项、收入确认和回款时间分开，未知值为 UNKNOWN。
- **用 AI/人审/客户/工程证据**各自不同：缺失即不能升级状态。

## 唯一状态契约（与 GOVERNANCE 同义）

- Engineering：NOT_RUN → RUN_WITH_EVIDENCE → VERIFIED。
- Human：UNASSESSED → PRACTICING → INDEPENDENT_PASS → TRANSFER_PASS。
- User：NOT_RUN → OBSERVED_WITH_CONSENT → VALIDATED_WITH_EVIDENCE。
- Commercial：NOT_VERIFIED → VERIFIED_BY_OWNER_REPO。

课程内容维度用 INDEXED/EXERCISE_DESIGNED/RUN_WITH_EVIDENCE 等作为**内容进度**，不能替代上述四轨；命名不同不意味着可提升商业证据。所有范例的客户、案例与金额必须标 SYNTHETIC 或公开研究。

## 推荐阅读

[Scrum Guide 官方 Product Owner/DoD](https://scrumguides.org/scrum-guide.html?lang=en) · [SVPG Four Big Risks](https://www.svpg.com/four-big-risks/) · [NN/g research ethics](https://www.nngroup.com/articles/informed-consent/) · [Strategyzer Experiment Library](https://www.strategyzer.com/library/experiment-library)。
