# 学习体系维护与验收约定

本仓按需求驱动增补知识，**全景图管覆盖，Router 管本次执行，真实项目管运行证据**。每个知识节点必须有 ID、作用、逻辑前置、权威资料 ID、可操作练习、可复核证据与触发场景。

- 修改 [knowledge-catalog](docs/atlas/knowledge-catalog.json) 时同步 [知识手册](docs/atlas/knowledge-handbook.md) / [图谱](docs/atlas/knowledge-graph.md) 的相应关系。
- 修改场景任务时同步 [scenarios.json](docs/scenarios/scenarios.json) 与场景文档；每次只建议一个主学习 Gap。
- 资源更新必须明确核验日期、官方来源与“页面已查/代码未跑”；文档链接不意味着可复制第三方授权内容。
- 不把 12 周、90 天计划当强制顺序；课程状态与个人、人审/用户/商业事实分别验收。
- 公共仓禁止个人 JD、简历、用户身份、密钥、客户订单和不具授权的数据；业务与工程证据须在事实权威仓核验。
- `python tools/learning_router.py validate`、`python tools/validate_repo.py`、`python -m unittest discover -s tools -p 'test_*.py' -v` 作为 CI 结构门禁；这些不会证明任何真实产品已上线。

## V4 内容一致性要求

- 新增知识节点，必须映射到 [18 领域覆盖矩阵](docs/quality/coverage-matrix.json)，否则 CI 应失败。
- 新增权威资料先查 [资料 ID/URL](resources/authorities.json) 是否已经存在；同 URL 的旧入口用 `alias_of` 兼容，不重复计数。
- 角色/风险/阶段/指标的语义以 [统一术语合同](docs/quality/terminology-contract.md) 为准。
- 新知识原则上要有**专业定义、通俗解释、触发条件、最小实验及负例**。旧卡允许渐进补齐，绝不因只是文档目录完整就宣称本人掌握。
- 审计与未来变更请维护 [缺口及验收记录](docs/quality/coverage-audit-20261114.md)。机器测试只证明目录结构与合成示例，不替代真实业务/学员证据。
