# Maintenance review — 2026-09-27

Scope: public blog index rendering and navigation.

The index previously inserted catalog text as HTML and had no search or tag filter. It now renders catalog values as text, accepts only HTTPS Medium links, and provides responsive search and tag filtering with a live result count.

Verification: an offline Node DOM harness passed safe-text rendering, HTTPS-link handling, search, tag filtering, and result-count checks. `git diff --check` passed.

The pre-existing edit to `posts/2026-07-13-open-source-vs-paid-frontier-llms/interactive.html` was preserved. No post content was changed or site deployed. Remaining gap: the page was not opened in a live browser.
