---
name: Agent Name
description: Brief description of what this agent does and when to use it (1-2 sentences)
model: sonnet  # Options: opus, sonnet, haiku
version: 1.0.0
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [react, typescript, code-review]  # Add relevant tags
---

# Agent Name

## Purpose

Describe the specific purpose of this agent and what problems it solves.

## When to Use This Agent

- Use when [specific scenario 1]
- Use when [specific scenario 2]
- Use when [specific scenario 3]

## When NOT to Use This Agent

- Don't use for [scenario where agent isn't suitable]
- Don't use for [another unsuitable scenario]

## Agent Instructions

```
[Full agent prompt goes here - this is what you'll paste when invoking the Task tool]

You are a specialized agent for [specific domain/purpose].

Your capabilities:
- [Capability 1]
- [Capability 2]
- [Capability 3]

Your workflow:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Important constraints:
- [Constraint 1]
- [Constraint 2]

Tools available to you: [list specific tools if relevant]
```

## How to Use

### Via Task Tool in Claude Code

```
I need you to launch a [Agent Name] agent to help with [task description].

Use the following prompt:
[Paste agent instructions from above]
```

### Via Copy/Paste to Project

1. Copy the agent instructions section above
2. Paste into your project's `.claude/` directory or project instructions
3. Invoke when needed during development

## Example Usage

**Scenario:** [Describe a real-world scenario]

**Task:** [What you want the agent to do]

**Expected Output:** [What the agent should produce]

## Configuration Options

- **model**: Recommended model (opus for complex reasoning, sonnet for balanced, haiku for speed)
- **thoroughness**: [if applicable] quick, medium, very thorough

## Dependencies

- Assumes codebase uses: [framework/language]
- Requires access to: [files/directories/tools]
- Works best with: [specific project structures]

## Version History

- **1.0.0** (YYYY-MM-DD) - Initial version
- [Future versions will be documented here]

## Related Agents

- [Link to related agent 1]
- [Link to related agent 2]

## Notes

- [Any additional notes, tips, or gotchas]
- [Common issues and solutions]
