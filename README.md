# to.ci Portal
The easy portal to AI & MCP.

[![X][x-image]][x-url]
[![Code style: black][black-image]][black-url]
[![Imports: reorder-python-imports][imports-image]][imports-url]
[![Pydantic v2][pydantic-image]][pydantic-url]
[![pre-commit][pre-commit-image]][pre-commit-url]
[![License MIT][license-image]][license-url]

to.ci portal is the central hub for managing and accessing MCP services. This repo is the central repo of the portal to ease deployment of to.ci clones.

## Features of to.ci

* Centralized access to MCP services
* User authentication and authorization
* Service discovery and management
* Integration with DARPEngine for MCP server search
* Modern web interface

## Installation

```bash
# Clone the repository
git clone https://github.com/DARPAI/portal
cd portal

# Clone all the other repositories
git clone https://github.com/DARPAI/portal_backend/
git clone https://github.com/DARPAI/portal-gateway/
git clone https://github.com/DARPAI/darp_engine/ registry
git clone https://github.com/DARPAI/mailing-api/
git clone https://github.com/DARPAI/users-service/
git clone https://github.com/DARPAI/portal_frontend/

# Set up environment variables
cp .env.sample .env
# Edit .env with your configuration

# Start the services
python3 docker_compose.py up -d
```

## Project Structure

* `portal_backend/` - Portal backend
* `portal-gateway/` - Portal gateway
* `registry/` - Registry
* `mailing-api/` - Mailing API
* `users-service/` - Users service
* `portal_frontend/` - Portal frontend

## Getting Started

1. Start the services using `python3 docker_compose.py up -d`
2. Access the web interface at `http://localhost:3000`
3. Register and log in to access MCP services
4. Connect to MCP servers through the registry

## Development

Refer to individual service READMEs for development instructions.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Get Help and Support

Please feel free to connect with us using the [discussion section](https://github.com/DARPAI/portal/discussions).

## License

The to.ci portal codebase is under MIT license.

<br>

[x-image]: https://img.shields.io/twitter/follow/DARP_AI?style=social
[x-url]: https://x.com/DARP_AI
[black-image]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[imports-image]: https://img.shields.io/badge/%20imports-reorder_python_imports-%231674b1?style=flat&labelColor=ef8336
[imports-url]: https://github.com/asottile/reorder-python-imports/
[pydantic-image]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json
[pydantic-url]: https://pydantic.dev
[pre-commit-image]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-url]: https://github.com/pre-commit/pre-commit
[license-image]: https://img.shields.io/github/license/DARPAI/portal
[license-url]: https://opensource.org/licenses/MIT
