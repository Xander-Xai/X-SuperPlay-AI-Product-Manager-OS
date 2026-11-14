# 生产交付实训：从知识点到真正在线可用的系统

> 路径是**独立的教学实训项目方案**，不属于某个固定下游产品仓；不代表已经执行。你可以从任何被现实需求触发的模块开始，知识图谱解决前置不足。若无真实客户授权，一律使用合成数据；练习最终可以部署到自己授权的测试域名，但真实用户/付费仍需独立验证。

## 0. 学习目标及最小系统

用一个用户可操作的 Web 应用贯通前端、身份、API、SQL、AI 功能、质量评测、部署、监控和恢复：**浏览器 → HTTP(S) → Web/BFF → API → SQL → AI 可选 → 任务反馈 → 指标/Trace**。

允许技术实现 A：Next.js + PostgreSQL + AI adapter（模块化单体）；实现 B：React/Vue + FastAPI + PostgreSQL + AI adapter；两者均可演进为隔离 Worker/模型服务。**Java 非禁止项**，只在团队/生态/现有企业系统/约束提供具体依据时选择，不能将更高复杂度误作更接近生产。

## 1. 八项可独立启动的工程演练

| 演练 | 触发的现实问题 | 理论与官方资源 | 必须实际做 | 失败注入与证据 |
|---|---|---|---|---|
| E1 UI/需求闭环 | 只能 Demo，用户操作不完整 | PM07/PM08/ENG02；[Next.js Production](https://nextjs.org/docs/app/guides/production-checklist) | 编写 PRD，组件状态机、错误/空/等待/取消；本地 E2E | API 429/500、页面刷新与重复点击；录制步骤+测试 |
| E2 API/数据持久性 | 页面刷新丢数据、后端无法分层 | ENG03/ENG04；[MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)、[PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) | 设计 API/SQL 表、迁移脚本、事务失败回滚 | DB 不可用与唯一约束冲突；迁移 up/down 输出 |
| E3 鉴权与多租户 | 登录正常但其他账号能看到资料 | ENG06/ENG10/OPS05；[FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)、[OWASP 2025](https://top10.owasp.org/2025/0x00_2025-Introduction/) | AuthN/AuthZ 在服务端数据层执行，不信任前端传来的 owner | 用户 A/B 交叉读写、无效 token、角色变更，全部拒绝 |
| E4 RAG/Agent AI 功能 | AI 回答不可信、工具乱执行 | AI03/AI05/AI11/AI12；[OpenAI Eval](https://developers.openai.com/api/docs/guides/evaluation-best-practices)、[Anthropic](https://www.anthropic.com/engineering/building-effective-agents) | 在规则/检索基线上添加可替换 AI adapter + 数据版本/工具审批 | 无出处拒答、越权检索、注入诱导写入；金标+Trace |
| E5 长任务与恢复 | 网络断了，后台重复执行 | ENG07/ENG08/AI08；[LangChain Learn](https://docs.langchain.com/oss/python/learn) | 状态持久化、幂等键、任务进度、失败重试/退避 | 重复 webhook/队列消息、Worker 中断、重复操作无副作用 |
| E6 测试→部署 | 本机能跑，服务器无法重启/HTTPS 不通 | ENG09/ENG11/OPS01；[FastAPI Deploy](https://fastapi.tiangolo.com/deployment/concepts/)、[Docker](https://docs.docker.com/compose/how-tos/production/) | 版本锁定，CI 构建+集成测试、staging 环境、HTTPS/健康检查 | 缺环境变量/容器崩溃/升级失败，能回滚到固定 SHA |
| E7 观察与恢复 | 线上报错定位不了，数据恢复不确定 | OPS02/OPS03/OPS04；[OpenTelemetry](https://opentelemetry.io/docs/concepts/observability-primer/) | 请求 Trace、error rate/P95/cost 指标、备份还原与响应 Runbook | DB Down、模型超时/成本告警，恢复步骤和耗时记录 |
| E8 实际业务验收 | 能访问不等于可运营，也不等于用户愿意付费 | OPS06/DATA01/BIZ01/BIZ02；[PAIR](https://pair.withgoogle.com/guidebook-v2/) | 授权用户任务 UAT、反馈/支持/删除/成本、停机策略 | 无真实授权只能合成 UAT，必须明确四轨证据状态 |

**推荐操作**：不懂任何一个实战任务时，直接 `python tools/learning_router.py route ENG06`（替换 ID）；只读该卡需要的理论，再完成该行实际任务。不是必须把 E1→E8 都按顺序学完，但**对外上线发布必须审查相关 Gate**。

## 2. 运行环境建议（按真实约束替换）

- **本地**：Python 3.11+/Node LTS/PostgreSQL/Docker Compose；锁定具体软件版本并记录环境。若只做 PM/AI 选型实验可使用 Mock API/合成 CSV，无须开发完整系统。
- **Staging**：隔离 DB、Fake 付费/Mock 工具、合成语料、独立凭证；生产数据不能直接拷入测试环境。
- **Production**：获授权的域名、证书/HTTPS、受控密钥、最小权限、DB 备份/恢复计划、实际运维责任人及告警升级链。
- **依赖管理**：模型/供应商通过 adapter，表结构通过版本化迁移，权限由后端统一判定；不要把 Prompt 当授权机制。

不强制使用云 Kubernetes、微服务或 Java。**必要性来源是负载/团队/边界/审计，不能为了像“企业架构”而引入。**

## 3. 最少可复现的发布证据包

```text
Release-Evidence/
  scope.md             # 用户任务、范围、授权与非目标
  architecture.md      # 数据边界、API、权限、模型 adapter
  acceptance.md        # UAT 与失败清单
  eval/                # 金标、样本分母、模型/Prompt/知识版本及实测
  tests/               # 正负例、AuthZ、幂等、安全测试结果
  deployment.md        # 环境、固定 commit、构建、发布和 HTTPS 健康状态
  recovery.md          # 备份、恢复、回滚和告警责任人
  operations.md        # 日志、Trace、P95/成本、支持升级
  decision.md          # GO/HOLD/STOP 和人审签名
```

这是**应在真实工程项目仓生成的交付结构**，此学习仓不写入业务部署凭据或假日志。

## 4. 两种独立考试

- **工程独立**：关闭 AI，变更租户/数据版本或模拟一条重复工具消息，在干净环境诊断、修复、复现并解释为何通过门禁；原始记录由人工评分。
- **产品独立**：关闭 AI，出现“模型准确但每成功任务成本超预算/用户体验差”的新约束，选择降级/改产品/继续投资并提出可否证验证。不能靠模型答辩替代真人用户反馈。

## 5. 生产现实边界

本实训能帮助建立“从需求到可部署系统”的知识与实践能力，但不保证一个真实系统自动符合不同国家/地区的隐私、支付、行业准入或审计要求。对外公开服务时，应按所在地/用户数据/业务类型核验具体法规和合同义务，并由有责任的专业人员评审高风险部分。

延伸：[完整上线门禁](production-readiness.md) · [迁移与服务拆分](architecture-evolution.md) · [离线微实验](../../labs/README.md) · [场景矩阵](../scenarios/README.md)。
