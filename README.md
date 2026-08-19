<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6d0e0e,50:5a1a5a,100:3d0e5c&height=180&section=header&text=Kooperative%20Rupestren&fontSize=42&fontColor=E8E8E8&animation=fadeIn&fontAlignY=40" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=18&pause=1000&color=8E8E93&center=true&vCenter=true&width=560&lines=Backend+Architecture+%26+Data+Modeling;Concurrency%2C+Consistency+%26+Systems+Design" alt="typing-svg" />

</div>

---

## <span style="color:#8B3A4A">Technologies</span>

<div align="center">

<img src="https://img.shields.io/badge/Python-2b2b2b?style=flat-square&logo=python&logoColor=8B3A4A" height="32">
<img src="https://img.shields.io/badge/C%2B%2B-2b2b2b?style=flat-square&logo=cplusplus&logoColor=8B3A4A" height="32">
<img src="https://img.shields.io/badge/PostgreSQL-2b2b2b?style=flat-square&logo=postgresql&logoColor=8B3A4A" height="32">
<img src="https://img.shields.io/badge/Docker-2b2b2b?style=flat-square&logo=docker&logoColor=8B3A4A" height="32">
<img src="https://img.shields.io/badge/Linux-2b2b2b?style=flat-square&logo=linux&logoColor=8B3A4A" height="32">
<img src="https://img.shields.io/badge/Redis-2b2b2b?style=flat-square&logo=redis&logoColor=8B3A4A" height="32">

</div>

## <span style="color:#74458A">Problems & Engineering Concerns</span>

Software involving the following classes of problems:

* **Data integrity** — enforcing domain invariants at the database level instead of relying exclusively on application-side validation.
* **Concurrency & consistency** — designing operations that remain correct when multiple actors access and modify shared state simultaneously.
* **Backend architecture** — separating domain logic, persistence, transport, and authorization so individual components can evolve independently.
* **Relational data modeling** — translating domain constraints into explicit PostgreSQL schemas, indexes, constraints, and transaction boundaries.
* **Complex system behavior** — modeling systems where local rules, state transitions, and interactions produce non-trivial global behavior.
* **Low-level resource management** — handling ownership, lifetime, memory, and data structures explicitly in C++.
* **Spatial data organization** — structuring spatial data for efficient querying and interaction inside simulation environments.

## <span style="color:#8B3A4A">Projects</span>

### Schedule Manager

Multi-tenant appointment scheduling backend built with Python, FastAPI, psycopg3, and raw PostgreSQL.

Designed around problems involving concurrent scheduling, authorization, data integrity, and transaction correctness.

* Scheduling conflicts enforced through PostgreSQL `GIST` exclusion constraints rather than application-side locking.
* Capability-based authorization.
* Cookie-based JWT authentication with Argon2 password hashing.
* Asynchronous PostgreSQL access.
* Redis-based infrastructure for distributed application concerns.
* Layered service, repository, and router architecture.
* Explicit handling of transaction and concurrency boundaries.
* Automated testing covering concurrent behavior and database-dependent logic.

### Karkinolution

Creature ecosystem simulator exploring emergent behavior from simple local rules.

Originally implemented in Python and currently being ported to C++.

Designed around problems involving simulation architecture, state modeling, system decoupling, spatial representation, ownership, and complex interactions between independent systems.

* Decoupled models for organism state, perception, physiology, and behavior.
* Systems designed to allow new behaviors without restructuring existing components.
* Custom data structures and spatial representations.
* **R*-tree spatial indexing algorithm** for organizing and querying spatial data efficiently.
* Explicit C++ ownership and lifetime management.
* Automated testing and continuous integration.

## <span style="color:#74458A">AI-Assisted Engineering</span>

AI-assisted development is treated as an engineering tool for reducing implementation time while retaining human responsibility for architecture, correctness, and validation.

Applicable uses include:

* Exploring and comparing implementation approaches.
* Accelerating routine implementation.
* Generating and expanding test cases.
* Debugging and analyzing unfamiliar behavior.
* Refactoring and reviewing existing code.
* Producing documentation and development artifacts.

The relevant capability is not merely generating code, but integrating AI into an engineering workflow where generated results are reviewed, tested, constrained by the existing architecture, and validated against observable behavior.

## <span style="color:#8B3A4A">Development Focus</span>

Data structures and algorithms, backend architecture, database design, concurrency, systems programming, and the interaction between software architecture and data integrity.

---

<div align="center">

<a href="https://www.instagram.com/kooperative.rupestren" target="_blank">
<img src="https://img.shields.io/badge/Instagram-2b2b2b?style=flat-square&logo=instagram&logoColor=8B3A4A" height="32">
</a>

</div>

---

<div align="center">

<sub><span style="color:#74458A">Systems · Constraints · Correctness</span></sub>

</div>

