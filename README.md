# tiny-chess-engine-v2

A 4 KB chess engine in pure Python for the make.fun tiny-chess-01
competition. Second entry, rewritten from scratch for speed.

Design: 120-square mailbox board, make/unmake move execution with an undo
stack and incremental evaluation, negamax with alpha-beta, iterative
deepening under a fixed 20,000-node budget, quiescence with capture and
promotion search plus full check evasions, killer and MVV-LVA move
ordering, hand-written piece-square tables, and a root rule that never
plays the immediate reverse of the engine's previous move (to avoid
shuffling draws). Deterministic: no clock,
no randomness, no model calls.

The harness runs it against the trial environment at MAKEFUN_ENV_URL.
