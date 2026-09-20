<div align="center">

![](https://capsule-render.vercel.app/api?type=waving\&color=0:6d0e0e,50:5a1a5a,100:3d0e5c\&height=180\&section=header\&text=Ko%C3%B6perative%20R%C3%BCpestr%C3%ABn\&fontSize=42\&fontColor=E8E8E8\&animation=fadeIn\&fontAlignY=40)

**Backend developer · Python · C++ · Go**

Enzo Gonçalves · Self-taught · Brazil (UTC−3)
Looking for my first backend role · Remote

[domicuslucinox@gmail.com](mailto:domicuslucinox@gmail.com)

![Python](https://img.shields.io/badge/Python-2b2b2b?style=flat-square\&logo=python\&logoColor=8B3A4A)
![C++](https://img.shields.io/badge/C%2B%2B-2b2b2b?style=flat-square\&logo=cplusplus\&logoColor=8B3A4A)
![Go](https://img.shields.io/badge/Go-2b2b2b?style=flat-square\&logo=go\&logoColor=8B3A4A)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-2b2b2b?style=flat-square\&logo=postgresql\&logoColor=8B3A4A)
![Docker](https://img.shields.io/badge/Docker-2b2b2b?style=flat-square\&logo=docker\&logoColor=8B3A4A)
![Linux](https://img.shields.io/badge/Linux-2b2b2b?style=flat-square\&logo=linux\&logoColor=8B3A4A)

</div>

---

## About

I build software around **correctness, explicit boundaries, and testable invariants**.

I tend to start with:

> **What can go wrong, and where should that be prevented?**

---

## Projects

### [Schedule Manager](https://github.com/Kooperativerupestre/Schedule-manager)

Multi-tenant scheduling API.

**Python · FastAPI · PostgreSQL · Redis · Docker**

Problems solved:

* Prevent concurrent double-booking → PostgreSQL `GIST` exclusion constraint.
* Keep queries explicit → `psycopg3` + raw SQL, no ORM.
* Control access → capability-based authorization.
* Validate concurrency → 50+ tests, including concurrent requests.

---

### [Karkinolution](https://github.com/Kooperativerupestre/Karkinolution)

C++ ecosystem simulator focused on deterministic state and systems design.

**C++23 · CMake · Asio · GoogleTest · Docker**

Problems solved:

* Deterministic state mutation → `Physiology` × `Motor`.
* Avoid `O(n²)` spatial searches → R*-tree for static data, octree for moving data.
* Handle irregular TCP byte streams → custom binary protocol + deserializer.
* Keep HashMap + R*-tree consistent → service boundary + unit tests.
* Enforce code standards → CLI + formatting/lint/check tooling.
* Keep agents within project conventions → concise repository skills.
* Enforce bounded values → `LimitedValue` + 16 unit tests.

---

### [XanboX](https://github.com/Kooperativerupestre/XanboX)

Backend for executing code inside isolated Docker containers.

**Go · Docker · PostgreSQL**

Problems explored:

* Separate application IDs from Docker IDs.
* Model execution state explicitly.
* Capture stdout/stderr.
* Handle failures across database and Docker.
* Make lifecycle operations idempotent.

---

## How I Work

I prefer **invariants over conventions**, **explicit boundaries over hidden behavior**, and **tests that attack failure cases rather than only happy paths**.

---

## AI

I use AI for exploration, test generation, API research, and code review.

Architecture, trade-offs, and validation remain my responsibility.

---

## Contact

[domicuslucinox@gmail.com](mailto:domicuslucinox@gmail.com)
