# 大代码库理解工具本地配置记录

本仓库将 GitNexus 作为默认图谱索引和 MCP 入口，将 Repomix 作为仓库快照打包工具。Serena、Sourcebot、CodeGraphContext、Claude Context 与 Gitingest 暂不默认常驻启用，避免给 Codex 启动和渲染增加额外负担。

## 已配置工具

- GitNexus：已安装全局命令 `gitnexus.cmd`，版本为 `1.6.4-rc.66`。Codex MCP 配置位于 `C:\Users\deepmind666\.codex\config.toml`，入口为 `gitnexus mcp`。稳定版 `1.6.3` 在当前 Node.js 24 环境下可显示版本与帮助，但 `analyze` 在最小测试仓库上静默失败，因此暂用官方 `rc` 版本。
- Repomix：已安装全局命令 `repomix.cmd`，版本为 `1.14.0`。用于生成仓库快照，不作为常驻服务。

## Codex MCP 配置

```toml
[mcp_servers.gitnexus]
command = "cmd"
args = ["/c", "C:\\Users\\deepmind666\\AppData\\Roaming\\npm\\gitnexus.cmd", "mcp"]
```

修改前已备份 Codex 配置文件。若 Codex 启动后未显示 GitNexus MCP，重启 Codex 或新开会话后再检查。

## 使用建议

对小范围问题先使用 `rg` 和直接读文件。对陌生大仓库，先执行 `gitnexus analyze <repo>` 建立索引，再用 GitNexus MCP、`gitnexus query`、`gitnexus context` 或 `gitnexus impact` 定位相关文件。当前 `lkr_ai_tool` 已建立 GitNexus 索引；由于该仓库以 Markdown skill 文档为主，图谱节点数可能较少，结论仍应以原文件阅读为准。对需要交给其他 agent 的仓库快照，使用 Repomix 生成一次性输出，完成后不要把 `repomix-output.*` 纳入版本控制。

## 参考来源

- GitNexus: https://github.com/abhigyanpatwari/GitNexus
- Repomix: https://github.com/yamadashy/repomix
- Serena: https://github.com/oraios/serena
- Sourcebot: https://github.com/sourcebot-dev/sourcebot
- CodeGraphContext: https://codegraphcontext.github.io/
- Gitingest: https://github.com/cyclotruc/gitingest
