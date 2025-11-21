# MCP Setup Guide

This guide explains how to set up Model Context Protocol (MCP) servers for enhanced design system workflows with the Design Systems Engineer agent.

---

## What are MCPs?

**MCP (Model Context Protocol)** servers provide Claude with specialized capabilities through tool integrations. For design systems work, two MCPs are particularly valuable:

1. **Figma MCP** - Direct integration with Figma for reading/creating design files
2. **shadcn/ui MCP** - Streamlined component installation and configuration

**Important:** MCPs are **optional**. The Design Systems Engineer agent works effectively without them, but they enhance automation and speed.

---

## Prerequisites

Before setting up MCPs:

- Claude Desktop installed
- Node.js (v18 or higher) installed
- npm or pnpm package manager
- Basic terminal/command line knowledge

---

## MCP 1: Figma Integration

### What it Does

The Figma MCP allows Claude to:
- Read Figma files directly
- Extract design tokens (colors, typography, spacing)
- Analyze component structure
- Export design specifications

### Installation Steps

#### Step 1: Get Figma API Token

1. Go to [Figma Account Settings](https://www.figma.com/settings)
2. Scroll to "Personal Access Tokens"
3. Click "Generate new token"
4. Name it: "Claude Code MCP"
5. Copy the token (save it securely - you won't see it again!)

#### Step 2: Install Figma MCP Server

**Option A: Using official MCP server (if available)**

Check the [MCP Server Registry](https://github.com/modelcontextprotocol/servers) for official Figma MCP.

```bash
# If official package exists:
npm install -g @modelcontextprotocol/server-figma
```

**Option B: Community MCP server**

Search for community-built Figma MCP servers:
- Check npm registry: `npm search figma mcp`
- Check GitHub: search "figma mcp server"
- Check [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) list

#### Step 3: Configure Claude Desktop

Add to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-figma"],
      "env": {
        "FIGMA_API_TOKEN": "your-figma-token-here"
      }
    }
  }
}
```

**For Windows:** Config location is `%APPDATA%\Claude\claude_desktop_config.json`

#### Step 4: Restart Claude Desktop

Fully quit and restart Claude Desktop to load the MCP server.

#### Step 5: Verify Installation

In Claude Desktop, ask:
```
What MCP servers are available?
```

You should see "figma" listed.

---

## MCP 2: shadcn/ui Integration

### What it Does

The shadcn/ui MCP allows Claude to:
- Install shadcn/ui components with single commands
- Configure Tailwind dependencies automatically
- Scaffold new custom components
- Update component configurations

### Installation Steps

#### Step 1: Check for Official MCP

**As of now**, there may not be an official shadcn/ui MCP. Check:
- [MCP Server Registry](https://github.com/modelcontextprotocol/servers)
- [shadcn/ui GitHub](https://github.com/shadcn-ui/ui) for MCP mentions

#### Step 2: Alternative - Use Bash/Terminal MCP

If no dedicated shadcn/ui MCP exists, Claude can use the **terminal** to run shadcn commands:

```bash
npx shadcn-ui@latest add button
npx shadcn-ui@latest add card
```

This works well without a dedicated MCP.

#### Step 3: (If Official MCP Exists) Install and Configure

```bash
# Hypothetical installation (adjust based on actual package)
npm install -g @modelcontextprotocol/server-shadcn
```

Add to Claude Desktop config:

```json
{
  "mcpServers": {
    "shadcn": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-shadcn"]
    }
  }
}
```

---

## MCP 3: File System (Built-in)

Claude Desktop typically includes file system access by default. Verify you can:
- Read files
- Write files
- Edit files

This is essential for creating components and config files.

---

## Testing Your MCP Setup

### Test Figma MCP

In Claude Desktop:

```
Please use the Figma MCP to read this Figma file:
[paste Figma URL]

Extract the color palette and typography settings.
```

If successful, Claude will return design tokens from the file.

### Test shadcn/ui Workflow

```
Please install the Button component from shadcn/ui in my project at:
/path/to/your/project

