# Portfolio and reference architecture notes

## Portfolio site

```text
Browser
  ├─ site/index.html       semantic content and project data
  ├─ site/styles.css       design tokens, responsive layout, theme variants
  ├─ site/script.js        small progressive enhancements
  └─ site/assets/*         first-party favicon and social-preview artwork
```

The browser loads static files from the same origin. There is no API, server-side rendering, framework runtime, storage of personal data, or contact backend. Content remains in HTML; JavaScript only manages optional interactions. Project filters hide and reveal existing cards rather than fetching or mutating remote data. A static host can serve `site/` as its document root.

## State and accessibility contracts

- CSS custom properties define dark/light design tokens; `data-theme` on the root selects the palette.
- The selected palette is stored as a single `portfolio-theme` value in `localStorage`; a blocked/unavailable storage environment still supports the toggle for the current page.
- The mobile menu communicates open/closed state with `aria-expanded`, supports Escape and outside-click close, and has a visible keyboard focus path.
- Project status is stored declaratively in each card's `data-status`. Filter controls communicate their selected state via `aria-pressed`.
- Section navigation indicates the intersecting section when `IntersectionObserver` is supported; ordinary anchor navigation still works without it.
- Reduced-motion preferences disable smooth scrolling and minimize transitions.

## Reference implementation: decoupled Vue and Laravel

```text
Vue 3 SPA
    │ Axios / HTTP
    ▼
Laravel REST API routes
    │ Sanctum authentication middleware
    ▼
Backend services and application logic
    │ relational queries
    ▼
Database
```

The existing portfolio describes a Vue 3.2.13 frontend and Laravel 10 API, Axios transport, Laravel Sanctum, bearer-token authentication, local-storage token persistence, protected routes, L5 Swagger/OpenAPI, and PHPUnit 10 tests. This is a reference implementation description, not a claim that the application is currently hosted.

The frontend owns presentation and request state. Axios communicates over the REST contract. Middleware authenticates protected requests; backend services implement application behavior and interact with persistence. OpenAPI describes the API contract, while tests can verify backend behavior.

Trade-offs include independent UI/API development and clearer boundaries in exchange for deployment/API coordination. Storing bearer tokens in local storage exposes them to same-origin script access; an implementation should weigh that risk and use appropriate XSS controls and session/token policy. The diagram does not assert an undocumented database vendor.

## Reference implementation: CodeIgniter monolith

```text
AdminLTE / jQuery browser views
    │ browser request / server-rendered response
    ▼
CodeIgniter 3 routes, controllers, MVC application
    │ session authentication + role checks
    │ models / queries
    ▼
MySQL
```

The documented stack includes CodeIgniter 3.1.9, MySQL, AdminLTE, jQuery, MVC, session-based authentication, and role-based access. The role descriptions are:

| Role | Documented responsibilities |
|---|---|
| Admin | Full system CRUD and user management |
| Promosi | Product catalog and visual asset management |
| Manager | Reporting, operational oversight, and approvals |
| Staff | Raw material, labor, color, type, and order management |

A monolith can be practical when one application boundary closely matches the operational workflows and deployment needs. Its trade-offs include tighter coupling and potentially harder independent scaling, testing, or component replacement as scope grows. This description is not a claim of public deployment.

## Status and source evidence

The two linked repositories are public source references. The `SiMadik` repository has its own custom restrictive license; repository visibility is not an unrestricted-use grant. No live environment, service endpoint, production data, or deployed demo is included in these diagrams.
