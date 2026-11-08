<div align="center">
  <img src="site/assets/social-preview.png" alt="Indra Gunawan Ardiansyah — Full-Stack Developer and Pragmatic Software Engineer" width="100%">
</div>

<div align="center">
  <h1>Indra Gunawan Ardiansyah</h1>
  <p><strong>Full-Stack Developer · Pragmatic Software Engineer</strong></p>
  <p>Building digital systems that solve real-world problems.</p>
  <p>
    <a href="https://github.com/irwansyah1998">GitHub</a>
    &nbsp;·&nbsp;
    <a href="mailto:nigun1998@gmail.com">Email</a>
    &nbsp;·&nbsp;
    <a href="#selected-work">Selected work</a>
    &nbsp;·&nbsp;
    <a href="#contact">Contact</a>
  </p>
</div>

> **Between doubt and reason, I choose both.** I approach engineering with curiosity and healthy skepticism: understand the problem, question unnecessary complexity, and build for how people and systems actually work.

**Based in Jombang, East Java, Indonesia** · **GitHub:** [@irwansyah1998](https://github.com/irwansyah1998)

> **Portfolio availability:** This repository contains the portfolio source, including the interactive website in [`site/`](site/). No public deployment or live website URL has been verified.

## Profile

I’m **Indra Gunawan Ardiansyah**, a full-stack developer interested in the systems behind useful software—from interfaces and APIs to data integrity, architecture, and the operations a system must support.

My experience brings together independent software development, a full-stack developer role at PT Bening Jaya Sentosa, and hands-on stock control and production-data reporting at PT Aksha Karunia Mill (PT AKM). Working with production records gives me practical insight into the gap between physical workflows and digital information: manual-entry risks, inconsistent records, reconciliation, traceability, and the limits of spreadsheet-based reporting.

My current PT AKM position is **operational stock and data control, not an IT engineering role**. I value that distinction: the operational experience informs how I think about software, but it is not presented as a completed software system.

> **“I don't just write code; I build systems for the real world.”**

## Engineering approach

| Principle | How it shapes my work |
|---|---|
| **Start with the work** | Understand users, operational workflows, data, and constraints before choosing a solution. |
| **Correctness first** | Treat reliable behavior, validation, and data integrity as core product requirements. |
| **Use proportionate architecture** | Prefer clear, maintainable systems; avoid dependencies and abstractions without a practical purpose. |
| **Design with security in mind** | Consider access, trust boundaries, and operational risk early in the design. |
| **Respect resources** | Account for performance, maintainability, and the cost of operating software. |

## Experience

### Stock Control & Operational Data Control · PT Aksha Karunia Mill
**December 2024 — Present**

Record and monitor peeled wood materials, materials awaiting rotary processing, and production input/output across eight rotary machines. Responsibilities include shift-based reporting, grades and volumes, spreadsheet workflows, stock control, and production-data reconciliation. This role provides practical domain context for data quality and traceability.

### Full-Stack Developer · PT Bening Jaya Sentosa
**2023 — 2024**

Worked on full-stack application features, frontend/backend integration, database-related development, troubleshooting, and maintenance for practical business-oriented applications.

### IT Freelancer · Intelligence of Technology Development
**2019 — Present**

Independent software development spanning web and full-stack applications, architecture and implementation, database integration, technical troubleshooting, and maintenance.

## Technical toolkit

Technologies and engineering areas represented in my portfolio. Listing a tool does not imply a proficiency score or a specific number of years using it.

| Area | Technologies and concepts |
|---|---|
| **Frontend** | HTML5, CSS3, JavaScript, Vue.js 3, Vite, Axios, Tailwind CSS |
| **Backend & APIs** | PHP, Laravel 10/11, CodeIgniter 3, REST APIs, Laravel Sanctum, OpenAPI |
| **Data** | MySQL, SQLite, PostgreSQL, relational design, normalization, SQL optimization |
| **Infrastructure** | Linux, Apache, Nginx, networking fundamentals, server administration |
| **Mobile exploration** | Flutter, Dart, Android, iOS |
| **Architecture & practice** | MVC, API contracts, role-based access, data integrity, security by design, performance and maintainability |

## Selected work

Projects are labeled by what can be verified. A public source repository is not a claim that a project is currently deployed; ideas and operational workflows are not described as finished software.

### Public source

| Project | Focus | Status |
|---|---|---|
| [Garment company data management](https://github.com/irwansyah1998/TugasAkhir) | CodeIgniter/PHP web application for organizing business data and supporting operational workflows. | Public source verified; deployment not verified. |
| [SiMadik · Education management](https://github.com/irwansyah1998/SiMadik) | CodeIgniter 3 school-management application; repository documentation describes attendance and administrative workflows. | Public source verified. The repository has a custom restrictive license; review its terms before use. |

### Operational case study

**Production data & stock control · PT Aksha Karunia Mill**

A real operational workflow covering shift reports, stock movement, and production records across eight rotary machines. This is maintained through operational records and spreadsheet reporting—not a completed software product. Possible software improvements such as validated inputs, audit trails, and centralized reporting remain proposals, not implemented features.

### Concepts and research

The following are **concepts, research, or projects whose implementation status is unverified**; they are not presented as completed products:

- **Indra Metered Connection** — Android network activity and connection-quality concept.
- **Peer-to-peer chat** — Flutter communication concept exploring peer identity and connectivity constraints.
- **Android memory inspector** — diagnostic-learning concept for applications I own or control, within Android sandbox boundaries.
- **Floating auto-tap** — user-directed Android accessibility concept, subject to platform permissions and restrictions.
- **IRW OS · Server core** — future exploration of modular Linux server management.
- **SEANKING content production** — AI-assisted content workflow research with human review.
- **Multi-language architecture** — research into language/runtime boundaries and system trade-offs.
- **CIF file compression** — future format research; the intended format and specification remain undefined.

## Architecture perspective

My portfolio documents two different reference patterns—not claims about currently deployed systems:

1. **Vue 3 + Laravel REST API:** a Vue single-page application communicates through Axios with a Laravel API; Sanctum protects routes, application services handle business logic, and OpenAPI/L5 Swagger describes the API.
2. **CodeIgniter 3 + MySQL:** a server-rendered MVC application keeps routing, session-based authentication, role checks, application logic, and persistence within one application boundary.

The right choice depends on the requirements: separating the interface and API can support independent development, while a monolith can keep a defined workflow simpler to operate. Both require deliberate attention to data integrity, access boundaries, and maintainability.

## Education

**Diploma III (D3), Informatics Engineering**

Universitas Sangga Buana YPKP Bandung · Graduated September 2020 · GPA **3.5 / 4.0**

## Contact

For professional inquiries, collaboration, or a conversation about practical software systems:

- **Email:** [nigun1998@gmail.com](mailto:nigun1998@gmail.com)
- **GitHub:** [github.com/irwansyah1998](https://github.com/irwansyah1998)
- **Location:** Jombang, East Java, Indonesia

## Explore this repository

The interactive, responsive portfolio website is implemented with semantic HTML, CSS, and vanilla JavaScript; it has no package manager or external runtime dependencies.

- [Open the portfolio source](site/index.html)
- [Read the architecture notes](docs/ARCHITECTURE.md)
- [Read the repository audit](docs/REPOSITORY-AUDIT.md)
- [Read the development documentation](Documentation.md)
- [View the changelog](CHANGELOG.md)

To preview the site locally, run from the repository root:

```powershell
python -m http.server 4173 --directory site
```

Then open `http://localhost:4173`. To run the dependency-free structural checks:

```powershell
python scripts/validate_site.py
```

There is no compilation/build step. GitHub Pages is not configured, and no deployment has been performed.

<details>
  <summary>Repository, accessibility, and license notes</summary>

- The site includes responsive layouts, visible keyboard focus, semantic landmarks, reduced-motion support, and keyboard-operable controls. Formal screen-reader and Lighthouse/Core Web Vitals results have not been measured.
- No repository-wide license file is present. Do not assume the website, assets, or linked project repositories are licensed for unrestricted reuse. SiMadik has its own custom restrictive license.
- Existing profile assets at the repository root are retained; they are not required to run the portfolio website.
</details>
