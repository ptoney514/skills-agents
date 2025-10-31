# Agent Library

This directory contains reusable agent definitions for use across projects with Claude Code.

## What Are Agents?

Agents are specialized AI assistants with specific expertise (e.g., React review, Supabase integration, code optimization). Unlike skills which are auto-loaded by Claude Desktop, agents are stored here as a reference library that you invoke manually when needed.

## Directory Structure

```
agents/
├── README.md              # This file
├── template/              # Template for creating new agents
│   └── AGENT.md
├── react-reviewer/        # Example: React code review agent
│   └── AGENT.md
├── supabase-expert/       # Example: Supabase integration agent
│   └── AGENT.md
└── code-optimizer/        # Example: Performance optimization agent
    └── AGENT.md
```

## Skills vs Agents

| Feature | Skills | Agents |
|---------|--------|--------|
| **Location** | `~/.claude/skills/` (symlinked) | This repo only |
| **Auto-loaded** | Yes, by Claude Desktop | No, manual invoke |
| **Use case** | Automation workflows | Specialized expertise |
| **Invocation** | Automatic based on context | Manual via Task tool |
| **Example** | Process Excel reports | Review React components |

## How to Use Agents

### Method 1: Invoke via Task Tool

When working in any project, invoke an agent using the Task tool:

```
I need a React code review. Please launch a Task agent using the prompt from
agents/react-reviewer/AGENT.md in my skills-agents repository.
```

### Method 2: Copy to Project

For frequently-used agents in a specific project:

1. Copy the agent's instructions to your project's `.claude/` directory
2. Reference in project CLAUDE.md
3. Agent will be auto-loaded for that project

### Method 3: Direct Reference

Simply ask Claude Code to read and use an agent:

```
Please read ~/Documents/Projects/skills-agents/agents/react-reviewer/AGENT.md
and review this component using those instructions.
```

## Creating a New Agent

1. **Copy the template:**
   ```bash
   cp -r agents/template agents/my-new-agent
   ```

2. **Edit AGENT.md:**
   - Update front matter (name, description, tags)
   - Write clear agent instructions
   - Add usage examples
   - Document dependencies

3. **Commit to Git:**
   ```bash
   git add agents/my-new-agent
   git commit -m "Add my-new-agent for [purpose]"
   git push
   ```

4. **Use across projects:**
   - Now available from this central repository
   - Pull latest version anytime with `git pull`

## Best Practices

### When Creating Agents

- **Be specific:** Focus on one domain/expertise area
- **Clear instructions:** Write detailed, unambiguous prompts
- **Version control:** Document changes in version history
- **Test thoroughly:** Verify agent works in real projects
- **Tag appropriately:** Use tags for easy discovery

### When Using Agents

- **Choose the right model:**
  - Opus for complex reasoning (architecture, refactoring)
  - Sonnet for balanced tasks (code review, implementation)
  - Haiku for quick tasks (formatting, simple fixes)

- **Provide context:** Give the agent relevant file paths and background
- **Iterate:** Refine agent prompts based on real-world usage

## Managing Your Agent Library

### Find agents by tag

```bash
grep -r "tags:" agents/*/AGENT.md
```

### List all agents

```bash
find agents -name "AGENT.md" -not -path "*/template/*" | xargs basename -s /AGENT.md
```

### Update from other machines

```bash
git pull  # Get latest agent definitions
```

### Archive old agents

```bash
mkdir agents/archive
mv agents/old-agent agents/archive/
git add agents/archive
git commit -m "Archive old-agent"
```

## Common Agent Types

- **Code reviewers:** React, Vue, TypeScript, Python, etc.
- **Framework experts:** Next.js, Supabase, Tailwind, etc.
- **Specialized tasks:** Performance optimization, security auditing, accessibility
- **Architecture:** Database design, API design, system architecture
- **Testing:** Unit tests, integration tests, E2E tests

## Version Control Benefits

- **Track improvements:** See how agent prompts evolve over time
- **Rollback:** Revert to older versions if needed
- **Collaborate:** Share agents across team members
- **Consistency:** Use same agent definitions across all projects
- **History:** Understand why changes were made

## Examples

See individual agent directories for specific examples of:
- React component review
- Supabase integration guidance
- Performance optimization
- And more as you build your library

## Contributing

When improving an agent:
1. Test the changes in a real project
2. Update version number and history in AGENT.md
3. Commit with descriptive message
4. Push to GitHub for access across all machines
