# docker-manager.sh

**docker-manager.sh** is a professional Bash script to manage Docker projects efficiently. It provides commands for Docker login, build, push, pull, and Docker Compose management, all with a simple and consistent interface.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Features

- Initialize project configuration
- Docker login automation
- Build, pull, and push Docker images
- Start, stop, create, close, and recreate containers using Docker Compose
- Supports custom environment files
- Default configuration stored in `docker-manager.json`
- Colorful, user-friendly terminal interface

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/mateocallec/docker-manager.sh.git
cd docker-manager.sh
```

2. Make the script executable:

```bash
chmod +x docker-manager.sh
```

3. Ensure dependencies are installed:

- Docker
- Docker Compose
- `jq` (for JSON configuration)

---

## Usage

```bash
./docker-manager.sh <command> [--env-file <path>]
```

If no command is provided, the script will prompt you for one.

### Available commands:

| Commande   | Description                                 |
| ---------- | ------------------------------------------- |
| `init`     | Initialize Docker username and project name |
| `login`    | Log in to Docker registry                   |
| `pull`     | Pull Docker image                           |
| `push`     | Push Docker image                           |
| `build`    | Build Docker image                          |
| `create`   | Start containers (Docker Compose)           |
| `close`    | Stop containers (Docker Compose)            |
| `recreate` | Restart containers (close + create)         |
| `start`    | Start stopped containers                    |
| `stop`     | Stop running containers                     |
| `help`     | Display help message                        |


### Options:

| Option              | Description                                                            |
| ------------------- | ---------------------------------------------------------------------- |
| `--env-file <path>` | Specify a custom `.env` file for Docker Compose (default: `/dev/null`) |

---

## Configuration

The script uses a JSON configuration file: `docker-manager.json`.

Default configuration:

```json
{
  "registry-host": "registry-1.docker.io",
  "registry-port": 5000,
  "username": "user",
  "name": "my-project",
  "docker-compose": "docker-compose.yml",
  "dockerfile": "Dockerfile"
}
```

Use the `init` command to customize your username and project name.

---

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

Please ensure code follows Bash best practices and maintain readability.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Author

**Matéo Florian Callec**
GitHub: [mateocallec](https://github.com/mateocallec)

---

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for details.
