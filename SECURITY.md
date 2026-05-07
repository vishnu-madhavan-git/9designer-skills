# Security Policy

## Supported Scope

This repository contains Codex skill instructions, helper scripts, and documentation. Security reports should focus on:

- Unsafe or misleading workflow instructions.
- Asset-handling behavior that could expose private files.
- Prompt rules that encourage leaking secrets or credentials.
- Helper script behavior that can unexpectedly modify or delete user data.

## Reporting

Do not open a public issue for sensitive security concerns.

Use GitHub private vulnerability reporting if it is enabled for the repository. If it is not enabled, contact the maintainer through a private channel and include:

- A short summary.
- A reproduction path.
- Affected file or skill.
- Expected risk.
- Suggested fix, if known.

## Handling Secrets

Never include API keys, tokens, cookies, private repository URLs, or private reference images in issues, pull requests, examples, or generated assets.

If a secret is accidentally committed, revoke it immediately and open a maintainer-only report.
