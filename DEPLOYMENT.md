# GitHub Pages 部署说明

本项目已配置好 GitHub Pages 部署，只需在 GitHub 仓库设置中启用即可。

## 启用步骤

### 方法一：通过 GitHub Actions 自动部署（推荐）

1. **合并 Pull Request**
   - 将此 PR 合并到 `main` 分支

2. **启用 GitHub Pages**
   - 进入仓库的 Settings（设置）
   - 在左侧菜单中找到 "Pages"
   - 在 "Build and deployment" 部分：
     - Source（源）选择：**GitHub Actions**
   - 保存设置

3. **等待部署完成**
   - GitHub Actions 会自动运行部署工作流
   - 在 Actions 标签页可以查看部署进度
   - 通常需要 1-2 分钟完成部署

4. **访问网站**
   - 部署完成后，网站将在以下地址可用：
   - `https://darrenhdc.github.io/youtube-crawler/`

### 方法二：从分支部署

如果你想先在分支上测试网站：

1. 进入仓库的 Settings → Pages
2. Source 选择：**Deploy from a branch**
3. Branch 选择：`copilot/create-website-for-project`
4. 文件夹选择：`/ (root)`
5. 保存后等待部署完成

## 已配置的文件

- `.github/workflows/pages.yml` - GitHub Actions 自动部署工作流
- `index.html` - 网站主页
- `style.css` - 样式文件
- `script.js` - 交互脚本

## 功能特点

✅ 自动部署：每次推送到 main 分支时自动更新网站
✅ 响应式设计：支持手机、平板、电脑访问
✅ 交互功能：代码一键复制、标签页切换
✅ 中文界面：完整的中文用户体验

## 故障排除

### 如果网站无法访问

1. **检查 GitHub Pages 设置**
   - 确认已在 Settings → Pages 中启用
   - 确认 Source 设置正确

2. **检查 Actions 工作流**
   - 进入 Actions 标签页
   - 查看是否有失败的工作流
   - 如有错误，查看日志详情

3. **权限问题**
   - Settings → Actions → General
   - 确认 "Workflow permissions" 设置为：
     - ✅ Read and write permissions
   - 或至少勾选 "Allow GitHub Actions to create and approve pull requests"

### 重新部署

如需重新部署，可以：
- 推送新的提交到 main 分支
- 或在 Actions 标签页手动触发 "Deploy to GitHub Pages" 工作流

## 自定义域名（可选）

如果你有自己的域名：

1. 在 DNS 服务商处添加 CNAME 记录指向：`darrenhdc.github.io`
2. 在 GitHub Pages 设置中添加你的自定义域名
3. 等待 DNS 生效（通常需要几分钟到几小时）

## 更新网站内容

要更新网站内容，只需：

1. 编辑 `index.html`、`style.css` 或 `script.js`
2. 提交并推送到 main 分支
3. GitHub Actions 会自动部署更新

祝你使用愉快！🎉
