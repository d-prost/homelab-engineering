# A subprocess consumed the caller's control stream

## Symptom

A wrapper script using a heredoc stopped progressing in a way that looked unrelated to the command being executed.

## Root cause

A subprocess inherited standard input even though it did not need it. The subprocess consumed bytes that belonged to the caller's control stream, so later shell input was no longer where the wrapper expected it to be.

This is easy to miss because the child command itself can still succeed.

## Correction

Detach standard input for subprocesses that are not supposed to consume the control stream.

The exact flag depends on the command. The rule is the useful part:

> a subprocess should not inherit control input it does not need.

## Lesson

When shell orchestration mixes heredocs, pipelines, SSH, container exec or nested commands, stdin ownership is part of the interface. Treat it explicitly rather than as an implementation detail.
