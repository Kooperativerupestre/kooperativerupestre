<div align="center">

![](https://capsule-render.vercel.app/api?type=waving&color=0:6d0e0e,50:5a1a5a,100:3d0e5c&height=180&section=header&text=Ko%C3%B6perative%20R%C3%BCpestr%C3%ABn&fontSize=42&fontColor=E8E8E8&animation=fadeIn&fontAlignY=40)

**Backend developer · Python · PostgreSQL · C++ · Go**

Enzo Gonçalves. Self-taught. Looking for my first backend role, remote.
Based in Brazil (UTC−3) · [domicuslucinox@gmail.com](mailto:domicuslucinox@gmail.com)

![Python](https://img.shields.io/badge/Python-2b2b2b?style=flat-square&logo=python&logoColor=8B3A4A)
![C++](https://img.shields.io/badge/C%2B%2B-2b2b2b?style=flat-square&logo=cplusplus&logoColor=8B3A4A)
![Go](https://img.shields.io/badge/Go-2b2b2b?style=flat-square&logo=go&logoColor=8B3A4A)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-2b2b2b?style=flat-square&logo=postgresql&logoColor=8B3A4A)
![SQLite](https://img.shields.io/badge/SQLite-2b2b2b?style=flat-square&logo=sqlite&logoColor=8B3A4A)
![Redis](https://img.shields.io/badge/Redis-2b2b2b?style=flat-square&logo=redis&logoColor=8B3A4A)
![Docker](https://img.shields.io/badge/Docker-2b2b2b?style=flat-square&logo=docker&logoColor=8B3A4A)
![Linux](https://img.shields.io/badge/Linux-2b2b2b?style=flat-square&logo=linux&logoColor=8B3A4A)

</div>

---

## About

I build backends where correctness matters more than features: data integrity enforced by the database, safe behavior under concurrent requests, and clear boundaries between layers.

I also write C++ to understand what runs under the abstractions: memory, ownership, and data structures.

---

## Projects

### [Schedule Manager](https://github.com/Kooperativerupestre/Schedule-manager)

Multi-tenant appointment scheduling API. Python · FastAPI · PostgreSQL · Redis · Docker.

**The problem:** two clients must never book the same slot, even when requests arrive at the same moment.

**Architecture**

```mermaid
flowchart LR
    Router --> Service --> Log --> Verify["Verify Capabilities"] --> Repository --> DB[(Database)]
```

**Decisions**
- Overlaps are rejected by a PostgreSQL `GIST` exclusion constraint, not by application code, so concurrent requests cannot double-book.
- `psycopg3` (async) with raw SQL and no ORM. Queries stay explicit.
- Layered architecture with explicit transaction boundaries.
- Capability-based authorization. Cookie-based JWT authentication with Argon2 password hashing.

**Evidence**
- 50+ automated tests.
- The concurrency test runs multiple threads/connections against the same shared resources and checks that they do not produce race conditions.

### [Karkinolution](https://github.com/Kooperativerupestre/Karkinolution)

Creature ecosystem simulator. C++ · Docker. Creatures evolve through genetic mechanisms and act through a weighted decision-making model.

**The problem:** many independent creatures need to find their neighbors quickly, and new behaviors must be added without rewriting existing systems.

**Decisions**
- Organism state, perception, physiology, and behavior are separate models, so a new behavior does not touch the others.
- **R\*-tree** and **octree** spatial indexes for neighbor queries instead of scanning every creature.
- Explicit ownership and lifetime management in C++.
- Automated tests and continuous integration.

<!--
Add the benchmark chart here once it exists:
![R*-tree vs brute force](./assets/rtree-benchmark.png)
-->

### [XanboX](https://github.com/Kooperativerupestre/XanboX)

A sandbox for running commands in a virtual environment. Go (async) · Docker. In development.

**Planned**
- More explicit error handling
- Resource control
- More explicit state control
- Idempotency using hashes
- Continuous updates with logs

---

## How I use AI

I use AI to explore options, generate and expand tests, and review code. Architecture, correctness, and validation stay my decisions.

---

## Contact

- Email: [domicuslucinox@gmail.com](mailto:domicuslucinox@gmail.com)