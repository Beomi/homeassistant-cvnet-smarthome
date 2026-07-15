# Repository Guidelines

## Project Structure & Module Organization

The integration lives in `custom_components/cvnet/`. Platform modules such as `light.py`, `climate.py`, and `config_flow.py` connect Home Assistant to code under `lib/`. Keep protocol code in `lib/api/` and `lib/client/`, data objects in `lib/model/`, and entities/coordinators in `lib/homeassistant/`. User-facing strings belong in both `translations/en.json` and `translations/ko.json`. Metadata and CI configuration live in `manifest.json`, `hacs.json`, and `.github/workflows/`.

There is currently no committed `tests/` directory or packaged build configuration.

## Build, Test, and Development Commands

- `python -m compileall custom_components/cvnet` checks all Python files for syntax errors.
- `hass --script check_config -c /path/to/ha-config` validates a Home Assistant configuration after installing this integration into `<ha-config>/custom_components/cvnet/`.
- `hass -c /path/to/ha-config` starts a development Home Assistant instance for config-flow and entity testing.

Pushes and pull requests run HACS validation and hassfest. Confirm both pass before merging. There is no separate build step.

## Coding Style & Naming Conventions

Use four-space indentation, type hints, and asynchronous Home Assistant APIs. Follow `snake_case` for modules, functions, and variables; `PascalCase` for classes; and `UPPER_SNAKE_CASE` for constants. Keep platform modules thin and reusable behavior in the appropriate `lib/` layer. Preserve translation keys across both locale files. No formatter or linter is configured, so keep changes PEP 8-compatible.

## Testing Guidelines

Add future pytest coverage under `tests/`, with files named `test_*.py`. Mock CVnet HTTP and WebSocket traffic; never require a real apartment account. Exercise config-flow failures, coordinator updates, entity mapping, and unload cleanup. Until a harness is added, run the checks above and manually verify affected platforms.

## Commit & Pull Request Guidelines

Recent commits use short, imperative, sentence-case subjects such as `Implement visitor photo feature` and `Fix unloading cleanup issue`. Keep each commit scoped to one behavior; mark breaking architectural changes clearly, following the existing `BC:` precedent.

Pull requests should explain the user-visible change, list validation performed and the Home Assistant version tested, and link related issues. Include screenshots for config-flow or entity UI changes. Update both translations and documentation when behavior or supported devices change.

## Security & Configuration

Never commit CVnet usernames, passwords, session tokens, raw API captures, apartment identifiers, or visitor images. Redact logs and fixtures before sharing them.
