# 学习治理、事实边界与状态契约

## 单一权威源

| 事实 | 权威存放处 | 公开本仓允许内容 |
|---|---|---|
| PM/PE 产品能力训练、公开模板、案例推演 | 本仓 | 文档、合成数据和脱敏学习结构 |
| RAG/Agent/模型训练的技术内容 | AI Learning OS（可能是私有仓） | 公开版知识路径及跳转 |
| 真实代码、运行日志、CI、部署 | 对应工程仓 | 固定 commit/Issue 的公开引用 |
| 真实岗位、薪资、简历、面试反馈 | Career OS | 匿名技能 Gap，绝不复制私密资料 |
| 真实客户、付款、合同、经营阶段 | OPC Blueprint | 公开可披露的脱敏引用 |
| 周计划与个人能力取舍 | Personal OS | 学习策略摘要而非平行数据账本 |

**Public 安全边界**：不公开个人/企业私密资料、API key、客户身份、录音、生产配置、未授权数据。第三方代码/文档不可因本仓 MIT License 就默认有复制权；优先链接与原创总结，具体复用需检查许可证。

## 事实与结果状态

来源级别：REAL_WITH_CONSENT（需授权和原始凭证）、PUBLIC_RESEARCH、HISTORICAL_NEEDS_RECHECK、SYNTHETIC、UNKNOWN。未核验的职位不能写“正在招聘”，AI 模拟客户不能写成真实买方。

四轨严格分离：
- Engineering：NOT_RUN → RUN_WITH_EVIDENCE → VERIFIED。
- Human：UNASSESSED → PRACTICING → INDEPENDENT_PASS → TRANSFER_PASS。
- User：NOT_RUN → OBSERVED_WITH_CONSENT → VALIDATED_WITH_EVIDENCE。
- Commercial：NOT_VERIFIED → VERIFIED_BY_OWNER_REPO。

人的能力必须关闭 AI 做陌生题并由真实人评审。代码 CI、文章/模板数量、AI 自我评分、合成 ROI 都不能升级用户或商业状态。

## 每张实战卡的字段

来源 URL/修订/核验日期、授权状态、用户目标与替代方案、无 AI 基线、主技能缺口、验收指标与分母、两个失败反例、技术证据链接、闭卷独立答案、1/3/7 日迁移和 Stop 条件。没有证据时保持 NOT_RUN。

学习排序：已确认面试与履约 > 有授权的现实问题 > 原工程可复现缺口 > 历史参考 > 合成练习 > 追热点框架。
