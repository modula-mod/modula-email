# Mailbox Model

The Email module now documents the first real Modula mailbox model:

- `Mailbox`
- `Thread`
- `Message`
- `Draft`

The host runtime owns persistence and routing. The package metadata declares the capabilities, services, actions, events, and workflows that describe what the module can do.

## Routes

- `/mail`
- `/mail/inbox`
- `/mail/sent`
- `/mail/drafts`
- `/mail/compose`
- `/mail/thread/[id]`

## Capabilities

- `mail.read`
- `mail.compose`
- `mail.send`
- `mail.drafts.read`
- `mail.thread.read`

## Services

- `mail.inbox.v1`
- `mail.compose.v1`
- `mail.threads.v1`
