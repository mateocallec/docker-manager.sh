# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [1.0.0] - 2025-11-18

### Added

- Initial release of `docker-manager.sh`
- Core commands for Docker management:
  - `init` – initialize Docker username and project name
  - `login` – log in to Docker registry
  - `pull` – pull Docker images
  - `push` – push Docker images
  - `build` – build Docker images
  - `create` – start containers using Docker Compose
  - `close` – stop containers using Docker Compose
  - `recreate` – restart containers (close + create)
  - `start` – start stopped containers
  - `stop` – stop running containers
  - `help` – display usage instructions
- Configuration file support with `docker-manager.json`
- Support for custom environment files (`--env-file`)
- Colorful and user-friendly terminal interface
- Default configuration values for Docker registry, project name, Dockerfile, and Compose file

### Changed

- N/A (initial release)

### Fixed

- N/A (initial release)
