# Modula Email

Identity-first Email module for Modula.

## Purpose

This package proves that a first-class module can expose:
- sidebar surfaces
- standalone host-routed pages
- a Board widget
- private capabilities and services
- host-controlled actions and workflows
- thread and compose routes
- a mailbox data model suitable for inbox, sent, drafts, and thread views

Email is intentionally private by default. It supports communication and recovery flows without becoming the public identity model.

## Surfaces

- `/mail`
- `/mail/inbox`
- `/mail/sent`
- `/mail/drafts`
- `/mail/compose`
- `/mail/thread/[id]`

## Widget

- `recent-mail`

## Services

- `mail.inbox.v1`
- `mail.compose.v1`
- `mail.threads.v1`

## Automation

- `mail.compose.open`
- `mail.draft.save`
- `mail.send.submit`
- workflow `mail.compose.send`
- workflow `mail.draft.autosave`

## Fixtures

This package now ships sample fixtures under `fixtures/` so host renderers, docs, and test flows can use consistent mailbox/thread examples.

- `fixtures/sample-mailbox.json`
- `fixtures/sample-thread.json`
- `fixtures/sample-compose.json`

## Docs

- `docs/overview.md`
- `docs/mailbox-model.md`
- `docs/fixtures.md`
