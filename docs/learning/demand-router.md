# 按需学习路由：不会哪里学哪里

**阅读法**：[专业定义/餐馆类比](../atlas/product-manager-primer.md) + [四张知识关系图](../atlas/product-lifecycle-mermaid.md) + [从点到面 SOP](point-to-system-method.md)；需要时查看 [上游学习资料链接](../../resources/upstream-pm-knowledge-index.md)。

## 最小路由（每次只挑一个主 Gap）

1. **写下当前任务或失败**：现象、期望行为、失败代价、来源、授权、真实/合成证据、截止期、可接受成本。
2. **分清阻塞类型 H/E/S/C**：硬资格/权限(H)、现有成果的证据或表达(E)、能力差(S)、渠道/协作约束(C)。只有真正的 **S** 自动进入课程；缺授权须停止，不可用学习绕过。
3. **定位图谱节点**：依据 [常见需求](../scenarios/README.md) 或运行命令，选择导致失败的**直接节点**。优先解决安全硬失败。
4. **补最低前置**：检查 directly requires；会解释/操作则跳过，不能则只补该依赖，不强制走 0→1→2。
5. **一项真实实验**：理论读1–2个权威页面 + 先做不使用 AI 的基线 + 正例/至少两个相关负例 + 执行与回归。
6. **独立验收**：闭卷、不依赖 AI 的陌生变式、固定代码/数据版本/命令、1/3/7 天迁移；AI 不给自己打 PASS。
7. **回到原需求**：技术技能学会仍可能不创造市场价值。区分 Engineering/Human/User/Commercial 四轨状态。

## CLI 操作（离线，不访问私仓/网络）

```bash
python tools/learning_router.py list
python tools/learning_router.py search "越权"
python tools/learning_router.py route ENG06
python tools/learning_router.py route ENG06 --deep
python tools/learning_router.py scenario rag-knowledge-assistant
python tools/learning_router.py scenario solo-ai-site
python tools/learning_router.py validate
```

`route` 默认只显示目标与直接依赖；`--deep` 显示完整概念依赖闭包，并区分需要学习的内容和已有能力。它不是自动给人的水平评分。报告引用 [权威索引](../../resources/official-resources.md)。

## 5 个实际例子

| 阻塞 | 路由首选 | 最小练习/客观成功条件 | 不应该做的事 |
|---|---|---|---|
| 有人说“我想做 AI 产品”但不明确场景 | PM02→PM03；必要时 PM04 | 两段有授权行为证据 + 反证条件 | 立即做 Agent SaaS |
| 需求改来改去无法验收 | PM07→ENG03/PM10 | PRD + Given/When/Then + 变更控制 | 继续扩产品范围 |
| RAG 旧版引用/权限错 | AI04+ENG06+AI11 | 旧版/跨租户/无证据三个负例 | 盲目换大模型 |
| 智能体重复写入/长任务死循环 | ENG07+AI08+OPS02 | 幂等/停止/审批/可恢复的合成工具测试 | 一上来升级多智能体 |
| 单体 Web 想迁 FastAPI/微服务 | ENG12+ENG04+ENG06+OPS01 | 接口边界、迁移图、数据回滚演练 | 为“架构更高级”而重写 |

## 任务输入模板

复制 [Task Contract](task-contract.md)。一次可处理一张需求卡：如果安全、隐私或真实用户证据不足，标出 UNKNOWN/NOT_RUN，保留清晰的下一步而不是虚构进度。

## 与上游的精确分工

本仓决定 **学什么、为解决哪个产品/交付问题、验收什么**。复杂技术原理（LLM 预/后训练、RAG 深度原理、LangGraph、Context/Harness）以 [上游 AI Learning OS](../../resources/upstream-downstream-index.md) 为专题权威。这里不复制用户私有职业/商业资料。

## 产品经理基础补缺快捷表

[按真实问题选知识](product-foundations-task-router.md) 提供市场规模、问卷抽样、用户研究授权、MVP/POC、Scrum Backlog/DoD、研究数据、用户激活、A/B 统计、产品发布与支持等入口。上游基础资料已链接，非必修课程表。若遇到越权/隐私、账务或数据丢失等硬门禁，优先处理安全与责任，不以“尚未学到这一章”为由放行。