Use the MCP if available, or run the CLI command.
```

---

## Troubleshooting

### Figma MCP Not Working

**Problem:** "Cannot connect to Figma"

**Solutions:**
1. Verify API token is correct
2. Check token has not expired
3. Ensure Figma file URL is accessible
4. Restart Claude Desktop

---

**Problem:** MCP server not found

**Solutions:**
1. Check `claude_desktop_config.json` syntax (valid JSON)
2. Verify MCP package is installed globally
3. Try absolute path to MCP server binary
4. Check Claude Desktop logs

---

### shadcn/ui Installation Issues

**Problem:** Components not installing

**Solutions:**
1. Ensure project has `package.json`
2. Verify Tailwind CSS is installed
3. Run `npx shadcn-ui@latest init` first
4. Check Node.js version (needs v18+)

---

### General MCP Debugging

**View MCP Logs:**

macOS/Linux:
```bash
tail -f ~/Library/Logs/Claude/mcp*.log
```

Windows:
```powershell
Get-Content "$env:APPDATA\Claude\Logs\mcp*.log" -Wait
```

**Test MCP Server Manually:**

```bash
# Run MCP server directly to see errors
npx @modelcontextprotocol/server-figma
```

---

## MCP Configuration Examples

### Minimal Config (File System Only)

```json
{
  "mcpServers": {}
}
```

File system access is built-in, no configuration needed.

---

### Figma Only

```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-figma"],
      "env": {
        "FIGMA_API_TOKEN": "figd_xxxxxxxxxxxxxxxxxxxx"
      }
    }
  }
}
```

---

### Full Design Systems Stack

```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-figma"],
      "env": {
        "FIGMA_API_TOKEN": "figd_xxxxxxxxxxxxxxxxxxxx"
      }
    },
    "shadcn": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-shadcn"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_xxxxxxxxxxxxxxxxxxxx"
      }
    }
  }
}
```

---

## When to Use MCPs vs Manual Workflow

### Use MCPs When:
- ✅ You work with Figma designs frequently
- ✅ You want automated design token extraction
- ✅ You need to sync design-code changes regularly
- ✅ You're building multiple design systems

### Skip MCPs When:
- ✅ You're doing a one-time design system setup
- ✅ You don't have Figma designs
- ✅ You prefer manual control over every step
- ✅ You're just learning design systems

**The agent works great either way!**

---

## Useful Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [MCP Server Registry](https://github.com/modelcontextprotocol/servers)
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)
- [Figma API Documentation](https://www.figma.com/developers/api)
- [shadcn/ui Documentation](https://ui.shadcn.com/)

---

## Security Best Practices

### API Tokens

- ✅ Use environment variables for tokens
- ✅ Never commit tokens to Git
- ✅ Rotate tokens regularly (every 90 days)
- ✅ Use separate tokens for different projects
- ❌ Don't share tokens in screenshots or docs
- ❌ Don't use tokens in public repositories

### Config File

```bash
# Make sure config file has proper permissions
chmod 600 ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

---

## Next Steps After Setup

Once MCPs are configured:

1. **Test the connection** - Verify each MCP works
2. **Invoke the agent** - Use the Design Systems Engineer agent
3. **Provide Figma files** - Share Figma URLs for token extraction
4. **Build components** - Let Claude automate component installation
5. **Iterate quickly** - Enjoy faster design-to-code workflows!

---

## Still Have Questions?

**MCP not working?** Try the manual workflow first - the agent is designed to work without MCPs.

**Need help with setup?** Ask Claude:
```
I'm trying to set up the Figma MCP but encountering [specific error].
Can you help me troubleshoot?
```

**Want to build your own MCP?** Check the [MCP SDK Documentation](https://modelcontextprotocol.io/docs/sdk).

---

**Remember:** MCPs enhance the experience but are **not required**. The Design Systems Engineer agent is fully functional with standard file operations and terminal commands.
