# Modula Email

Identity-first Email module for Modula.

## Purpose

This package proves that a first-class module can expose:
- sidebar surfaces
- standalone host-routed pages
- a Board widget
- private capabilities and services
- host-controlled actions and workflows

Email is intentionally private by default. It supports communication and recovery flows without becoming the public identity model.

## Surfaces

- `/mail`
- `/mail/inbox`
- `/mail/sent`
- `/mail/drafts`

## Widget

- `recent-mail`

## Automation

- `mail.compose.open`
- `mail.send.submit`
- workflow `mail.compose.send`
