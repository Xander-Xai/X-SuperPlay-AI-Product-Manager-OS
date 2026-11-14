# Lab：为什么 Agent 的工具调用必须经过审批、租户授权和幂等

> 对应 AI05、AI06、AI08、ENG06、ENG07、ENG08、OPS02。此 Lab **只有 Fake Tool 的规则状态机，没有真实 Agent/LLM、数据库或外部业务写入**。

## 关键理论

- **模型建议 ≠ 权限授权**：Prompt 决不能授予数据库写入权；服务端每次执行再次验证。
- **审批状态 ≠ 任务已执行**：PENDING/APPROVED/REJECTED 分开，拒绝态无任何副作用。
- **重试 ≠ 重复执行**：同一幂等键、同一请求返回同一结果；键相同但参数冲突应该拒绝。
- **长任务上下文 ≠ 可恢复状态**：本实验内存状态只能在单进程生效，真实系统还需持久化、事务及异常恢复。

## 执行

```bash
python -m unittest labs.agent_approval.test_workflow -v
```

## 失败注入与学习迁移

包含 7 个测试：未经审批执行、跨租户审批、非审批者审批、拒绝仍执行、重复消息双写、跨租户工具执行、幂等键碰撞。

请关闭 AI 做进阶实现：将审批状态与幂等记录改成**原子事务**，模拟进程重启与两个 Worker 并行提交；证明同时不会双写，失败时可恢复，并给出 Trace ID。不要把内存演示自称生产可用。

权威参考：[Anthropic Agent 设计](https://www.anthropic.com/engineering/building-effective-agents) · [MCP 2026 协议版本](https://blog.modelcontextprotocol.io/posts/2026-07-28/) · [OWASP](https://top10.owasp.org/2025/0x00_2025-Introduction/)。
