# pygame-lessons

> **Draft — needs teacher review.** Drafted 2026-04-22 and not yet reviewed. At the start of the next session, remind the user to review and refine this file, then remove this banner.

---

Small pygame projects for teaching middle- and high-school students (ages ~10–17) who have done basic Python (usually `turtle`), maybe text-based games or Scratch. Assume a 12-year-old is reading the code.

## Concepts in play

Always available: variables, constants, `if`/`else`, `and`/`or`, `while`/`for`, lists, functions.

Gated (advanced students only, and only when the lesson explicitly covers it): classes and OOP. Do not use classes unless the teacher has said this lesson is about OOP.

## Dependencies

Vanilla Python + `pygame` only. Standard-library modules (e.g. `random`) are fine. No other third-party libraries.

## File conventions

- Naming: `<game>_part<N>.py`. Each part builds on the prior — keep the earlier code and its teaching comments intact; add to them.
- Top of file: banner comment with `# ===` borders, game name, part number, controls.
- Part 2+: include a `# ===== NEW IN PART N =====` summary block near the top, and mark each added block inline with `# ===== NEW IN PART N: ... =====`.
- Section dividers: `# --- Section ---` (major), `# -- subsection --` (minor).

## Code style

- Functions are fine when they genuinely help a student understand the code. Don't introduce them just for tidiness.
- No classes unless the lesson is explicitly about OOP.
- Constants `UPPER_CASE` (`WHITE`, `WINNING_SCORE`). Variable names descriptive (`paddle1`, not `p1`).
- File order: imports → `pygame.init()` → window / clock / colors / font → game objects and state → game loop → `pygame.quit()`.
- Game loop order: events → held keys → update → draw → `display.flip()` → `clock.tick(60)`.
- `pygame.Rect` for positions, `colliderect` for collisions.
- Repetition is often intentional. Don't DRY it up.
- `str(x)` over f-strings unless f-strings have been taught.

## Commenting style

Comments teach. Explain *why* and introduce pygame concepts in plain language. Keep inline reminders for easily-forgotten bits (e.g. `# (R, G, B) from 0-255` near a color, `# pygame.Rect(x, y, w, h)` near a Rect). Err toward more explanation than production code.

## What NOT to do

- Don't use classes unless the lesson is explicitly about OOP — classes are reserved for advanced students.
- Don't refactor lesson code into "cleaner" versions — no extracting functions from procedural code, no DRY'ing up repetition, no reorganizing the game loop.
- Don't use Python features the student hasn't seen: list comprehensions, f-strings, ternaries, dataclasses, type hints, walrus, decorators.
- Don't remove or condense teaching comments.
- Don't add features beyond the lesson's scope, even if obvious.
- Don't reach for advanced pygame APIs (`pygame.sprite.Group`, `pygame.math.Vector2`, custom events) unless the lesson calls for them.
- Don't create new lesson files unprompted — curriculum decisions come from the teacher.

## Polish vs core

Sprites, music, sound effects, particles, animated backgrounds are **optional polish**, not part of core lessons. Keep them out of main lesson files unless a lesson explicitly covers them.

## Lesson progression

- `pong_part1.py` — two-player Pong. Window, game loop, `Rect`, `key.get_pressed()`, `colliderect`, text rendering, scoring.
- `pong_part2.py` — win condition, post-point pause via `pygame.time.get_ticks()`, game over + restart. Introduces `KEYDOWN`, game state flag, timestamp pausing.
- `flappybird_part1.py` — Flappy Bird. Lists of objects, `for` loops over lists, `append`/`pop`, gravity, `random.randint`, frame-counter timer.
